from typing import List

from rich.console import Console
from rich.table import Table


def show_issues(console: Console, rows: List):
    table = Table(show_header=True, header_style="bold green")
    table.add_column("KEY", style="dim", width=8)
    table.add_column("SUMMARY")

    for row in rows:
        issue_key = row[0]
        issue_summary = row[1]
        table.add_row("[green]" + issue_key, issue_summary)
    console.print(table)
