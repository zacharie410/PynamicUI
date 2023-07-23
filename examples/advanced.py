from pynamicui import createDom, createElement, createStylesheet

class CalculatorApp:
    def __init__(self, dom):
        self.dom = dom
        self.currentValue = ""

        self.displayContainer = createElement(self.dom, "Frame", style="Container", place={"relwidth": 1, "relheight": 0.2})
        self.buttonsContainer = createElement(self.dom, "Frame", style="Container", place={"relwidth": 1, "relheight": 0.8, "rely": 0.2})

        self.buttonsContainer.setGrid(4, 5, [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", ".",
            "0", "-", "+", "=",
            "^", "(", ")", "=",
        ])

        self.displayLabel = createElement(self.displayContainer, "Label", style="Display", props={"text": ""}, place={"relwidth": 1, "relheight": 1})

        for gridId in self.buttonsContainer.grid.keys():
            self.createButton(gridId)

    def createButton(self, gridId):
        styleName = "CalculatorButton"
        if gridId.isnumeric():
            styleName = "CalculatorNumber"
        elif gridId == "=":
            styleName = "EvaluateButton"

        createElement(self.buttonsContainer, "Button", style=styleName, props={"text": gridId, "command": lambda t=gridId: self.onButtonClick(t)}, id=gridId)

    def onButtonClick(self, text):
        if text == "=":
            try:
                result = eval(self.currentValue)
                self.displayLabel.setProp("text", str(result))
            except:
                self.displayLabel.setProp("text", "Error")
            finally:
                self.currentValue = ""
        else:
            self.currentValue += text
            self.displayLabel.setProp("text", self.currentValue)


if __name__ == "__main__":
    # Create the virtual DOM
    dom = createDom()

    # Create the stylesheet
    stylesheet = createStylesheet()
    stylesheet.addStyle("Container", {"padx": 0.05, "pady": 0.05})
    stylesheet.addStyle("Display", {"padx": 0.2, "pady": 0.2, "font": ("Helvetica", 42)})
    stylesheet.addStyle("CalculatorButton", {"padx": 0.1, "pady": 0.15, "font": ("Helvetica", 42, "bold"), "fg_color": "#2E4053"})
    stylesheet.addNestedStyle("CalculatorButton", "CalculatorNumber", {"fg_color": "#34495E"})
    stylesheet.addNestedStyle("CalculatorButton", "EvaluateButton", {"fg_color": "#1A5276"})

    # Set the stylesheet to the virtual DOM
    dom.setStylesheet(stylesheet)

    # Set the window title and size
    dom.root.title("Calculator App")
    dom.setGeometry("400x500")

    # Create the CalculatorApp with the custom grid
    calculator_app = CalculatorApp(dom)

    # Render the virtual DOM
    dom.render()
