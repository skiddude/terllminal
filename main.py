"""
Ok so this app will have 2 modes:
1- TUI mode
2- CLI mode
the first one is the user friendly one and the other one is the "nerdy" only
the default option is tui.
"""
from rich import print
from rich.console import Console
from beaupy import select, prompt

console = Console()

tui_options = [
    "Start",
    "Settings",
    "Help",
    "About",
    "Quit",
]

about_project = """
terllminal is a project to bring LLMs from their slow, unresponsive web "apps" to the terminal!
"""
def tui():
	console.print("Hello welcome to [bold]terllminal[/bold]!")
	console.print("Please choose an option:")
	option = select(tui_options)
    if option == "About":
        console.print(about_project)

def options():
    if option == "Start":
        print("hi")
    elif option == "Settings":
        print("hit")

tui()
