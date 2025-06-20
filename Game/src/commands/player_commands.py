from src.entities.character import Enemy, Trader
from src.config import Game, PlayerEntity
from .game_commands import GameCommand

class PlayerCommand():
    
    @staticmethod
    def move(direction):
        """
        Move to another cave in given direction.

        Args:
            direction (str): Direction to move in.
        """
        Game.current_cave = Game.current_cave.move(direction)
    
    
    @GameCommand.display_decorator
    @staticmethod
    def talk():
        """Talk with current cave inhabitant."""   
        #GameCommand.clear_terminal()     
        if Game.cave_inhabitant is not None:
            GameCommand.sequential_print_segments(segments = 2, 
                                                  strings = [Game.cave_inhabitant.talk()[0], Game.cave_inhabitant.talk()[1]], 
                                                  speeds = [0.075, 0.15], 
                                                  colours = [Game.character_text_colour, "\x1b[38;5;208m"])

        else: 
            GameCommand.sequential_print("Its so lonely in here...", Game.standard_print_speed, Game.standard_text_colour)
            
        GameCommand.wait_for_enter()
    
    
    @GameCommand.display_decorator
    @staticmethod
    def fight():
        """Attempt to fight with current cave inhabitant."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Enemy):
            #Fight with the inhabitant if there is one
            print("What will you fight with")
            fight_with = GameCommand.get_input()

            if fight_with in PlayerEntity.bag:
                if Game.cave_inhabitant.fight(combat_item= fight_with) == True:
                    #win message
                    print("Bravo, hero you won the fight!")
                    Game.current_cave.set_character(None)
                    
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")  
                        PlayerEntity.dead = True                  

                else:
                    #loss message
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    PlayerEntity.dead = True
                    
            else:
                GameCommand.sequential_print_segments(segments= 2,
                                                      strings= ["You don't have a ", f"{fight_with}"], 
                                                      speeds= [Game.standard_print_speed], 
                                                      colours= [Game.standard_text_colour, Game.item_text_colour])
                GameCommand.wait_for_enter()

        else:
            GameCommand.sequential_print("There is no one here to fight with", Game.standard_print_speed, Game.standard_text_colour)
            GameCommand.wait_for_enter()
    
    
    @GameCommand.display_decorator
    @staticmethod
    def pat():
        """Attempt to pat current cave inhabitant."""
        if Game.cave_inhabitant is not None:
            if isinstance(Game.cave_inhabitant, Enemy):
                GameCommand.sequential_print("I wouldn't do that if I were you...", Game.standard_print_speed, Game.standard_text_colour)

            else:
                GameCommand.sequential_print_segments(segments= 2,
                                                      strings= Game.cave_inhabitant.pat(), 
                                                      speeds= [Game.standard_print_speed], 
                                                      colours= [Game.character_text_colour, Game.standard_text_colour])

        else:
            GameCommand.sequential_print(f"There is no one here to pat :(", Game.standard_print_speed, Game.standard_text_colour)
            
        GameCommand.wait_for_enter()
    
    
    @GameCommand.display_decorator
    @staticmethod
    def take():
        """Take the item in the current cave."""
        if Game.cave_item is not None:
            GameCommand.sequential_print_segments(segments= 3,
                                                  strings= ["You put the ", f"{Game.cave_item.get_name()} ", "in your bag"], 
                                                  speeds= [Game.standard_print_speed], 
                                                  colours= [Game.standard_text_colour, Game.item_text_colour, Game.standard_text_colour])
            PlayerEntity.bag.append(Game.cave_item.get_name())
            Game.current_cave.set_item(None)
            
        else:
            GameCommand.sequential_print("The floor is empty...", Game.standard_print_speed, Game.standard_text_colour)
            
        GameCommand.wait_for_enter()
    
    
    @GameCommand.display_decorator
    @staticmethod
    def trade():
        """Trade with current inhabitant if they are a Trader."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Trader):
                print("What do you have to trade")
                PlayerEntity_trades = GameCommand.get_input()
                
                if PlayerEntity_trades not in PlayerEntity.bag: 
                    GameCommand.sequential_print_segments(segments= 2, 
                                                          strings= ["You don't have a ", f"{PlayerEntity_trades}"], 
                                                          speeds= [Game.standard_print_speed], 
                                                          colours = [Game.standard_text_colour, Game.item_text_colour]) 
                    GameCommand.wait_for_enter()
                    return

                if PlayerEntity_trades == Game.cave_inhabitant.get_item_wants():
                    GameCommand.sequential_print_segments(segments= 4 , 
                                                          strings = ["You trade a ",f"{PlayerEntity_trades} ","for a ",f"{Game.cave_inhabitant.get_item_trades()}"],
                                                          speeds = [Game.standard_print_speed],
                                                          colours = [Game.standard_text_colour, Game.item_text_colour, Game.standard_text_colour, Game.item_text_colour])
                    PlayerEntity.bag.remove(PlayerEntity_trades)
                    PlayerEntity.bag.append(Game.cave_inhabitant.get_item_trades())
                    
                else:
                    GameCommand.sequential_print_segments(segments= 3,
                                                          strings= [f"{Game.cave_inhabitant.name} ", "doesn't want a ", f"{PlayerEntity_trades}"],
                                                          speeds= [Game.standard_print_speed],
                                                          colours= [Game.character_text_colour, Game.standard_text_colour, Game.item_text_colour])
        else:
            GameCommand.sequential_print("There is no one here to trade with", Game.standard_print_speed, Game.standard_text_colour)
            
        GameCommand.wait_for_enter()
        
        
    @GameCommand.display_decorator
    @staticmethod
    def invalid():
        print("Invalid Command")
        GameCommand.wait_for_enter()