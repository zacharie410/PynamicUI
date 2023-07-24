class createPageViewer:
    def __init__(self, dom, pageWidth, pageLength, container, previousPageButton, nextPageButton, createItem):
        self.dom = dom
        self.pageLength = pageLength
        self.pageWidth = pageWidth
        self.currentPage = 0
        self.items = []

        # Container and buttons are passed as parameters
        self.container = container
        self.previousPageButton = previousPageButton
        self.nextPageButton = nextPageButton
        # Assign createItem method
        self.createItem = createItem

        # Add the onClick commands to the buttons
        self.previousPageButton.setProp("command", self.previousPage)
        self.nextPageButton.setProp("command", self.nextPage)

        # Set the initial grid
        self.container.setGrid(self.pageWidth, self.pageLength, [str(index) for index in range(self.pageLength)])

        #track items
        self.uniqueId = 0

    def addItem(self, item):
        item.uniqueId = self.uniqueId
        self.uniqueId += 1
        self.items.append(item)
        self.renderItems()

    def removeItem(self, item):
        for index, item1 in enumerate(self.items):
            if item1.uniqueId == item.uniqueId:
                if item1.element:
                    item1.element.destroy()
                self.items.pop(index)

        self.renderItems()

    def getItem(self, index):
        try:
            return self.items[index]
        except IndexError:
            print(f"No item at index {index}")
            return None

    def nextPage(self):
        if (self.currentPage + 1) * self.pageLength < len(self.items):
            self.currentPage += 1
            self.renderItems()

    def previousPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.renderItems()

    def renderItems(self):
        start_index = self.currentPage * self.pageLength
        end_index = start_index + self.pageLength
        grid_index = 0

        for index, item in enumerate(self.items):
            if index >= start_index and index < end_index:
                if not item.element:
                    itemRow = self.createItem(item, self.container, grid_index)
                    item.setElement(itemRow)
                else:
                    item.element.setId(str(grid_index))
                grid_index += 1
            elif item.element:
                item.element.destroy()
                item.element = None

        self.previousPageButton.setProp("state", "normal" if self.currentPage > 0 else "disabled")
        self.nextPageButton.setProp("state", "normal" if end_index < len(self.items) else "disabled")

        self.container.render()