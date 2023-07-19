# Sample code demonstrating dynamic list creation
# (Please note that this is a simplified example for demonstration purposes)
from pynamicui import createDom, createElement

dom = createDom()

# Parent container
container = createElement(dom, "Frame", place={"relx": 0, "rely": 0, "relwidth": 1, "relheight": 1})

# Dynamic list items (using a loop to create multiple items)
num_items = 5
for i in range(num_items):
    item = createElement(container, "Button", props={"text": f"Item {i+1}"})
    item.place({"relx":0, "rely":(i / num_items), "relwidth":1, "relheight": (1 / num_items)})

# Render the virtual DOM
dom.render()
