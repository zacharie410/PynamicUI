from pynamicui import createDom, createElement

def button_click_handler(event):
    print("Button clicked!")

dom = createDom()

# Create a button element with a click event handler
button = createElement(dom, "Button", props={"text": "Click Me"}, place={"relwidth": 1, "relheight": 1})

def bind_click_event(prop, element, success):
    print("Mounted")
    # Bind the click event handler to the button widget
    button.widget.bind("<Button-1>", button_click_handler)

def unbind_click_event(prop, element, success):
    print("Unmounted")
    # Unbind the click event handler from the button widget
    button.widget.unbind("<Button-1>", button_click_handler)

# Bind the click event when the button mounts
button.useEffect(props=[""], hook=bind_click_event, unmount=unbind_click_event)

# Render the virtual DOM
dom.render()
