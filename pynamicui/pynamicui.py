import customtkinter as tk

class VirtualDom:
    def __init__(self):
        self.root = tk.CTk()  # Create the root window
        self.elements = []
        self.routes = {}
        self.currentPage = None
        self.route = ""
        self.states = {}  # Dictionary to store state values and callbacks
        self.widget = self.root

    def render(self):
        for element in self.elements:
            element.render(self)  # Render each element in the root window
        self.root.mainloop()  # Start the main event loop

    def getCurrentRoute(self):
        return self.route

    def addRoute(self, url, element):
        self.routes[url] = element

    def getRoute(self, url):
        return self.routes[url]

    def nav(self, url):
        self.route = url
        if self.currentPage:
            self.currentPage.hide()
        self.currentPage = self.getRoute(url)
        self.currentPage.show()

    def addElement(self, element):
        self.elements.append(element)

    def getState(self, attr):
        return self.states[attr]["value"]

    def setState(self, attr, value):
        self.states[attr]["value"] = value
        if "callback" in self.states[attr]:
            self.states[attr]["callback"](self, value)

    def useState(self, name, value, callback):
        self.states[name] = {"value": value, "callback": callback}
        # Register a state with its initial value and associated callback

class VirtualElement:
    def __init__(self, tag, name=None, props=None, children=None, place=None, visible=True, hooks=None):
        self.name = name or "Pynamic" + tag + "Element"  # Name of the virtual element
        self.tag = "CTk" + tag  # Tag name for tkinter widget
        self.props = props or {}  # Dictionary to store widget properties
        self.children = children or []  # List of child elements
        self.widget = None  # Reference to the tkinter widget instance
        self.place = place  # Placement options for the widget
        self.visible = visible  # Flag to indicate element visibility
        self.hooks = hooks or {}  # Dictionary to store hooks
        self.parent = None  # Reference to the parent element

    def render(self, parent):
        self.parent = parent
        
        if self.visible:

            self.widget = getattr(tk, self.tag)(parent.widget)  # Create the tkinter widget
            for prop, value in self.props.items():
                self.widget.configure(**{prop: value})  # Configure widget properties

            for child in self.children:
                if child.visible:
                    child.render(self)  # Render each child element

            if self.place and self.visible:
                self.widget.place(**self.place)  # Place the widget in the parent

    def unmount(self):
        if self.widget:
            self.widget.destroy()
            self.widget = None
        for hook in self.hooks.values():
            if hook[1] is not None:
                hook[1](self)  # Invoke the unmount hook if present
        for child in self.children:
            child.unmount()  # Unmount each child element recursively

    def mount(self):
        if self.hooks.get(""):
            self.hooks[""][0](self)  # Invoke the mount hook if present
        for child in self.children:
            child.mount()  # Mount each child element recursively

    def useEffect(self, prop, callback, unmount=None):
        self.hooks[prop] = [callback, unmount]  # Register a hook with its callback and unmount function

    def setProp(self, prop, value):
        self.props[prop] = value  # Update the property value
        self.widget.configure(**{prop: value})  # Configure the updated property
        
        if self.hooks.get(prop):
            self.hooks[prop][0](self, value)  # Invoke the hook callback if present

    def hide(self):
        self.visible = False
        self.unmount()  # Unmount the element and its children
    
    def show(self):
        self.visible = True
        self.render(self.parent)  # Render the element in the parent
        self.mount()  # Mount the element and its children
