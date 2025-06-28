from .config import CaveEntities
from .config import Config
from src.commands.commands import Command
from src.entities.player import Player
from src.entities.character import Enemy
from src.entities.item import Item
from src.assets.title import Title
from src.assets.player_info_display import PlayerDisplay
from src.assets.cave_info_display import CaveDisplay, CombatDisplay


class Game():
    """This class store Game wide variable"""
    current_cave = None
    cave_inhabitant = None
    cave_item = None
    
    run_game = None
    game_mode = None
    
    last_command = None
    
    def display_decorator(func):
        def wrapper(*args): 
            Command.clear_terminal()
            Title.output()
            PlayerDisplay.update_info(Game.current_cave, Player.health, Player.bag) 
            PlayerDisplay.update_display()                    
            PlayerDisplay.output()
            
            print("----------")
            print("\x1b[1;38;5;196m", Game.current_cave.get_name(), "\x1b[0m")
            print("----------")
            func(*args)
        return wrapper          
        
    
    @classmethod
    def set_game_mode(cls, game_mode):
        cls.game_mode = game_mode
    
    @classmethod
    def initialise(cls):
        """Initialise Game objects"""
        cls.run_game = True
        cls.current_cave = CaveEntities.cavern
        cls.last_command = None
        
    @classmethod
    def update_state(cls):
        """
        Updates Game variables.
        """
        cls.cave_inhabitant = cls.current_cave.get_character()
        cls.cave_item = cls.current_cave.get_item()
    
    
    @classmethod
    def display_details(cls):
        Title.output()
        PlayerDisplay.update_info(Game.current_cave, Player.health, Player.bag) 
        PlayerDisplay.update_display()                    
        PlayerDisplay.output()
        
        print("----------")
        print("\x1b[1;38;5;196m", Game.current_cave.get_name(), "\x1b[0m")
        print("----------")
        
        print(cls.current_cave.describe())
        
        
        if cls.cave_inhabitant is not None and cls.cave_item is None:
            CaveDisplay.update_character_info(cls.cave_inhabitant)
            CaveDisplay.update_display()
            CaveDisplay.display_character()
        elif cls.cave_item is not None and cls.cave_inhabitant is None:
            CaveDisplay.update_item_info(cls.cave_item)
            CaveDisplay.update_display()
            CaveDisplay.display_item()
        elif cls.cave_item is not None and cls.cave_inhabitant  is not None:
            CaveDisplay.update_character_info(cls.cave_inhabitant)
            CaveDisplay.update_item_info(cls.cave_item)
            CaveDisplay.update_display()
            CaveDisplay.display()
        
    @classmethod
    def display_fight(cls):
        Command.clear_terminal()
        Title.output()
        PlayerDisplay.update_info(Game.current_cave, Player.health, Player.bag) 
        PlayerDisplay.update_display()                    
        PlayerDisplay.output()
        
        print("----------")
        print("\x1b[1;38;5;196m", Game.current_cave.get_name(), "\x1b[0m")
        print("----------")
        CombatDisplay.update_character_info(cls.cave_inhabitant)
        CombatDisplay.update_display()
        CombatDisplay.display_character()
        
    # @classmethod
    # def display_item_description(cls):
        
    @classmethod
    def print_last_command(cls):
        """
        Prints the last command the user has inputted with a faded look.

        Args:
            last_command (str): Last action the the user has inputted e.g. move.
        """
        if cls.last_command not in [None , ""]:
            print("\n\x1b[38;5;241m>\x1b[38;2;148;150;65m", cls.last_command, "\x1b[0m")
        else:
            print("")  
            
    @classmethod
    def check_win_condition(cls):
        """
        Checks to see if the condition for winning or losing has been met for the chosen game mode

        Raises:
            Exception: no game mode set

        Returns:
            bool: returns false if win/lose condition is met else it returns True
        """
        match cls.game_mode:
            
            case "default":
                if Enemy.enemies_to_defeat == 0:
                    return False
                elif Player.health <= 0:
                    Player.dead = True
                    return False 
                else:
                    return True
                
            case "exit":
                return False
                  
            case _:
                raise Exception("no game mode set")
    
    @classmethod
    def print_game_over(cls):
        #Command.clear_terminal()
        #Title.output()
        match cls.game_mode:
            case "default":
                if Player.dead == True:
                    Command.sequential_print("YOU DIED", 0.1, "\x1b[38;5;196m")
                    Command.pause(0.2)
                    print("")
                    Command.sequential_print("Better Luck Next Time", Config.standard_print_speed, Config.standard_text_colour)
                else:
                    Command.sequential_print("CONGRATULATIONS!", 0.1, "\x1b[38;5;203m")
                    Command.pause(0.2)
                    print("")
                    Command.sequential_print("You defeated all the enemies!", Config.standard_print_speed, Config.standard_text_colour)
                    
            case "exit":
                print("Game closed")
        Command.pause(2)