__version__ = "0.0.6"

import customtkinter as tk

from .createDom import createDom
from .createElement import createElement
from .createStylesheet import createStylesheet

def setAppearanceMode(mode):
    tk.set_appearance_mode(mode)

def setDefaultColorTheme(theme):
    tk.set_default_color_theme(theme)

def setWidgetScaling(scale):
    tk.set_widget_scaling(scale)
