from src.ticket import Ticket
from src.jira_wrapper import JiraWrapper

import json
import webbrowser


CONFIG_LOCATION = "config.json"
DRY_RUN = False


def main():
    ticket = Ticket(default_config=get_default_config())
    ticket.ask_for_title()
    ticket.ask_for_description()
    ticket.ask_for_default_epic()
    jira = JiraWrapper(get_jira_credentials(), dry=DRY_RUN)
    new_issue = jira.create_issue(ticket)
    open_issue_in_browser(new_issue)


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


def open_issue_in_browser(issue):
    if not DRY_RUN:
        open_issue = input("Open in browser? [y/N]: ")
        if open_issue.lower() in ["yes", "y"]:
            webbrowser.open_new_tab(issue.permalink())


if __name__ == "__main__":
    main()
