from typing import List

import ujson
from jira import JIRA, Issue
from jira.resilientsession import raise_on_error

from jiral.config import Config
from jiral.entity.issue_staus import IssueStatus
from jiral.entity.issue_type import IssueType


def login_jira(config: Config) -> JIRA:
    options = {"server": config.server}
    return JIRA(options, basic_auth=(config.user, config.token))


def search_jira_issues(jira: JIRA, project: str, limit: int = 50) -> List[Issue]:
    return jira.search_issues(
        f"project={project} and assignee = currentUser() and status not in (resolved, closed, Done)",
        maxResults=limit,
    )


def create_jira_issue(
    jira: JIRA, project: str, summary: str, description: str, issue_type: IssueType
) -> Issue:
    return jira.create_issue(
        project=project, summary=summary, description=description, issuetype={"name": issue_type.value}
    )


def update_jira_issue(jira: JIRA, issue_id: str, issue_status: IssueStatus) -> Issue:
    issue = jira.issue(issue_id)
    transitions = jira.transitions(issue)
    for transition in transitions:
        transition_name = transition["name"].upper().replace(" ", "")
        if transition_name == issue_status.value:
            jira.transition_issue(issue, transition["id"])
            return issue


def assign_issue(jira: JIRA, issue: Issue, account_id: str):
    # pre-port
    # ref.https://github.com/pycontribs/jira/blob/master/jira/client.py#L1572
    url = jira._options["server"] + "/rest/api/latest/issue/" + str(issue.key) + "/assignee"
    payload = {"accountId": account_id}
    r = jira._session.put(url, data=ujson.dumps(payload))
    raise_on_error(r)
