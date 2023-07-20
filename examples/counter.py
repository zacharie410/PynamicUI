from pynamicui import createDom, createElement

class CounterApp:
    def __init__(self, dom):
        self.dom = dom
        # Create the counter state using dom.useState
        self.dom.useState("counter", 0, self.update_counter_label)

        # Create a label to display the counter value
        self.counter_label = createElement(self.dom, "Label", props={"text": "Counter: 0"}, place={"relwidth": 1, "relheight": 0.5}, spacing={"padx" : 0.1, "pady": 0.1})

        # Create a button to increment the counter
        self.increment_button = createElement(self.dom, "Button", props={"text": "Increment", "command": self.increment_counter}, spacing={"padx" : 0.1, "pady": 0.1}, place={"relwidth": 1, "relheight": 0.5, "rely": 0.5})

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

# Create the virtual DOM
dom = createDom()

dom.root.title("counter.py")

# Render the CounterApp component
counter_app = CounterApp(dom)

# Render the virtual DOM
dom.render()