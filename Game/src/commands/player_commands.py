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
    
    @staticmethod
    def talk():
        """Talk with current cave inhabitant."""   
        GameCommand.clear_terminal()     
        if Game.cave_inhabitant is not None:
            GameCommand.sequential_print(Game.cave_inhabitant.talk(), 0.1)

        else: 
            print("Its so lonely in here...")
            
        GameCommand.wait_for_enter()
    
    @staticmethod
    def fight():
        """Attempt to fight with current cave inhabitant."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Enemy):
            #Fight with the inhabitant if there is one
            print("What will you fight with")
            fight_with = input("> ")

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
                print(f"You don't have a {fight_with}")

        else:
            print("There is no one here to fight with")
    
    @staticmethod
    def pat():
        """Attempt to pat current cave inhabitant."""
        if Game.cave_inhabitant is not None:
            if isinstance(Game.cave_inhabitant, Enemy):
                print("I wouldn't do that if I were you...")

            else:
                Game.cave_inhabitant.pat()

        else:
            print(f"There is no one here to pat :(")
    
    @staticmethod
    def take():
        """Take the item in the current cave."""
        if Game.cave_item is not None:
            print(f"You put the {Game.cave_item.get_name()} in your bag")
            PlayerEntity.bag.append(Game.cave_item.get_name())
            Game.current_cave.set_item(None)
            
        else:
            print("The floor is empty...")
    
    @staticmethod
    def trade():
        """Trade with current inhabitant if they are a Trader."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Trader):
                print("What do you have to trade")
                PlayerEntity_trades = input("> ")
                
                if PlayerEntity_trades not in PlayerEntity.bag: 
                    print(f"You don't have a {PlayerEntity_trades}") 
                    return
                
                if PlayerEntity_trades == Game.cave_inhabitant.get_item_wants():
                    print(f"You trade a {PlayerEntity_trades} for a {Game.cave_inhabitant.get_item_trades()}")
                    PlayerEntity.bag.remove(PlayerEntity_trades)
                    PlayerEntity.bag.append(Game.cave_inhabitant.get_item_trades())
                    
                else:
                    print(f"{Game.cave_inhabitant.name} doesn't want a {PlayerEntity_trades}")
        else:
            print("There is no one here to trade with")