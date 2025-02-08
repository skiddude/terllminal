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
    "About",
    "Quit",
]

def tui():
	console.print("Hello welcome to terllminal!")
	console.print("Please choose an option:")
	select(tui_options)
tui()