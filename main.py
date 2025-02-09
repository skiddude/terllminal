"""
Ok so this app will have 2 modes:
1- TUI mode
2- CLI mode
the first one is the user friendly one and the other one is the "nerdy" only
the default option is tui.
"""
import os
import time
from rich import print
from rich.console import Console
from beaupy import select, prompt
from openai import OpenAI
import env

console = Console()


tui_options = [
    "Start",
    "Settings",
    "Help",
    "About",
    "Quit",
]

providers = [
    "OpenAI",
    "Google Gemini",
    "Anthropic Claude",
    "Mistral",
    "Cohere",
    "Back",
]

models = {
    "OpenAI": ["GPT-4", "GPT-3.5", "GPT-4 Turbo", "Back"],
    "Google Gemini": ["Gemini 1", "Gemini Pro", "Back"],
    "Anthropic Claude": ["Claude 2", "Claude 3", "Back"],
    "Mistral": ["Mistral-7B", "Mixtral", "Back"],
    "Cohere": ["Command-R", "Command-R+", "Back"]
}


API_KEYS = {
    "OpenAI": env.openai_api_key,
    "Google Gemini": env.gemini_api_key,
    "Anthropic Claude": env.anthropic_api_key,
    "Mistral": env.mistral_api_key,
    "Cohere": env.cohere_api_key,
    "xAI (Grok)": env.xai_api_key
}


back_option = [
    "Back",
]

about_project = """
terllminal is a project to bring LLMs from their slow, unresponsive web "apps" to the terminal!
project website: https://skiddude.github.io/terllminal
github repo: https://github.com/skiddude/terllminal

made in saudi arabia with love :D
"""

def query_provider(provider, model, prompt):
    """Send a request to the selected provider's API."""
    api_key = API_KEYS.get(provider)
    if not api_key:
        console.print(f"[red]Error: No API key found for {provider}![/red]")
        return

    if provider == "OpenAI":
        client = OpenAI(api_key=api_key)
        response = client.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]

    elif provider == "Google Gemini":
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text

    elif provider == "Anthropic Claude":
        client = anthropic.Anthropic(api_key=api_key)
        response = client.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    
    elif provider == "Mistral":
        url = "https://api.mistral.ai/v1/completions"
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {"model": model, "prompt": prompt, "max_tokens": 100}
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("choices", [{}])[0].get("text", "No response")
    
    elif provider == "Cohere":
        url = "https://api.cohere.ai/v1/generate"
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {"model": model, "prompt": prompt, "max_tokens": 100}
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("generations", [{}])[0].get("text", "No response")
    
    elif provider == "xAI (Grok)":
        url = "https://api.x.ai/grok/completions"
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {"model": model, "prompt": prompt, "max_tokens": 100}
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("output", "No response")

    return "Unsupported provider."



def clear():
    """Clear the terminal screen."""
    os.system("cls||clear")


def tui():
    """Display the main TUI menu and get the user's selection."""
    clear()
    console.print("Hello, welcome to [bold green]terLLMinal[/bold green]!")
    console.print("Please choose an option:")
    return select(tui_options)



def about_screen():
    """Display the about screen and return to the main menu."""
    clear()
    console.print(about_project)
    back = select(back_option)
    if back == "Back":
        return True  # Return to the main menu



def start_menu():
    """Start menu - choose provider and model."""
    while True:
        clear()
        console.print("[bold cyan]Choose an AI Provider:[/bold cyan]")
        provider = select(providers)

        if provider == "Back":
            return  # Go back to main menu

        if provider in models:
            while True:
                clear()
                console.print(f"[bold yellow]Choose a model from {provider}:[/bold yellow]")
                model = select(models[provider])

                if model == "Back":
                    break  # Go back to provider selection
                
                console.print(f"[green]You selected {model} from {provider}![/green]")
                input("\nPress Enter to continue...")
                return  # Return to main menu after selection



def main():
    """Main loop to keep the app interactive."""
    while True:
        option = tui()

        if option == "Start":
            start_menu()
        elif option == "Settings":
            console.print("Settings screen coming soon!")
            # Add functionality for 'Settings' here
        elif option == "Help":
            console.print("Help screen coming soon!")
            # Add functionality for 'Help' here
        elif option == "About":
            if not about_screen():  # Go back to the menu if "Back" is selected
                continue
        elif option == "Quit":
            console.print("[bold red]Goodbye![/bold red]")
            break  # Exit the loop and end the program

        # Pause to allow user to read the screen before continuing
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
