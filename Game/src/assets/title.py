from time import sleep
from os import system, name

class Title():
    """Used to display game title"""
    title = [
        "╔───────────────────────────────────────────────╗",
        "│    ___                _                       │",
        "│   / __\__ ___   _____| |__   ___  _ __ _ __   │",
        "│  / /  / _` \ \ / / _ \ '_ \ / _ \| '__| '_ \  │",
        "│ / /__| (_| |\ V /  __/ |_) | (_) | |  | | | | │",
        "│ \____/\__,_| \_/ \___|_.__/ \___/|_|  |_| |_| │",
        "│                                               │",
        "╚───────────────────────────────────────────────╝"
    ]
    
    
    @classmethod 
    def output(cls):
        for line in cls.title:
            print(line)    
            
    @classmethod
    def cascade_output(cls):
        sleep(0.3)
        colour_id = 232
        time = 0.09
        for i in range(24):
            system('cls' if name == 'nt' else 'clear')
            for line in cls.title:
                print(f"\x1b[38;5;{colour_id}m" + line)
            sleep(time)
            time += 0.0051
            colour_id += 1
            