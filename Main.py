import os, configparser, colorama, inquirer
from pyuac import main_requires_admin
from src.Lyre import Lyre

def read_config() -> dict:
    config = configparser.ConfigParser()
    config.read("config.ini")

    return {
        "build_path": config.get("build", "PATH"),
        "start_key": config.get("input", "START_KEY"),
        "end_key": config.get("input", "END_KEY"),
        "close_key": config.get("input", "CLOSE_KEY")
    }

def process(song: str, option: str) -> None:
    song = song.replace(colorama.Fore.LIGHTCYAN_EX, "")
    if song is None: song = "Default"

    lyre = Lyre(
        config=read_config(),
        song_path="songs/" + song
    )

    if option.startswith(colorama.Fore.LIGHTCYAN_EX + "Build"):
        lyre.build_macro()

    elif option.startswith(colorama.Fore.LIGHTCYAN_EX + "Run"):
        lyre.execute_lyre()

@main_requires_admin
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
    
    print(colorama.Fore.MAGENTA + "* " + colorama.Fore.LIGHTMAGENTA_EX + "Lyre is a tool developed by Hazu to interpret and build macros for the Windsong Lyre from Genshin Impact.\n")
    
    option = inquirer.list_input(message=colorama.Fore.LIGHTMAGENTA_EX + "Choose an option" + colorama.Fore.MAGENTA, choices=[colorama.Fore.LIGHTCYAN_EX + "Build ahk file", colorama.Fore.LIGHTCYAN_EX + "Run with Lyre"], default="Build .ahk file")

    files = [colorama.Fore.LIGHTCYAN_EX + f for f in os.listdir("songs") if f.split(".")[1] == "wsl"]

    if len(files) < 1: print(colorama.Fore.RED + "* " + colorama.Fore.LIGHTRED_EX + "There is no file in the songs path.")
    
    song = inquirer.list_input(message=colorama.Fore.LIGHTMAGENTA_EX + "Choose a song" + colorama.Fore.MAGENTA, choices=files, default=files[0])
    process(song, option)

    if input(colorama.Fore.GREEN + "\n- " + colorama.Fore.LIGHTGREEN_EX + "Continue? (Y/N): " + colorama.Fore.GREEN).lower() == "y": init()

def main() -> None: init()

if __name__ == "__main__":
    main()