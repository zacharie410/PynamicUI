from pynamicui import createDom, createElement

dom = createDom()

# Parent container with margin
container_with_margin = createElement(dom, "Frame", place={"relx": 0, "rely": 0, "relwidth": 1, "relheight": 1})

# Child element inside the parent container
element_inside_container_with_margin = createElement(container_with_margin, "Button", place={"relx": 0.1, "rely": 0.1, "relwidth": 0.8, "relheight": 0.8}, props={"text": "Button"})

# Render the virtual DOM
dom.render()
