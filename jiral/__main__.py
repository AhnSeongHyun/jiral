import webbrowser

import typer
from rich.console import Console

from jiral.config import Config, load_config, save_config
from jiral.display import show_issues
from jiral.entity.issue_staus import IssueStatus
from jiral.entity.issue_type import IssueType
from jiral.exc import ConfigSaveError, JiraLoginError
from jiral.service import assign_issue, create_jira_issue, login_jira, search_jira_issues, update_jira_issue

app = typer.Typer()
create_app = typer.Typer()
update_app = typer.Typer()
app.add_typer(create_app, name="create", help="Create a new Jira issue")
app.add_typer(update_app, name="update", help="Update an existing Jira issue")


@update_app.command("issue")
def update_issue(
    issue_id: str = typer.Option(..., help="issue id eg. JIRA-123", case_sensitive=False),
    issue_status: IssueStatus = typer.Option(
        ..., help="update status : TODO, IN_PROGRESS, IN_REVIEW, DONE", case_sensitive=False
    ),
):
    """
    Update jira issue
    """
    is_task_completed = False
    console = Console()
    with console.status("[bold green]Working on tasks..."):
        while not is_task_completed:
            config = load_config()
            jira = login_jira(config)
            updated_issue = update_jira_issue(jira=jira, issue_id=issue_id, issue_status=issue_status)
            is_task_completed = True
    typer.echo(typer.style(f"[{updated_issue.key}] updated!! 🌮", fg=typer.colors.GREEN, bold=True))


@create_app.command("issue")
def create_issue(
    project: str = typer.Option(..., help="project key", case_sensitive=False),
    summary: str = typer.Option(..., help="issue summary"),
    desc: str = typer.Option(default="", help="issue desc"),
    issue_type: IssueType = typer.Option(default=IssueType.TASK, help="issue type", case_sensitive=False),
):
    """
    Create jira issue and Assign to me
    """
    is_task_completed = False
    console = Console()
    with console.status("[bold green]Working on tasks..."):
        while not is_task_completed:
            config = load_config()
            jira = login_jira(config)
            new_issue = create_jira_issue(
                jira=jira,
                project=project,
                summary=summary,
                description=desc,
                issue_type=issue_type,
            )
            assign_issue(jira=jira, issue=new_issue, account_id=jira.myself()["accountId"])
            is_task_completed = True
    typer.echo(typer.style(f"[{new_issue.key}] created!! 🌮", fg=typer.colors.GREEN, bold=True))


@app.command()
def issue(
    project: str = typer.Option(..., help="project key", case_sensitive=False),
    limit: int = typer.Option(help="limit", default=10),
):
    """
    Retrieve jira issue
    """
    is_task_completed = False
    console = Console()
    with console.status("[bold green]Working on tasks..."):
        while not is_task_completed:
            config = load_config()
            jira = login_jira(config)
            issues = search_jira_issues(jira=jira, project=project, limit=limit)
            is_task_completed = True

            show_issues(console=console, rows=[(issue.key, issue.fields.summary) for issue in issues])


@app.command()
def config(
    server: str = typer.Option(..., prompt=True),
    user: str = typer.Option(..., prompt=True),
    token: str = typer.Option(..., prompt=True),
):
    """
    Config jira Authentication
    """
    try:
        config = Config(server=server, user=user, token=token)
        login_jira(config)
    except Exception:
        raise JiraLoginError

    try:
        save_config(config)
        typer.echo(typer.style("saved!! 🌮", fg=typer.colors.GREEN, bold=True))
    except (FileNotFoundError, ValueError, TypeError):
        raise ConfigSaveError


@app.command()
def open():
    config = load_config()
    url = config.server
    webbrowser.open_new_tab(url)


if __name__ == "__main__":
    app()
