import customtkinter as tk

class createElement:
    def __init__(self, dom, tag, name=None, props=None, children=None, place=None, visible=True, hooks=None, style=None):
        self.dom = dom
        self.name = name or "Pynamic" + tag + "Element"  # Name of the virtual element
        self.tag = "CTk" + tag  # Tag name for tkinter widget
        self.props = props or {}  # Dictionary to store widget properties
        self.children = children or []  # List of child elements
        self.widget = None  # Reference to the tkinter widget instance
        self.place = place  # Placement options for the widget
        self.visible = visible  # Flag to indicate element visibility
        self.hooks = hooks or {}  # Dictionary to store hooks
        self.parent = None  # Reference to the parent element
        self.style = style or ""

    def render(self, parent):
        self.parent = parent
        
        if self.visible:

            self.widget = getattr(tk, self.tag)(parent.widget)  # Create the tkinter widget
            for prop, value in self.props.items():
                self.widget.configure(**{prop: value})  # Configure widget properties
            
            self.updateStyle()

            for child in self.children:
                if child.visible:
                    child.render(self)  # Render each child element

            if self.place and self.visible:
                self.widget.place(**self.place)  # Place the widget in the parent

    def unmount(self):
        if self.widget:
            self.widget.destroy()
            self.widget = None
        for prop, hook in self.hooks.items():
            if hook[1] is not None:
                hook[1](prop, self, self.props.get(prop))  # Invoke the unmount hook if present
        for child in self.children:
            child.unmount()  # Unmount each child element recursively

    def mount(self):
        if self.hooks.get("") and self.hooks[""][0]:
            self.hooks[""][0]("", self, True)  # Invoke the mount hook if present
        for child in self.children:
            child.mount()  # Mount each child element recursively

    def useEffect(self, props=[""], hook=None, unmount=None):
        for prop in props:
            self.hooks[prop] = [hook, unmount]  # Register a hook with its callback and unmount function

    def setProp(self, prop, value):
        self.props[prop] = value  # Update the property value
        self.widget.configure(**{prop: value})  # Configure the updated property
        
        if self.hooks.get(prop):
            self.hooks[prop][0](prop, self, value)  # Invoke the hook callback if present

    def hide(self):
        self.visible = False
        self.unmount()  # Unmount the element and its children
    
    def show(self):
        self.visible = True
        self.render(self.parent)  # Render the element in the parent
        self.mount()  # Mount the element and its children

    def setStyle(self, style):
        self.style = style
        self.updateStyle()

    def updateStyle(self):
        if self.style != "" and self.widget:
            for item, value in self.dom.stylesheet[self.style].items():
                self.widget.configure(**{item: value})
