from pjc import get_jira_credentials
from src.jira_wrapper import JiraWrapper

from sys import argv
import webbrowser



def main():
    issue_key = argv[1] if len(argv) > 1 else input("Enter issue key: ").strip()
    if not issue_key:
        return

    jira = JiraWrapper(get_jira_credentials(), dry=False)
    issue = jira.get_issue(issue_key)
    webbrowser.open_new_tab(issue.permalink())


if __name__ == "__main__":
    main()
