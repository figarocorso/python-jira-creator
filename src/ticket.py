class Ticket:

    def __init__(self, default_config={}):
        self.title = ""
        self.description = ""
        self.component = default_config["component"] if "component" in default_config else ""
        self.epic = default_config["epic"] if "epic" in default_config else ""

    def __str__(self):
        return f"""
Ticket content:
  Title:       {self.title}
  Description: {self.description}
  Component:   {self.component}
  Epic:        {self.epic}"""

    def ask_for_title(self):
        self.title = input("Enter title: ")

    def ask_for_description(self):
        self.description = input("Enter description: ")
