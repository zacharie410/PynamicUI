import customtkinter as tk

def findDom(parent):
    if hasattr(parent, "root"):
        return parent
    elif hasattr(parent, "parent"):
        return findDom(parent.parent)
    else:
        # If no "root" attribute is found and there is no "parent" attribute, return None or raise an exception
        return None

def applyPaddingToGeometry(geometry, padx, pady):
    """
    Adjust the geometry with padx and pady values relative to the scale of relwidth and relheight.

    Parameters:
        geometry (dict): A dictionary representing the geometry with keys 'relwidth', 'relheight', 'relx', and 'rely'.
        padx (float): The padding value to be applied relative to the scale of relwidth.
        pady (float): The padding value to be applied relative to the scale of relheight.

    Returns:
        dict: A new dictionary with adjusted geometry values after applying padding.
    """
    adjustedGeometry = {}

    scale_width = geometry.get('relwidth', 1)
    scale_height = geometry.get('relheight', 1)

    adjustedGeometry['relwidth'] = scale_width - (scale_width * padx)
    adjustedGeometry['relheight'] = scale_height - (scale_height * pady)

    adjustedGeometry['relx'] = geometry.get('relx', 0) + (.5 * scale_width * padx)
    adjustedGeometry['rely'] = geometry.get('rely', 0) + (.5 * scale_height * pady)

    return adjustedGeometry

class createElement:
    def __init__(self, parent, tag, name=None, props=None, children=None, place=None, visible=True, hooks=None, style=None, spacing=None):
        self.parent = parent
        self.name = name or "Pynamic" + tag + "Element"  # Name of the virtual element
        self.tag = "CTk" + tag  # Tag name for tkinter widget
        self.props = props or {}  # Dictionary to store widget properties
        self.children = children or []  # List of child elements
        self.widget = None  # Reference to the tkinter widget instance
        self.currentPlace = place or {}  # Placement options for the widget
        self.spacing = spacing or {"padx": 0, "pady": 0} # padx and pady
        self.visible = visible  # Flag to indicate element visibility
        self.hooks = hooks or {}  # Dictionary to store hooks
        self.style = style or ""
        self.mounted = False

        if hasattr(self.parent, "root"):
            self.dom = self.parent
            self.dom.appendChild(self)
        elif self.parent:
            self.dom = findDom(self.parent.parent)
            self.parent.appendChild(self)
        

    def render(self):
        if self.visible:
            
            if self.widget:
                self.widget.destroy()
            self.widget = getattr(tk, self.tag)(self.parent.widget)  # Create the tkinter widget
            for prop, value in self.props.items():
                self.widget.configure(**{prop: value})  # Configure widget properties
            
            self.updateStyle()

            for child in self.children:
                if child.visible:
                    child.render()  # Render each child element

            self.place(self.currentPlace)  # Place the widget in the parent

    def unmount(self):
        self.mounted = False
        for prop, hook in self.hooks.items():
            if hook[1] is not None:
                hook[1](prop, self, self.props.get(prop))  # Invoke the unmount hook if present
        for child in self.children:
            child.unmount()  # Unmount each child element recursively
        if self.widget:
            self.widget.destroy()
            self.widget = None

    def mount(self):
        self.mounted = True
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
        self.render()  # Render the element in the parent
        self.mount()  # Mount the element and its children

    def setStyle(self, style):
        self.style = style
        self.updateStyle()

    def place(self, geometry):
        self.currentPlace = geometry
        if self.widget:
            self.widget.place(**applyPaddingToGeometry(self.currentPlace, self.spacing.get("padx", 0), self.spacing.get("pady", 0)))

    def updateStyle(self):
        if self.style != "" and self.widget:
            for item, value in self.dom.stylesheet[self.style].items():
                if item in self.spacing:
                    self.spacing[item] = value
                else:
                    self.widget.configure(**{item: value})

    def appendChild(self, child):
        if child in child.parent.children:
            index_to_remove = child.parent.children.index(child)
            child.parent.children.pop(index_to_remove)
        self.children.append(child)
        child.parent = self

    def setParent(self, parent):
        if self in self.parent.children:
            index_to_remove = self.parent.children.index(self)
            self.parent.children.pop(index_to_remove)
        self.parent = parent
        if hasattr(self.parent, "root"):
            self.dom = self.parent
            self.dom.appendChild(self)
        elif self.parent:
            self.dom = findDom(self.parent.parent)
            self.parent.appendChild(self)
        self.render()

    def destroy(self):
        if self in self.parent.children:
            index_to_remove = self.parent.children.index(self)
            self.parent.children.pop(index_to_remove)
        self.parent = None
        if self.widget:
            self.widget.destroy()
        self.props = {}
        self.hooks = {}
        for child in self.children:
            child.destroy()
        del self


