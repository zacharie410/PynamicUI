# PynamicUI

- [PynamicUI](#pynamicui)
  - [Features](#features)
  - [Developer Guide](#developer-guide)
    - [Installation](#installation)
    - [Importing the Library](#importing-the-library)
    - [Creating a Stylesheet](#creating-a-stylesheet)
      - [Example:](#example)
    - [Creating Components](#creating-components)
      - [Example: Creating a Navigation Bar Component](#example-creating-a-navigation-bar-component)
      - [Example: Creating a Counter Page Component](#example-creating-a-counter-page-component)
    - [The `App` Class](#the-app-class)
      - [Example:](#example-1)
    - [Running the App](#running-the-app)
    - [Conclusion](#conclusion)
- [PynamicUI: An In-Depth Look](#pynamicui-an-in-depth-look)
  - [Introduction](#introduction)
  - [Inspirations from React](#inspirations-from-react)
  - [Inspirations from CSS and HTML](#inspirations-from-css-and-html)
  - [Use of CustomTkinter](#use-of-customtkinter)
  - [Facilitating Application Development](#facilitating-application-development)
  - [Conclusion](#conclusion-1)
- [PynamicUI: What Sets It Apart](#pynamicui-what-sets-it-apart)
  - [1. Dynamic User Interfaces with Virtual DOM](#1-dynamic-user-interfaces-with-virtual-dom)
  - [2. Component-Based Architecture](#2-component-based-architecture)
  - [3. CSS-Inspired Styling](#3-css-inspired-styling)
  - [4. Integration with Tkinter via CustomTkinter](#4-integration-with-tkinter-via-customtkinter)
  - [5. Streamlined Application Development](#5-streamlined-application-development)
  - [6. Active Development and Community Support](#6-active-development-and-community-support)
  - [7. Lightweight and Non-Intrusive](#7-lightweight-and-non-intrusive)
  - [Conclusion](#conclusion-2)


PynamicUI is a lightweight Python library that provides a dynamic user interface (UI) framework for creating interactive and responsive applications. It simplifies the process of building user interfaces by abstracting away the complexities of working directly with a UI toolkit like Tkinter. With PynamicUI, you can create dynamic web-like UIs using a declarative syntax, making it easy to define and manage the UI components and their interactions.

## Features

- **Virtual DOM:** PynamicUI implements a Virtual DOM architecture, allowing you to define UI components using a declarative approach. The Virtual DOM efficiently manages updates and renders the UI components when necessary.

- **State Management:** PynamicUI includes a built-in state management system, allowing you to define and manage application states. State changes trigger automatic UI updates, ensuring your UI stays in sync with the underlying data.

- **Hooks and Effects:** PynamicUI provides hooks and effects to add custom logic and side effects to your UI components. You can utilize hooks to perform actions when components mount, unmount, or update. Effects enable you to respond to changes in state or other component properties.

- **Routing and Navigation:** PynamicUI supports routing and navigation, allowing you to create multi-page applications. You can define routes and associate them with specific UI components, enabling seamless navigation between different pages.

- **Stylesheets and nested styles** PynamicUI supports mapped stylesheets, allowing you to create fast and smooth style transitions. Most importantly it helps keep your different modules readable and in scope.


## Developer Guide
An extensive developer guide for PynamicUI. We'll cover the main classes and their methods, along with examples to demonstrate how to use them effectively.

### Installation

Before you begin, make sure you have installed PynamicUI. You can install it using pip:

```bash
pip install PynamicUI
```

### Importing the Library

To use PynamicUI, import the necessary elements from the library:

```python
from pynamicui.pynamicui import *
```

### Creating a Stylesheet

The `StylesheetConstructor` class is responsible for creating and managing stylesheets. You can add styles dynamically and create nested styles that inherit from existing styles.

#### Example:

```python
# Create a stylesheet instance
styles = createStylesheet()

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

# Adding a nested style that inherits from "PrimaryButton" and updates "fg_color"
styles.addNestedStyle("PrimaryButton", "NestedPrimaryButton", {
    "fg_color": "darkblue",
})
```

### Creating Components

Components are the building blocks of your user interface. In PynamicUI, you create components using classes that represent different parts of your application.

#### Example: Creating a Navigation Bar Component

```python
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
```

#### Example: Creating a Counter Page Component

```python
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
```

### The `App` Class

The `App` class acts as the main application class. It initializes the virtual DOM, sets the stylesheet, and creates instances of different components.

#### Example:

```python
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
```

### Running the App

To run the app, create an instance of the `App` class:

```python
if __name__ == "__main__":
    App()
```

Now you have a complete example of creating a dynamic user interface using PynamicUI. You can further extend the application by adding more components, styles, and interactions based on your specific use case.

### Conclusion

Congratulations! You have successfully learned how to create dynamic user interfaces using PynamicUI. You can now build complex and interactive applications with ease by leveraging the power of virtual DOM and dynamic component creation. Explore the documentation for more advanced features and customization options. Happy coding!

# PynamicUI: An In-Depth Look

## Introduction

PynamicUI is a Python library that simplifies the process of creating dynamic user interfaces for desktop applications. It takes inspiration from popular web development frameworks like React, the styling capabilities of CSS, and the structure of HTML. The library also utilizes CustomTkinter as a widget library to ensure cross-compatibility and seamless integration with Tkinter, one of the standard GUI frameworks in Python.

## Inspirations from React

React is a widely-used JavaScript library for building user interfaces, known for its component-based architecture and the concept of a virtual DOM. PynamicUI borrows the idea of components and implements a similar virtual DOM approach to efficiently update and render UI elements when their state changes. Components in PynamicUI are classes that represent different parts of the user interface, and they can be dynamically created and updated.

React's unidirectional data flow principle is also reflected in PynamicUI, where changes to the application's state trigger re-rendering of the virtual DOM and subsequently update the user interface. This helps in maintaining a clear separation of concerns and facilitates the building of complex UIs with ease.

## Inspirations from CSS and HTML

Styling in PynamicUI takes inspiration from CSS. Styles are defined using dictionaries containing key-value pairs for attributes such as font, color, padding, etc. The StylesheetConstructor class allows for dynamic creation and management of styles, offering a similar experience to working with CSS.

PynamicUI's createElement function is reminiscent of HTML, where you can create elements like Buttons, Labels, Frames, etc., and define their properties and styles in a familiar HTML-like syntax. This makes it intuitive for developers with experience in web development to transition into creating desktop applications with PynamicUI.

## Use of CustomTkinter

CustomTkinter is a widget library developed for PynamicUI that sits on top of the standard Tkinter library. It extends the functionality of Tkinter and introduces additional features required to implement the dynamic nature of PynamicUI.

By using CustomTkinter, PynamicUI ensures cross-compatibility and maintains the robustness of the Tkinter framework. CustomTkinter is well-maintained and designed to seamlessly integrate with PynamicUI, providing developers with a stable and consistent experience when building GUI applications.

## Facilitating Application Development

PynamicUI is a facilitator that aims to simplify the process of creating Python GUI desktop applications. By taking inspiration from popular web development frameworks and adopting familiar concepts from CSS and HTML, PynamicUI reduces the learning curve for developers. Its component-based architecture and virtual DOM approach make it easy to build interactive and responsive user interfaces.

The library does not aim to introduce overly complex or fancy features; instead, it focuses on making the development workflow more accessible and efficient. PynamicUI streamlines the UI creation process, allowing developers to focus on the core logic of their applications without worrying about the intricacies of GUI design.

## Conclusion

In conclusion, PynamicUI is a powerful yet straightforward library that empowers Python developers to create dynamic user interfaces for desktop applications. Taking inspiration from React, CSS, and HTML, PynamicUI offers a familiar development experience while leveraging CustomTkinter for cross-compatibility and reliable integration with Tkinter. By serving as a facilitator, PynamicUI aims to make GUI desktop application development in Python easier, faster, and more enjoyable for developers of all levels of experience.

# PynamicUI: What Sets It Apart

PynamicUI stands out as a unique and viable option for developers looking to build dynamic user interfaces for Python desktop applications. Its distinctive features and benefits make it an excellent choice for various use cases. Let's explore what sets PynamicUI apart and why it's a viable option for developers:

## 1. Dynamic User Interfaces with Virtual DOM

One of the key differentiators of PynamicUI is its adoption of the virtual DOM approach. Inspired by web development frameworks like React, PynamicUI efficiently manages updates and re-renders only the necessary components when the application's state changes. This dynamic nature significantly enhances the performance and responsiveness of the user interface, making it ideal for applications with complex and interactive UI requirements.

## 2. Component-Based Architecture

PynamicUI embraces a component-based architecture, mirroring React's paradigm. Components are modular building blocks of the user interface, encapsulating their own logic, styles, and state. This promotes code reusability, maintainability, and separation of concerns, enabling developers to build complex applications in a structured and organized manner.

## 3. CSS-Inspired Styling

Styling in PynamicUI draws inspiration from CSS, providing developers with a familiar and intuitive way to define styles for UI elements. Styles are created using dictionaries containing key-value pairs for various attributes, such as font, color, padding, etc. The StylesheetConstructor class allows for the dynamic creation and management of styles, streamlining the process of designing visually appealing and consistent user interfaces.

## 4. Integration with Tkinter via CustomTkinter

PynamicUI leverages CustomTkinter, a well-maintained widget library that extends the functionality of the standard Tkinter library. By building on top of Tkinter, PynamicUI ensures cross-compatibility and stability. Developers can seamlessly use PynamicUI's features alongside Tkinter's existing components and functionalities, making it a viable option for those already familiar with Tkinter.

## 5. Streamlined Application Development

PynamicUI is designed to facilitate the creation of Python GUI desktop applications by minimizing the complexity of UI development. By providing developers with familiar concepts from web development and simplifying the creation and management of styles and components, PynamicUI streamlines the application development workflow. This allows developers to focus more on application logic and functionality and less on the intricacies of GUI design.

## 6. Active Development and Community Support

PynamicUI benefits from active development and a growing community of contributors and users. This active community ensures that the library is regularly updated, improved, and supported. Developers can rely on PynamicUI as a viable long-term option for building Python desktop applications, knowing that it will continue to evolve and adapt to their needs.

## 7. Lightweight and Non-Intrusive

PynamicUI is lightweight and non-intrusive, allowing developers to integrate it seamlessly into their existing projects. The library does not impose heavy dependencies or substantial changes to the development environment. Developers can easily adopt PynamicUI without disrupting their existing workflow, making it an attractive option for both new and existing projects.

## Conclusion

PynamicUI's dynamic user interfaces, component-based architecture, CSS-inspired styling, integration with Tkinter via CustomTkinter, streamlined development process, and active community support make it a standout and viable option for developers. Its ability to simplify and enhance the creation of Python GUI desktop applications sets it apart and positions it as an excellent choice for projects of all sizes and complexities. Whether you are a seasoned developer or new to GUI application development, PynamicUI empowers you to build engaging and interactive user interfaces with ease and efficiency.