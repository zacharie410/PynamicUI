from pynamicui import createDom, createElement, createStylesheet, createPageViewer

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.element = None

    def setElement(self, element):
        self.element = element

class ContactManagerApp:
    def __init__(self, dom):
        self.dom = dom

        self.container = createElement(self.dom, "Frame", style="Container", place={"relwidth": 1, "relheight": 0.2})
        self.container.setGrid(5, 1, [
            "NameEntry", "PhoneEntry", "EmailEntry", "AddButton", "Empty"
        ])

        self.nameEntry = createElement(self.container, "Entry", style="Entry", id="NameEntry")
        self.phoneEntry = createElement(self.container, "Entry", style="Entry", id="PhoneEntry")
        self.emailEntry = createElement(self.container, "Entry", style="Entry", id="EmailEntry")
        self.addButton = createElement(self.container, "Button", props={"text": "Add Contact", "command": self.addContact}, style="Button", id="AddButton")

        # Create the contacts container
        self.contactsContainer = createElement(self.dom, "Frame", style="Container", place={"relwidth": 1, "relheight": 0.8, "rely": 0.2})

        # Create the page navigation buttons
        self.previousPageButton = createElement(self.dom, "Button", props={"text": "< Previous Page", "state" : "disabled"}, style="Button", place={"relwidth": 0.2, "relheight": 0.2, "rely" : 0.8 , "relx": 0})
        self.nextPageButton = createElement(self.dom, "Button", props={"text": "Next Page >", "state" : "disabled"}, style="Button", place={"relwidth": 0.2, "relheight": 0.2, "rely" : 0.8 , "relx": 0.2})

        # Initialize the PageViewer with the created container and buttons
        self.pageViewer = createPageViewer(self.dom, pageWidth=1, pageLength=10,
                                      container=self.contactsContainer,
                                        previousPageButton=self.previousPageButton,
                                          nextPageButton=self.nextPageButton,
                                          createItem=lambda item, container, id: self.createContactRow(container, id, item))

    def createContactRow(self, container, id, contact):
        contactRow = createElement(container, "Frame", style="ContactRow", id=str(id))
        contactRow.setGrid(4, 1, [
            "NameLabel", "PhoneLabel", "EmailLabel", "DeleteButton"
        ])

        createElement(contactRow, "Label", props={"text": contact.name}, style="ContactLabel", id="NameLabel")
        createElement(contactRow, "Label", props={"text": contact.phone}, style="ContactLabel", id="PhoneLabel")
        createElement(contactRow, "Label", props={"text": contact.email}, style="ContactLabel", id="EmailLabel")
        createElement(contactRow, "Button", props={"text": "Delete", "command": lambda c=contact: self.pageViewer.removeItem(c)}, style="DeleteButton", id="DeleteButton")

        return contactRow

    def addContact(self):
        contact = Contact(self.nameEntry.widget.get(), self.phoneEntry.widget.get(), self.emailEntry.widget.get())
        self.pageViewer.addItem(contact)

    def deleteContact(self, contact):
        self.pageViewer.removeItem(contact)

if __name__ == "__main__":
    dom = createDom()
    stylesheet = createStylesheet()
    stylesheet.addStyle("Container", {"padx": 0.05, "pady": 0.05})
    stylesheet.addStyle("Entry", {"padx": 0.05, "pady": 0.05})
    stylesheet.addStyle("Button", {"padx": 0.05, "pady": 0.05})
    stylesheet.addStyle("ContactRow", {"padx": 0.05, "pady": 0.05})
    stylesheet.addStyle("ContactLabel", {"padx": 0.05, "pady": 0.05})
    stylesheet.addStyle("DeleteButton", {"padx": 0.05, "pady": 0.05})
    dom.setStylesheet(stylesheet)
    dom.root.title("Contact Manager")
    dom.setGeometry("600x800")

    app = ContactManagerApp(dom)

    dom.render()
