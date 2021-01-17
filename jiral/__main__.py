import typer
from rich.console import Console

from jiral.config import Config, load_config, save_config
from jiral.display import show_issues
from jiral.exc import ConfigSaveError, JiraLoginError
from jiral.service import login_jira, search_issues

app = typer.Typer()


@app.command()
def issue(
    project: str = typer.Option(..., help="project key"),
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
            issues = search_issues(jira=jira, project=project, limit=limit)
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
        typer.echo(typer.style("saved!!", fg=typer.colors.GREEN, bold=True))
    except (FileNotFoundError, ValueError, TypeError):
        raise ConfigSaveError


if __name__ == "__main__":
    app()
