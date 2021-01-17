from typing import List

from jira import JIRA, Issue

from jiral.config import Config


def login_jira(config: Config) -> JIRA:
    options = {"server": config.server}
    return JIRA(options, basic_auth=(config.user, config.token))


def search_issues(jira: JIRA, project: str, limit: int = 50) -> List[Issue]:
    return jira.search_issues(
        f"project={project} and assignee = currentUser() and status not in (resolved, closed, Done)",
        maxResults=limit,
    )
