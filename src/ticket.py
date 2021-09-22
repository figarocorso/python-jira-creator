class Ticket:

    def __init__(self):
        title = ""
        description = ""

    def __str__(self):
        return f"""
Ticket content:
  Title: {self.title}
  Description: {self.description}"""

    def ask_for_title(self):
        self.title = input("Enter title: ")

    def ask_for_description(self):
        self.description = input("Enter description: ")
