from src.entities.character import Enemy, Trader
from src.assets.title import Title
from src.assets.player_info_display import PlayerDisplay
from src.config import Config
from src.entities.player import Player
from src.game import Game
from .commands import Command

class PlayerCommand():
    
    @staticmethod
    def move(direction):
        """
        Move to another cave in given direction.

        Args:
            direction (str): Direction to move in.
        """
        next_cave = Game.current_cave.move(direction)
        if next_cave is None:
            Title.output()
            PlayerDisplay.output()
            print("\nYou walk into a wall \nThere is nothing there!")
            Command.wait_for_enter()
        else:
            Game.current_cave = next_cave     
            Title.output()
            PlayerDisplay.output()
            print("\nMoving", end = "")
            Command.sequential_print("...", 0.1, Config.standard_text_colour)        
    
    
    @Game.display_decorator
    @staticmethod
    def talk():
        """Talk with current cave inhabitant."""   
        #Command.clear_terminal()     
        if Game.cave_inhabitant is not None:
            Command.sequential_print_segments(segments = 2, 
                                                  strings = [Game.cave_inhabitant.talk()[0], Game.cave_inhabitant.talk()[1]], 
                                                  speeds = [0.075, 0.15], 
                                                  colours = [Config.character_text_colour, "\x1b[38;5;208m"])

        else: 
            Command.sequential_print("Its so lonely in here...", Config.standard_print_speed, Config.standard_text_colour)
            
        Command.wait_for_enter()
    
    
    @Game.display_decorator
    @staticmethod
    def fight():
        """Attempt to fight with current cave inhabitant."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Enemy):
            #Fight with the inhabitant if there is one
            print("What will you fight with")
            fight_with = Command.get_input()

            if fight_with in Player.bag:
                if Game.cave_inhabitant.fight(combat_item= fight_with) == True:
                    #win message
                    print("Bravo, hero you won the fight!")
                    Game.current_cave.set_character(None)
                                    
                else:
                    #loss message
                    print("Scurry home, you lost the fight.")
                    Player.damage(100)
                    
            else:
                Command.sequential_print_segments(segments= 2,
                                                      strings= ["You don't have a ", f"{fight_with}"], 
                                                      speeds= [Config.standard_print_speed], 
                                                      colours= [Config.standard_text_colour, Config.item_text_colour])
                Command.wait_for_enter()

        else:
            Command.sequential_print("There is no one here to fight with", Config.standard_print_speed, Config.standard_text_colour)
            Command.wait_for_enter()
    
    
    @Game.display_decorator
    @staticmethod
    def pat():
        """Attempt to pat current cave inhabitant."""
        if Game.cave_inhabitant is not None:
            if isinstance(Game.cave_inhabitant, Enemy):
                Command.sequential_print("I wouldn't do that if I were you...", Config.standard_print_speed, Config.standard_text_colour)

            else:
                Command.sequential_print_segments(segments= 2,
                                                      strings= Game.cave_inhabitant.pat(), 
                                                      speeds= [Config.standard_print_speed], 
                                                      colours= [Config.character_text_colour, Config.standard_text_colour])

        else:
            Command.sequential_print(f"There is no one here to pat :(", Config.standard_print_speed, Config.standard_text_colour)
            
        Command.wait_for_enter()
    
    
    @Game.display_decorator
    @staticmethod
    def take():
        """Take the item in the current cave."""
        if Game.cave_item is not None:
            Command.sequential_print_segments(segments= 3,
                                                  strings= ["You put the ", f"{Game.cave_item.get_name()} ", "in your bag"], 
                                                  speeds= [Config.standard_print_speed], 
                                                  colours= [Config.standard_text_colour, Config.item_text_colour, Config.standard_text_colour])
            Player.bag.append(Game.cave_item.get_name())
            Game.current_cave.set_item(None)
            
            
        else:
            Command.sequential_print("The floor is empty...", Config.standard_print_speed, Config.standard_text_colour)
            
        Command.wait_for_enter()
    
    
    @Game.display_decorator
    @staticmethod
    def trade():
        """Trade with current inhabitant if they are a Trader."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Trader):
                print("What do you have to trade")
                player_trades = Command.get_input()
                
                if player_trades not in Player.bag: 
                    Command.sequential_print_segments(segments= 2, 
                                                          strings= ["You don't have a ", f"{player_trades}"], 
                                                          speeds= [Config.standard_print_speed], 
                                                          colours = [Config.standard_text_colour, Config.item_text_colour]) 
                    Command.wait_for_enter()
                    return

                if player_trades == Game.cave_inhabitant.get_item_wants():
                    Command.sequential_print_segments(segments= 4 , 
                                                          strings = ["You trade a ",f"{player_trades} ","for a ",f"{Game.cave_inhabitant.get_item_trades()}"],
                                                          speeds = [Config.standard_print_speed],
                                                          colours = [Config.standard_text_colour, Config.item_text_colour, Config.standard_text_colour, Config.item_text_colour])
                    Player.bag.remove(player_trades)
                    Player.bag.append(Game.cave_inhabitant.get_item_trades())
                    
                else:
                    Command.sequential_print_segments(segments= 3,
                                                          strings= [f"{Game.cave_inhabitant.name} ", "doesn't want a ", f"{player_trades}"],
                                                          speeds= [Config.standard_print_speed],
                                                          colours= [Config.character_text_colour, Config.standard_text_colour, Config.item_text_colour])
        else:
            Command.sequential_print("There is no one here to trade with", Config.standard_print_speed, Config.standard_text_colour)
            
        Command.wait_for_enter()
        
        
    @Game.display_decorator
    @staticmethod
    def invalid():
        print("Invalid Command")
        Command.wait_for_enter()