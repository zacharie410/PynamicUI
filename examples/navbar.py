from pynamicui import createDom, createElement, createStylesheet

class NavBarApp:
    def __init__(self, dom):
        self.dom = dom

        # Create a frame container for the navigation bar
        self.navbar_container = createElement(self.dom, "Frame", place={"relwidth": 1, "relheight": 0.1})

        # Create the navigation buttons
        self.home_button = createElement(self.navbar_container, "Button", style="NavButton", props={"text": "Home", "command": lambda: self.dom.nav("home")}, place={"relwidth": 0.25, "relheight": 1})
        self.about_button = createElement(self.navbar_container, "Button", style="NavButton", props={"text": "About", "command": lambda: self.dom.nav("about")}, place={"relwidth": 0.25, "relheight": 1, "relx": 0.25})
        self.products_button = createElement(self.navbar_container, "Button", style="NavButton", props={"text": "Products", "command": lambda: self.dom.nav("products")}, place={"relwidth": 0.25, "relheight": 1, "relx": 0.5})
        self.contact_button = createElement(self.navbar_container, "Button", style="NavButton", props={"text": "Contact", "command": lambda: self.dom.nav("contact")}, place={"relwidth": 0.25, "relheight": 1, "relx": 0.75})

        # Create a frame container for the content pages
        self.pages_container = createElement(self.dom, "Frame", place={"relwidth": 1, "relheight": 0.9, "rely": 0.1})

        # Create the pages
        self.home_page = createElement(self.pages_container, "Frame", visible=False, place={"relwidth": 1, "relheight": 1})
        self.home_label = createElement(self.home_page, "Label", props={"text": "Welcome to Home Page"}, place={"relwidth": 1, "relheight": 1})

        self.about_page = createElement(self.pages_container, "Frame", visible=False, place={"relwidth": 1, "relheight": 1})
        self.about_label = createElement(self.about_page, "Label", props={"text": "Welcome to About Page"}, place={"relwidth": 1, "relheight": 1})

        self.products_page = createElement(self.pages_container, "Frame", visible=False, place={"relwidth": 1, "relheight": 1})
        self.products_label = createElement(self.products_page, "Label", props={"text": "Welcome to Products Page"}, place={"relwidth": 1, "relheight": 1})

        self.contact_page = createElement(self.pages_container, "Frame", visible=False, place={"relwidth": 1, "relheight": 1})
        self.contact_label = createElement(self.contact_page, "Label", props={"text": "Welcome to Contact Page"}, place={"relwidth": 1, "relheight": 1})

        # Add the pages to the DOM routing
        self.dom.addRoute("home", self.home_page)
        self.dom.addRoute("about", self.about_page)
        self.dom.addRoute("products", self.products_page)
        self.dom.addRoute("contact", self.contact_page)

        #Go to home page
        self.dom.nav("home")

# Create the virtual DOM
dom = createDom()

dom.root.title("navbar.py")

stylesheet = createStylesheet()

stylesheet.addStyle("NavButton", {"padx" : 0.05, "pady" : 0.1})

dom.setStylesheet(stylesheet)

#Set the window size
dom.setGeometry("800x600")

# Render the NavBarApp component
navbar_app = NavBarApp(dom)

# Render the virtual DOM
dom.render()
