from config import Player, Game
from os import system, name
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
            
    @classmethod
    def display(cls):
        pass
    
    @staticmethod
    def clear_terminal():
        system('cls' if name == 'nt' else 'clear')
        