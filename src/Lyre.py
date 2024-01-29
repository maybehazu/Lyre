import colorama

class Lyre:
    def __init__(self, config: dict, song_path: str="songs/Default.txt") -> None:
        self.path = song_path
        self.config = config
        self.segments = []
        self.info = []

        clefs = {
            "((ti))": "a",
            "((la))": "a",
            "((so))": "a",
            "((fa))": "a",
            "((mi))": "a",
            "((re))": "a",
            "((do))": "a",
            "(ti)": "a",
            "(la)": "a",
            "(so)": "a",
            "(fa)": "a",
            "(mi)": "a",
            "(re)": "a",
            "(do)": "a",
            "ti": "a",
            "la": "a",
            "so": "a",
            "fa": "a",
            "mi": "a",
            "re": "a",
            "do": "a",
        }

        try: 
            with open(self.path, "r") as file:
                content = file.read().split("#Song")
                info = content[0][6:-1]

                self.title = info.split("Title: ")[1].split("Interval:")[0].strip().replace(" ", "_")
                self.interval = float(info.split("Interval: ")[1])
                self.type = int(info.split("Type: ")[1].split("Title:")[0])

                if self.type == 2:
                    for key, value in clefs.items():
                        content[1] = content[1].replace(key, value)
                
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