import customtkinter as tk

def findDom(parent):
    if hasattr(parent, "root"):
        return parent
    elif hasattr(parent, "parent"):
        return findDom(parent.parent)
    else:
        # If no "root" attribute is found and there is no "parent" attribute, return None or raise an exception
        return None

def parseGrid(cols, rows, grid):
    """
    Parse a grid of ids into usable place geometry

    Parameters:
        cols (float): The width\n
        rows (float): The Length\n
        grid (list): A list representing the geometry with ids, for example a 2 x 3 grid:\n
        ["1", "2",\n
        "1", "2",\n
        "4", "3"\n
        ]\n
        This parses into a grid with 4 elements.\n


    Returns:
        dict: A new dictionary with geometry values after applying grid locations from ids.
    """
    # Initialize an empty dictionary for storing parsed grid
    parsed_grid = {}

    # Loop through each item in the grid
    for i, item in enumerate(grid):
        # If the current item hasn't been processed yet
        if not parsed_grid.get(item):
            # Calculate the row and column of the current item based on its index
            row, col = i // cols, i % cols

            # Initialize row_span and col_span as 1 (each item spans at least one row and one column)
            row_span = 1
            col_span = 1

            # Loop through each item in the grid starting from the item after the current one
            for n in range(i + 1, rows * cols):
                # If an item is the same as the current item
                if grid[n] == item:
                    # Calculate its row and column based on its index
                    x, y = n // cols, n % cols

                    # If the item is in the same column but a different row, increment the row span
                    if y == col and x > row:
                        row_span += 1
                    # If the item is in the same row but a different column, increment the column span
                    elif y > col and x == row:
                        col_span += 1

            # Add the parsed item to the parsed grid dictionary, with its tag as the key
            parsed_grid[item] = {
                # The relative width and height are calculated as the span divided by the total number of columns/rows
                "relwidth": col_span / cols,
                "relheight": row_span / rows,
                # The relative x and y coordinates are calculated as the column/row number divided by the total number of columns/rows
                "relx": col / cols,
                "rely": row / rows
            }
    # Return the parsed grid
    return parsed_grid



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
    def __init__(self, parent, tag, id=None, name=None, props=None, children=None, place=None, visible=True, hooks=None, style=None, spacing=None):
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
        self.id = id or None
        self.grid = None

        if hasattr(self.parent, "root"):
            self.dom = self.parent
            self.dom.appendChild(self)
        elif self.parent:
            self.dom = findDom(self.parent.parent)
            self.parent.appendChild(self)

    def render(self):
        """
        Render the element and its descendents
        """
        if self.visible:
            
            if self.widget:
                self.widget.destroy()
            self.widget = getattr(tk, self.tag)(self.parent.widget)  # Create the tkinter widget
            for prop, value in self.props.items():
                self.widget.configure(**{prop: value})  # Configure widget properties
            
            self.updateStyle()


            for child in self.children:
                if child.visible:
                    if self.grid and child.id:
                        pos = self.grid.get(child.id)
                        if pos:
                            child.place(pos)
                    child.render()  # Render each child element

            self.place(self.currentPlace)  # Place the widget in the parent

    def unmount(self):
        """
        PRIVATE: Unmount the element to virtual dom (interal use)
        """
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
        """
        PRIVATE: Mount the element to virtual dom (interal use)
        """
        self.mounted = True
        if self.hooks.get("") and self.hooks[""][0]:
            self.hooks[""][0]("", self, True)  # Invoke the mount hook if present
        for child in self.children:
            child.mount()  # Mount each child element recursively

    def useEffect(self, props=[""], hook=None, unmount=None):
        """
        Attach a hook, typical examples: \n
        props defaults to [""], which calls automatically on mount
        """
        for prop in props:
            self.hooks[prop] = [hook, unmount]  # Register a hook with its callback and unmount function

    def setProp(self, prop, value):
        """
        Set a Widget prop value (Must be a valid element prop (refer to wiki))
        """
        self.props[prop] = value  # Update the property value
        self.widget.configure(**{prop: value})  # Configure the updated property
        
        if self.hooks.get(prop):
            self.hooks[prop][0](prop, self, value)  # Invoke the hook callback if present

    def hide(self):
        """
        Hide element and its descendants (Will call unmount event)
        """
        self.visible = False
        self.unmount()  # Unmount the element and its children
    
    def show(self):
        """
        Show the element and its descendants (Will call mount event)
        """
        self.visible = True
        self.render()  # Render the element in the parent
        self.mount()  # Mount the element and its children

    def setStyle(self, style):
        """
        Set the element's style and apply the changes to the rendered widget
        """
        self.style = style
        self.updateStyle()

    def place(self, geometry):
        """
        Set the element's geometry and place the widget if it exists
        """
        self.currentPlace = geometry
        if self.widget:
            self.widget.place(**applyPaddingToGeometry(self.currentPlace, self.spacing.get("padx", 0), self.spacing.get("pady", 0)))

    def updateStyle(self):
        """
        This will apply any styling to the element's widget.
        """
        if self.style != "" and self.widget:
            for item, value in self.dom.stylesheet[self.style].items():
                if item in self.spacing:
                    self.spacing[item] = value
                else:
                    self.widget.configure(**{item: value})

    def appendChild(self, child):
        """
        Append a child to this element and remove the child from any other element's child list
        """
        if child in child.parent.children:
            index_to_remove = child.parent.children.index(child)
            child.parent.children.pop(index_to_remove)
        self.children.append(child)
        child.parent = self

    def setGrid(self, width, height, grid):
        """ Example input:
        element.setGrid(4, 4, [\n
            "7", "7", "7", "7",\n
            "1", "2", "5", "5",\n
            "1", "2", "5", "5",\n
            "1", "2", "3", "3"\n
         ])
        # Elements with matching id will be assigned the following parsed places:\n
         element.grid = {\n
             '7': {'relwidth': 1.0, 'relheight': 0.25, 'relx': 0.0, 'rely': 0.0},\n
             '1': {'relwidth': 0.25, 'relheight': 0.75, 'relx': 0.0, 'rely': 0.25},\n
             '2': {'relwidth': 0.25, 'relheight': 0.75, 'relx': 0.25, 'rely': 0.25},\n
             '5': {'relwidth': 0.5, 'relheight': 0.5, 'relx': 0.5, 'rely': 0.25},\n
             '3': {'relwidth': 0.5, 'relheight': 0.25, 'relx': 0.5, 'rely': 0.75}\n
         }\n
         So a child element with id '7' would have a place of {'relwidth': 1.0, 'relheight': 0.25, 'relx': 0.0, 'rely': 0.0},\n
         and a child element with an id of '1' would have a place of {'relwidth': 0.25, 'relheight': 0.75, 'relx': 0.0, 'rely': 0.25},\n
        """
        if grid:
            self.grid = parseGrid(width, height, grid)
        else:
            self.grid = None

    def setParent(self, parent):
        """
        Set the parent of the element to somewhere within the virtual DOM (must be another element or the DOM itself)
        """
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
        """
        Destroy the element and all its children from the virtual DOM
        """
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


