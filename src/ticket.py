class Ticket:

    def __init__(self, default_config={}):
        self.title = ""
        self.description = ""

        self.project = default_config["project"] if "project" in default_config else ""
        self.component = default_config["component"] if "component" in default_config else ""
        self.epic = ""
        self._default_epic = default_config["epic"] if "epic" in default_config else ""

    def __str__(self):
        return f"""
Ticket content:
  Title:       {self.title}
  Description: {self.description}
  Project:     {self.project}
  Component:   {self.component}
  Epic:        {self.epic}"""

    def ask_for_title(self):
        self.title = input("Enter title: ")

    def ask_for_description(self):
        self.description = self.multiline_input("Enter description (\".\" to finish): ")

    def ask_for_default_epic(self):
        include_epic = input(f"Include default epic ({self._default_epic})? [Y/n]: ")
        if include_epic.lower() not in ["no", "n"]:
            self.epic = self._default_epic

    @classmethod
    def multiline_input(cls, text):
        lines = []
        line = input(text)
        while line != ".":
            lines.append(line)
            line = input()
        return '\n'.join(lines)
