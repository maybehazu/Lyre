import colorama, keyboard, time, threading, os

def transform_clefs(sheet: str) -> None:
    clefs = {
        "((ti))": "u",
        "((la))": "y",
        "((so))": "t",
        "((fa))": "r",
        "((mi))": "e",
        "((re))": "w",
        "((do))": "q",
        "(ti)": "j",
        "(la)": "h",
        "(so)": "g",
        "(fa)": "f",
        "(mi)": "d",
        "(re)": "s",
        "(do)": "a",
        "ti": "m",
        "la": "n",
        "so": "b",
        "fa": "v",
        "mi": "c",
        "re": "x",
        "do": "z",
    }

    for key, value in clefs.items():
        sheet = sheet.replace(key, value)
    
    return sheet

class Lyre:
    def __init__(self, config: dict, song_path: str="songs/Default.txt") -> None:
        self.path = song_path
        self.config = config
        self.segments = []
        self.info = []

        try: 
            with open(self.path, "r") as file:
                content = file.read().split("#Song")
                info = content[0][6:-1]

                self.title = info.split("Title: ")[1].split("Interval:")[0].strip().replace(" ", "_")
                self.interval = float(info.split("Interval: ")[1])
                self.type = int(info.split("Type: ")[1].split("Title:")[0])

                if self.type == 2: content[1] = transform_clefs(content[1])
                
                segments = content[1].replace(" ", "").split("\n")
            
            for segment in segments:
                if len(segment) < 1 or segment.startswith("."): continue;
                count = [0, 0]

                for index, key in enumerate(segment):
                    if key == ".":
                        if count[0] == 0: count[0] = index
                        count[1] += 1
                
                if count[0] == 0: self.segments.append("{}:0".format(segment)); continue
                
                self.segments.append("{}:{}".format(segment[0:count[0]], count[1] * self.interval))

        except Exception as err:
            print(colorama.Fore.RED + "- " + colorama.Fore.LIGHTRED_EX + "There was an error trying to process the song: {}".format(err) + colorama.Fore.RESET)
    
    def build_macro(self) -> None:
        try:
            print(colorama.Fore.YELLOW + "* " + colorama.Fore.LIGHTYELLOW_EX + "Building song in path \"{}\"".format(self.path) + colorama.Fore.RESET)
            instructions = []

            for segment in self.segments:
                [keybind, duration] = segment.split(":")

                instruction = ""

                for key in keybind:
                    instruction += "    Send, {}\n".format(key)

                if float(duration) > 0: instruction += "    Sleep, {}\n".format(duration)

                instructions.append(instruction)
            
            instructions = "".join(instructions)

            with open("templates/Macro.ahk", "r") as file: template = file.read()

            template = template.replace("[key1]", self.config["start_key"])
            template = template.replace("[key2]", self.config["end_key"])
            template = template.replace("[song]", instructions)

            build_path = self.config["build_path"] + self.title + ".ahk"

            with open(build_path, "w+") as file:
                file.write(template)
            
            print(colorama.Fore.CYAN + "+ " + colorama.Fore.LIGHTCYAN_EX + "The macro has been built correctly in the path \"{}\"".format(build_path) + colorama.Fore.RESET)
        
        except Exception as err:
            print(colorama.Fore.RED + "- " + colorama.Fore.LIGHTRED_EX + "There was an error trying to process the song: {}".format(err) + colorama.Fore.RESET)
    
    def execute_lyre(self) -> None:
        try:
            os.system("cls")

            print(colorama.Fore.CYAN + "+ " + colorama.Fore.LIGHTCYAN_EX + "Running Lyre...\n" + colorama.Fore.YELLOW + "* " + colorama.Fore.LIGHTYELLOW_EX + "{}: start".format(self.config["start_key"]) + colorama.Fore.YELLOW + "\n* " + colorama.Fore.LIGHTYELLOW_EX + "{}: stop\n".format(self.config["end_key"]) + colorama.Fore.YELLOW + "* " + colorama.Fore.LIGHTYELLOW_EX + "{}: close".format(self.config["close_key"]))

            isRunning = True
            canPlay = False

            instructions = []

            for segment in self.segments:
                [keybind, duration] = segment.split(":")

                for key in keybind:
                    instructions.append("press:" + key)
                
                instructions.append("wait:" + str(duration))

            def process_instructions() -> None:
                nonlocal canPlay

                for instruction in instructions:
                    if not canPlay: break

                    if instruction.startswith("press"):
                        thread = threading.Thread(target=lambda x: keyboard.send(x), args=(instruction.split(":")[1].lower(),))
                        thread.start()
                        #keyboard.send(instruction.split(":")[1].lower())
                    
                    elif instruction.startswith("wait"):
                        wait_time = float(instruction.split(":")[1]) / 1050
                        time.sleep(wait_time)

            def on_key_event(e) -> None:
                nonlocal isRunning
                nonlocal canPlay

                if e.event_type == keyboard.KEY_UP:
                    if e.name == self.config["start_key"].lower():
                        canPlay = True

                        action_thread = threading.Thread(target=process_instructions)
                        action_thread.start()

                    elif e.name == self.config["end_key"].lower(): canPlay = False
                    elif e.name == self.config["close_key"].lower(): isRunning = False; canPlay = False

            keyboard.hook(on_key_event)

            while isRunning:
                pass

        except Exception as err:
            print(colorama.Fore.RED + "- " + colorama.Fore.LIGHTRED_EX + "There was an error trying to process the song: {}".format(err) + colorama.Fore.RESET)
        
        finally:
            keyboard.unhook_all()