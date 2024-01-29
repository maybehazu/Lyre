import os, configparser, colorama
from src.Lyre import Lyre

def read_config() -> dict:
    config = configparser.ConfigParser()
    config.read("config.ini")

    return {
        "build_path": config.get("build", "PATH"),
        "start_key": config.get("input", "START_KEY"),
        "end_key": config.get("input", "END_KEY")
    }

def process(path: str="Default") -> None:
    if path is None: path = "Default"

    song_path = "songs/" + path + ".txt"
    print(colorama.Fore.YELLOW + "* " + colorama.Fore.LIGHTYELLOW_EX + "Building song in path \"{}\"".format(song_path) + colorama.Fore.RESET)

    lyre = Lyre(
        config=read_config(),
        song_path=song_path
    )

    lyre.build_macro()

def init() -> None:
    os.system("cls")

    print(colorama.Fore.LIGHTMAGENTA_EX + """
 _     ___  _  ____   _____
/ \    \  \// /  __\ /  __/
| |     \  /  |  \/| |  \  
| |_/\  / /   |    / |  /_ 
\____/ /_/    \_/\_\ \____/
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        
          """ + colorama.Fore.RESET)
    
    song = input(colorama.Fore.MAGENTA + "> " + colorama.Fore.LIGHTMAGENTA_EX +  "Song: " + colorama.Fore.MAGENTA)
    process(path=song if len(song) > 0 else None)

    if input(colorama.Fore.CYAN + "\n- " + colorama.Fore.LIGHTCYAN_EX + "Continue? (Y/N): " + colorama.Fore.CYAN).lower() == "y": init()

def main() -> None: init()

if __name__ == "__main__":
    main()