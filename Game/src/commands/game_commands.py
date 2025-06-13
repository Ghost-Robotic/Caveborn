from src.config import Game, PlayerEntity
from src.assets.bit_maps import Bitmap
from os import system, name
from time import sleep
from sys import stdout

class GameCommand():
    def display_decorator(func):
        def wrapper(): 
            Bitmap.update_info(Game.current_cave, PlayerEntity.health, PlayerEntity.bag) 
            Bitmap.update_map()                    
            Bitmap.display_bitmap()
            
            print("----------")
            print("\x1b[1;38;5;196m", Game.current_cave.get_name(), "\x1b[0m")
            print("----------")
            func()
        return wrapper
    
    
    @display_decorator
    @staticmethod
    def display_details():
        print(Game.current_cave.describe())
        
        if Game.cave_inhabitant is not None:
            print(Game.cave_inhabitant.describe())
            
        if Game.cave_item is not None:
            print(Game.cave_item.describe())
            
            
    @staticmethod
    def sequential_print(string, speed, colour):
        for character in string:
            stdout.write(f"{colour}{character}\x1b[0m_")
            stdout.write("\b \b")
            stdout.flush()
            sleep(speed)
        sleep(0.1)
          
            
    @staticmethod
    def sequential_print_segments(segments, strings, speeds, colours):
        try:
            if len(range(segments)) != len(speeds):
                for i in range(segments):
                    for character in strings[i]:
                        stdout.write(f"{colours[i]}{character}\x1b[0m_")
                        stdout.write("\b \b")
                        stdout.flush()
                        sleep(speeds[0])
            else:
                for i in range(segments):
                    for character in strings[i]:
                        stdout.write(f"{colours[i]}{character}\x1b[0m_")
                        stdout.write("\b \b")
                        stdout.flush()
                        sleep(speeds[i])
        except:
            raise Exception("Number of segments does not match strings, speeds or colours given")
        
        sleep(0.1)               
    
    
    @staticmethod
    def clear_terminal():
        system('cls' if name == 'nt' else 'clear')
        
        
    @staticmethod
    def update_state():
        """Updates Game class variables"""
        Game.cave_inhabitant = Game.current_cave.get_character()
        Game.cave_item = Game.current_cave.get_item()
        
        PlayerEntity.health = (PlayerEntity.health if PlayerEntity.health <= 100 else 100)
        
        if PlayerEntity.health <= 0:
            PlayerEntity.dead = True
           
            
    @staticmethod
    def wait_for_enter():
        print("\n")
        GameCommand.sequential_print("Press ", 0.06, "")
        GameCommand.sequential_print("Enter ", 0.06, "\x1b[38;5;226m")
        GameCommand.sequential_print("to Continue", 0.06, "")
        input("\n\033[?25l")
        print('\033[?25h', end="")
        
        
    @staticmethod
    def get_input():
        command = input(">\x1b[38;5;226m ").lower().strip()
        print('\x1b[0m', end="")
        return command
    
    
    @staticmethod
    def print_last_command(last_command):
        if last_command is not None:
            print("\n\x1b[38;5;241m>\x1b[38;2;148;150;65m", last_command, "\x1b[0m")
        else:
            print("")        