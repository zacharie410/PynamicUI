from pynamicui import createDom, createElement

class CounterApp:
    def __init__(self, dom):
        self.dom = dom

        self.container = createElement(self.dom, "Frame", place={"relwidth" : 0.9, "relheight": 1})
        self.scrollFrame = createElement(self.container, "Frame", place={"relwidth" : 1, "relheight": 2})
        self.label = createElement(self.scrollFrame, "Label", place={"relwidth" : 0.5, "relheight": 0.5})

        self.slider = createElement(self.dom, "Slider",
                                     spacing={"padx":0.25},
                                     place={"relwidth" : 0.1, "relheight" : 1, "relx" : 0.9},
                                     spawnProps={"from_" : 0, "to" : 100, "orientation": "vertical", "progress_color": "transparent"},
                                     props={"command" : lambda num: self.scrollFrame.place({"relwidth":1, "relheight":2, "rely":-1+num/100 })})

        self.slider.useEffect([""], hook = lambda prop, element, value: (
                              self.slider.widget.set(100),

                              ))
                              

    def increment_counter(self):
        # Get the current counter value
        counter = self.getCount()
        # Increment the counter value
        counter += 1
        # Update the counter state
        self.setCount(counter)

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