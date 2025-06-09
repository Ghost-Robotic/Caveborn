from config import Game
from src.entities.Player import Player
from os import system, name
from time import sleep
from sys import stdout
class GameCommand():
    def display_decorator(func):
        def wrapper():
            print(f"| Health: {Player.health} |")
            print("‾" * 15)
            print(Game.current_cave.get_name())
            print("----------")
            func()
        return wrapper
    
    @display_decorator
    @staticmethod
    def display_details():
        Game.current_cave.describe()
        
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
        
        
    @staticmethod
    def update_state():
        """Updates Game class variables"""
        Game.cave_inhabitant = Game.current_cave.get_character()
        Game.cave_item = Game.current_cave.get_item()
        
        Player.health = (Player.health if Player.health <= 100 else 100)
        
        if Player.health <= 0:
            Player.dead = True