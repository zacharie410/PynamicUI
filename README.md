# PynamicUI

PynamicUI is a lightweight Python library that provides a dynamic user interface (UI) framework for creating interactive and responsive applications. It simplifies the process of building user interfaces by abstracting away the complexities of working directly with a UI toolkit like Tkinter. With PynamicUI, you can create dynamic web-like UIs using a declarative syntax, making it easy to define and manage the UI components and their interactions.

## Features

- **Declarative Syntax:** Define UI components using a declarative syntax similar to HTML, making it intuitive and easy to manage.
- **Dynamic Rendering:** Efficiently render virtual elements as tkinter widgets, ensuring responsiveness and interactivity.
- **State Management:** Manage the state of your application and automatically update the UI when state changes occur.
- **Hooks and Effects:** Utilize hooks and effects to add custom logic and side effects to elements, enhancing interactivity.
- **Styling Capabilities:** Apply styles to UI elements with ease, allowing for seamless customization of appearance.
- **Responsive and Interactive UIs:** Build dynamic and responsive user interfaces with web-like interactions.

## Installation

PynamicUI requires the `CustomTkinter` library. To install PynamicUI and its dependencies, you can use `pip`:

```bash
pip install pynamicui
```

## Documentation

For detailed documentation and usage examples, please refer to the [PynamicUI Wiki](https://github.com/zacharie410/PynamicUI/wiki).

## Examples

Check out the [examples](https://github.com/zacharie410/PynamicUI/blob/main/examples/) folder for practical examples building an application with PynamicUI.

### [Example Calculator App](https://github.com/zacharie410/PynamicUI/wiki/Example-Calculator-App)
![App](https://github.com/zacharie410/PynamicUI/blob/main/examples/screenshots/calculatorapp.png?raw=true)
Explore a step-by-step tutorial on how to build a simple calculator app using PynamicUI.

### [Example Counter App](https://github.com/zacharie410/PynamicUI/wiki/Example-Counter-App)
![](https://github.com/zacharie410/PynamicUI/blob/main/examples/screenshots/counterapp.png?raw=true)
See a practical example of creating a counter app to learn more about PynamicUI's state management and hooks.

### [Example Dynamic List](https://github.com/zacharie410/PynamicUI/wiki/Example-Dynamic-List)
![](https://github.com/zacharie410/PynamicUI/blob/main/examples/screenshots/dynamiclistapp.png?raw=true)
Discover how to create a dynamic list using PynamicUI's powerful `place` method for flexible and responsive UI elements.

### [Example NavBar App](https://github.com/zacharie410/PynamicUI/wiki/Example-NavBar-App)
![](https://github.com/zacharie410/PynamicUI/blob/main/examples/screenshots/navbarapp.png?raw=true)
Explore a tutorial on building a navigation bar with buttons to switch between different pages in your application.

## An abstraction of CustomTkinter
PynamicUI supports nearly all the same elements as [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).
![](https://github.com/TomSchimansky/CustomTkinter/blob/master/documentation_images/image_example_dark_Windows.png?raw=true)

## Getting Started

### Using PynamicUI in a New Project

To start using PynamicUI in a new project, follow these steps:

1. Import the required classes and functions from PynamicUI:

```python
from pynamicui import createStylesheet, createDom, createElement, setAppearanceMode
import customtkinter as tk
```

2. Define your UI components using the `createElement` class:

```python
class CounterApp:
    def __init__(self, dom):
        self.dom = dom
        # Create the counter state using dom.useState
        self.dom.useState("counter", 0, self.update_counter_label)

        # Create a label to display the counter value
        self.counter_label = createElement(self.dom, "Label", props={"text": "Counter: 0"}, place={"relwidth": 1, "relheight": 0.5})

        # Create a button to increment the counter
        self.increment_button = createElement(self.dom, "Button", style="PrimaryButton", props={"text": "Increment", "command": self.increment_counter}, place={"relwidth": 1, "relheight": 0.5, "rely": 0.5})

    def increment_counter(self):
        # Get the current counter value
        counter = self.dom.getState("counter")
        # Increment the counter value
        counter += 1
        # Update the counter state
        self.dom.setState("counter", counter)

    def update_counter_label(self, prop, element, value):
        # Update the counter label text prop with the new counter value
        self.counter_label.setProp("text", f"Counter: {value}")
```

3. Add styles using the `createStylesheet` class:

```python
styles = createStylesheet()

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
```

4. Render the virtual DOM and launch your application:

```python
if __name__ == "__main__":
    dom = createDom()
    dom.setStylesheet(styles)
    
    CounterApp(dom)

    dom.render()
```

### Integrating PynamicUI in an Existing Project

To integrate PynamicUI into an existing project, follow these steps:

1. Install PynamicUI and its dependencies as described in the [Installation](#installation) section.

2. Import the required classes and functions from PynamicUI:

```python
from pynamicui import createStylesheet, createDom, createElement, setAppearanceMode
import customtkinter as tk
```

3. Identify the parts of your application where you want to use PynamicUI and create virtual elements accordingly.

4. Add styles using the `createStylesheet` class to customize the appearance of the UI elements.

5. Implement state management and hooks to add interactivity and custom logic to your application.

6. Render the virtual DOM and launch your application:

```python
if __name__ == "__main__":
    dom = createDom(root=existingCustomTkinterRoot)
```

## Contributions

Contributions to PynamicUI are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on [GitHub](https://github.com/zacharie410/PynamicUI).

## Issue Tracking

This wiki page explains the proper procedures for submitting an issue related to PynamicUI
[Issue Tracking with PynamicUI](https://github.com/zacharie410/PynamicUI/wiki/Issue-Tracking)

## License

PynamicUI is licensed under the [Apache License](https://github.com/zacharie410/PynamicUI/blob/main/LICENSE). Feel free to use, modify, and distribute this library as permitted by the license.

## Acknowledgments

PynamicUI is built upon the foundation of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky. Special thanks to the developers of CustomTkinter for their valuable contributions.