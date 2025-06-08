from config import Player, Game
from os import system, name
from time import sleep
from sys import stdout
class GameCommand():
    def display_decorator(func):
        def wrapper():
            print(Player.current_cave.get_name())
            print("----------")
            func()
        return wrapper
    
    @display_decorator
    @staticmethod
    def display_details():
        Player.current_cave.describe()
        
        if Game.cave_inhabitant is not None:
            Game.cave_inhabitant.describe()
            
        if Game.cave_item is not None:
            Game.cave_item.describe()
            
    @staticmethod
    def sequential_print(string):
        for character in string:
            stdout.write(f"{character}_")
            stdout.write("\b \b")
            stdout.flush()
            sleep(0.2)
    
    
    @staticmethod
    def clear_terminal():
        system('cls' if name == 'nt' else 'clear')
        