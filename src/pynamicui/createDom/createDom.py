import customtkinter as tk

class createDom:
    def __init__(self):
        self.root = tk.CTk()  # Create the root window
        self.elements = []
        self.routes = {}
        self.currentPage = None
        self.route = ""
        self.states = {}  # Dictionary to store state values and callbacks
        self.widget = self.root
        self.stylesheet = {}

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
        if "callbacks" in self.states[attr]:
            for callback in self.states[attr]["callbacks"]:
                callback(attr, self, value)

    def useState(self, attr, value, callback):
        st = self.states.get(attr)
        if st:
            self.states[attr] = {"value": value, "callbacks": st.callbacks.append(callback)}
        else:
            self.states[attr] = {"value": value, "callbacks": [callback]}
        # Register a state with its initial value and associated callback

    def setStylesheet(self, sheet):
        self.stylesheet=sheet

    def setGeometry(self, val):
        if self.widget:
            self.widget.geometry(val)