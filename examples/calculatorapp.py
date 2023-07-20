from pynamicui import createDom, createElement, createStylesheet
class CalculatorApp:
    def __init__(self, dom):
        self.dom = dom
        self.current_value = ""  # Variable to store the current value entered by the user

        # Create a label to display the current value
        self.display_label = createElement(self.dom, "Label", props={"text": ""}, place={"relwidth": 1, "relheight": 0.2})

        # Create the buttons for numbers and operators
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        for i, text in enumerate(button_texts):
            self.create_button(text, i // 4, i % 4)

    def create_button(self, text, row, column):
        createElement(self.dom, "Button", style="CalculatorButton", props={"text": text, "command": lambda: self.on_button_click(text)}, place={"relwidth": 0.25, "relheight": 0.2, "relx": 0.25 * column, "rely": 0.2 * row + 0.2})

    def on_button_click(self, text):
        if text == "=":
            try:
                # Evaluate the expression and display the result
                result = eval(self.current_value)
                self.display_label.setProp("text", str(result))
            except:
                # Handle any errors in the expression
                self.display_label.setProp("text", "Error")
            finally:
                self.current_value = ""
        else:
            # Update the current value with the button clicked
            self.current_value += text
            self.display_label.setProp("text", self.current_value)
# Create the virtual DOM
dom = createDom()

stylesheet = createStylesheet()

stylesheet.addStyle("CalculatorButton", {"padx" : 0.1, "pady" : 0.05})

dom.root.title("calculatorapp.py")

dom.setStylesheet(stylesheet)

# Set the window size
dom.setGeometry("400x500")

# Render the CalculatorApp component
calculator_app = CalculatorApp(dom)

# Render the virtual DOM
dom.render()
