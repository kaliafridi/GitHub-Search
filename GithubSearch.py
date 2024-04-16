import requests
from colorama import Fore, Style
from time import sleep

tool_name = "GitHub Repositories Search Tool"
made_by = "Made By Rayyan Afridi"
version = "Version 1.0"

dragon = r"""
               _____                                                                   _____ 
( ___ )-----------------------------------------------------------------( ___ )
 |   |                                                                   |   | 
 |   |                                                                   |   | 
 |   |                                                                   |   | 
 |   |  ____                           _                                 |   | 
 |   | / ___|   ___   __ _  _ __  ___ | |__                              |   | 
 |   | \___ \  / _ \ / _` || '__|/ __|| '_ \                             |   | 
 |   |  ___) ||  __/| (_| || |  | (__ | | | |                            |   | 
 |   | |____/  \___| \__,_||_|   \___||_| |_|                            |   | 
 |   |  ____                           _  _                _             |   | 
 |   | |  _ \  ___  _ __    ___   ___ (_)| |_  ___   _ __ (_)  ___  ___  |   | 
 |   | | |_) |/ _ \| '_ \  / _ \ / __|| || __|/ _ \ | '__|| | / _ \/ __| |   | 
 |   | |  _ <|  __/| |_) || (_) |\__ \| || |_| (_) || |   | ||  __/\__ \ |   | 
 |   | |_| \_\\___|| .__/  \___/ |___/|_| \__|\___/ |_|   |_| \___||___/ |   | 
 |   |             |_|                                                   |   | 
 |   |                                                                   |   | 
 |   |                                                                   |   | 
 |___|                                                                   |___| 
(_____)-----------------------------------------------------------------(_____)
"""

def search_github_repositories(keyword):
    url = f"https://api.github.com/search/repositories?q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        urls = [item['html_url'] for item in data['items']]
        return urls
    else:
        return None

def display_animation():
    for _ in range(3):
        print(Fore.YELLOW + "Searching.")
        sleep(0.5)
        print(Fore.YELLOW + "Searching..")
        sleep(0.5)
        print(Fore.YELLOW + "Searching...")
        sleep(0.5)

def main():
    print(Fore.GREEN + "╭────────────────────────────────────────────────────╮")
    print(Fore.GREEN + f"│            {Fore.YELLOW}{tool_name}{Fore.GREEN}            │")
    print(Fore.GREEN + f"│            {Fore.YELLOW}{made_by}{Fore.GREEN}            │")
    print(Fore.GREEN + f"│            {Fore.YELLOW}{version}{Fore.GREEN}            │")
    print(Fore.GREEN + "╰────────────────────────────────────────────────────╯\n")

    while True:
        user_input = input(Fore.BLUE + "Enter 'search' to search for GitHub repositories or 'exit' to quit: ").lower()

        if user_input == 'search':
            keyword = input(Fore.GREEN + "Enter a keyword to search for in GitHub repositories: ")
            display_animation()
            urls = search_github_repositories(keyword)

            if urls:
                print(Fore.GREEN + "\nMatching GitHub Repository URLs:")
                for url in urls:
                    print(Fore.BLUE + url)
            else:
                print(Fore.RED + "\nNo matching repositories found.")
        elif user_input == 'exit':
            print(Fore.YELLOW + "Exiting the tool. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")

if __name__ == "__main__":
    print(Fore.RED + dragon)
    main()
