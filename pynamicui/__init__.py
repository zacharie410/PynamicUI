__version__ = "0.1.0"

import customtkinter as tk
from PIL import Image

from .createDom import createDom
from .createElement import createElement
from .createStylesheet import createStylesheet
from .createPageViewer import createPageViewer

def setAppearanceMode(mode):
    tk.set_appearance_mode(mode)

def setDefaultColorTheme(theme):
    tk.set_default_color_theme(theme)

def createImage(imagePath):
    """
    Create an image that is static between dark and light mode
    """
    return tk.CTkImage(light_image=Image.open(imagePath))

def createImageTheme(lightImagePath, darkImagePath):
    """
    Create an image that has a light mode and dark mode image
    """
    return tk.CTkImage(light_image=Image.open(lightImagePath), dark_image=Image.open(darkImagePath))