from pynamicui import createDom, createElement
from PIL import Image
import customtkinter

class ImageApp:
    def __init__(self, dom):
        self.dom = dom

        # Create the CTkImage element
        self.image_button = createElement(
            self.dom,
            "Button",
            props={"image": customtkinter.CTkImage(light_image=Image.open("screenshots/counterapp.png"))},
            place={"relwidth": 0.5, "relheight": 0.5, "relx": 0.25, "rely": 0.25}
        )

dom = createDom()

# Render the ImageApp component
image_app = ImageApp(dom)

# Render the virtual DOM
dom.render()
