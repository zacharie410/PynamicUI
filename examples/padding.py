from pynamicui import createDom, createElement

dom = createDom()

# Parent container with padding
container_with_padding = createElement(dom, "Frame", place={"relx": 0.1, "rely": 0.1, "relwidth": 0.8, "relheight": 0.8})

# Child container with padding (nested inside the parent container)
child_container_with_padding = createElement(container_with_padding, "Frame", place={"relx": 0.1, "rely": 0.1, "relwidth": 0.8, "relheight": 0.8})

# Child element inside the nested container
element_inside_child_container = createElement(child_container_with_padding, "Button", props={"text": "Button"})

# Render the virtual DOM
dom.render()
