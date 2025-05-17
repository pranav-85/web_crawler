from rich.console import Console
from rich.table import Table

console = Console()

def print_progress(url: str, title: str):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Crawled URL", style="dim")
    table.add_column("Page Title")
    table.add_row(url, title)
    console.print(table)