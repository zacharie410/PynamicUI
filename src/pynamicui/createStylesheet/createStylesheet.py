class createStylesheet:
    def __init__(self):
        self.stylesheet = {}

    def addStyle(self, styleName, style):
        self.stylesheet[styleName] = style

    def addNestedStyle(self, inheritsFrom, name, updateArgs):
        if inheritsFrom not in self.stylesheet:
            raise ValueError(f"The style '{inheritsFrom}' does not exist in the stylesheet.")
        
        newStyle = self.stylesheet[inheritsFrom].copy()
        newStyle.update(updateArgs)
        self.stylesheet[name] = newStyle