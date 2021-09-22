from jira import JIRA


class JiraWrapper:

    def __init__(self, credentials, dry=False):
        self.jira_client = JIRA(basic_auth=(credentials["username"],
                                            credentials["password"]),
                                options={"server": credentials["server"]})
        self.dry = dry

    def create_issue(self, ticket, add_epic=False):
        issue_dict = {
            'project': {'key': ticket.project},
            'summary': ticket.title,
            'description': ticket.description,
            'components': [{"name" : ticket.component}],
            'issuetype': {'name': 'Task'},
        }

        if self.dry:
            return issue_dict

        new_issue = self.jira_client.create_issue(fields=issue_dict)
        if add_epic:
            self.jira_client.add_issues_to_epic(ticket.epic, [new_issue.key])

        return new_issue
