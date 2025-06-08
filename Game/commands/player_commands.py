from src.entities.character import Enemy, Trader
from config import Player, Game

class PlayerCommand():
    
    @staticmethod
    def move(direction):
        """
        Move to another cave in given direction.

        Args:
            direction (str): Direction to move in.
        """
        Player.current_cave = Player.current_cave.move(direction)
    
    @staticmethod
    def talk():
        """Talk with current cave inhabitant."""        
        if Game.cave_inhabitant is not None:
            Game.cave_inhabitant.talk()
        
        else: 
            print("Its so lonely in here...")
    
    @staticmethod
    def fight():
        """Attempt to fight with current cave inhabitant."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Enemy):
            #Fight with the inhabitant if there is one
            print("What will you fight with")
            fight_with = input("> ")

            if fight_with in Player.bag:
                if Game.cave_inhabitant.fight(combat_item= fight_with) == True:
                    #win message
                    print("Bravo, hero you won the fight!")
                    Player.current_cave.set_character(None)
                    
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")  
                        Player.dead = True                  

                else:
                    #loss message
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    Player.dead = True
                    
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
            Player.bag.append(Game.cave_item.get_name())
            Player.current_cave.set_item(None)
            
        else:
            print("The floor is empty...")
    
    @staticmethod
    def trade():
        """Trade with current inhabitant if they are a Trader."""
        if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Trader):
                print("What do you have to trade")
                player_trades = input("> ")
                
                if player_trades not in Player.bag: 
                    print(f"You don't have a {player_trades}") 
                    return
                
                if player_trades == Game.cave_inhabitant.get_item_wants():
                    print(f"You trade a {player_trades} for a {Game.cave_inhabitant.get_item_trades()}")
                    Player.bag.remove(player_trades)
                    Player.bag.append(Game.cave_inhabitant.get_item_trades())
                    
                else:
                    print(f"{Game.cave_inhabitant.name} doesn't want a {player_trades}")
        else:
            print("There is no one here to trade with")