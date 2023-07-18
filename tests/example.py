
from pynamicui_zacharie410 import (createStylesheet, createDom, createElement, setAppearanceMode)

import customtkinter as tk
styles = createStylesheet()
# Create Stylesheet
# Adding styles dynamically
styles.addStyle("PrimaryButton", {
    "font": ("Arial", 14, "normal"),
    "fg_color": "grey",
    "bg_color": "blue"
})
styles.addStyle("SecondaryButton", {
    "font": ("Arial", 14, "normal"),
    "fg_color": "black",
    "bg_color": "green"
})
# Adding a nested style that inherits from "PrimaryButton" and updates "bg_color"
styles.addNestedStyle("PrimaryButton", "NestedPrimaryButton", {
    "fg_color": "darkblue",
})

class NavBar:
    def __init__(self, dom):
        self.dom = dom
 
        # Create the home navigation button
        self.navButton = createElement(self.dom,
            "Button",
            style="PrimaryButton",
            props={"text": "Home", "command": lambda: self.dom.nav("home")},
            place={"relwidth": 0.5, "relheight": 1, "rely": 0},
        )
        
        # Create the about navigation button
        self.navButton2 = createElement(self.dom,
            "Button",
            style="NestedPrimaryButton",
            props={"text": "About", "command": lambda: self.dom.nav("about")},
            place={"relwidth": 0.5, "relheight": 1, "relx": 0.5},
        )
        
        # Create the navigation bar containing the buttons
        self.navBar = createElement(self.dom,
            "Frame",
            children=[self.navButton, self.navButton2],
            place={"relwidth": 1, "relheight": 0.2},
            visible=True
        )

        # Add the navigation bar element to the virtual DOM
        self.dom.addElement(self.navBar)


class CounterPage:
    def __init__(self, dom):
        self.dom = dom

        # Create the counter button
        self.counterButton = createElement(self.dom,
            "Button",
            props={"text": "Click Me", "command": lambda: self.increment("counter")},
            place={"relwidth": 1, "relheight": 0.2, "rely": 0.3},
        )

        # Create the counter label
        self.counterLabel = createElement(self.dom,
            "Label",
            name="counterLabel",
            props={"text": "0"},
            place={"relwidth": 1, "relheight": 0.5, "rely": 0.5},
        )

        # Create the counter page containing the button and label
        self.page1 = createElement(self.dom,
            "Frame",
            children=[self.counterButton, self.counterLabel],
            place={"relwidth": 1, "relheight": .8, "rely": 0.2},
            visible=False
        )

        # Add the counter page element to the virtual DOM
        self.dom.addElement(self.page1)

        # Add a route to the virtual DOM
        self.dom.addRoute("home", self.page1)

        # Add hooks for the counter label
        self.counterLabel.useEffect(props=["", "text"], hook=self.effect, unmount=self.elementDidUnmount)

        # Set up a state for the counter
        self.dom.useState("counter", 0, self.change)


    def elementDidMount(self, prop, element, value):
        print("Mounted element: " + element.name)

    def elementDidUnmount(self, prop, element, value):
        if prop=="":
            print("Unmounted element: " + element.name)

    def increment(self, attr):
        value = self.dom.getState(attr)
        value += 1
        self.dom.setState(attr, value)

    def effect(self, prop, element, value):
        if prop == "":
            self.elementDidMount(prop, element, value)
            return
        print(prop + str(value))

    def change(self, prop, element, value):
        self.counterLabel.setProp("text", str(value))


class AboutPage:
    def __init__(self, dom):
        self.dom = dom

        # Create the about label
        self.aboutLabel = createElement(self.dom,
            "Label",
            props={"text": "About page"},
            place={"relwidth": 1, "relheight": 0.2},
        )
        
        # Create the about button
        self.aboutButton = createElement(self.dom,
            "Button",
            props={"text": "Click Me", "command": lambda: self.action()},
            place={"relwidth": 1, "relheight": 0.2, "rely": 0.3},
        )

        # Create the about page containing the label and button
        self.page2 = createElement(self.dom,
            "Frame",
            children=[self.aboutLabel, self.aboutButton],
            place={"relwidth": 1, "relheight": .8, "rely": 0.2},
            visible=False
        )

        # Add the about page element to the virtual DOM
        self.dom.addElement(self.page2)

        # Add a route to the virtual DOM
        self.dom.addRoute("about", self.page2)

        self.aboutLabel.useEffect(props=[""], hook=self.elementDidMount, unmount=self.elementDidUnmount)

    def elementDidMount(self, prop, element, value):
        print("Mounted element: " + element.name)

    def elementDidUnmount(self, prop, element, value):
        print("Unmounted element: " + element.name)

    def action(self):
        if self.aboutLabel.visible:
            self.aboutLabel.hide()
            self.aboutButton.setStyle("PrimaryButton")
        else:
            self.aboutLabel.show()
            self.aboutButton.setStyle("SecondaryButton")


class App:
    def __init__(self):
        self.dom = createDom()
        self.dom.setStylesheet(styles.stylesheet)
        self.dom.setGeometry("800x600")
        # Create the navbar component
        self.navbar = NavBar(self.dom)

        # Create the counter page component
        self.counterPage = CounterPage(self.dom)

        # Create the about page component
        self.aboutPage = AboutPage(self.dom)

        #Style

        setAppearanceMode("Light")

        # Render the virtual DOM
        self.dom.render()


# Launch app
# Example usage
if __name__ == "__main__":
    App()
