from src.ticket import Ticket
from src.jira_wrapper import JiraWrapper

import json


CONFIG_LOCATION = "config.json"


def main():
    ticket = Ticket(default_config=get_default_config())
    ticket.ask_for_title()
    ticket.ask_for_description()
    jira = JiraWrapper(get_jira_credentials(), dry=True)
    new_issue = jira.create_issue(ticket, add_epic=False)
    print(new_issue)


def get_default_config():
    default_config = {}
    with open(CONFIG_LOCATION) as f:
        default_config = json.load(f)
    return default_config.get("defaults", {})


def get_jira_credentials():
    credentials = {}
    with open(CONFIG_LOCATION) as f:
        default_config = json.load(f)
    return default_config.get("credentials", {})


if __name__ == "__main__":
    main()
