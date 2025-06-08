from src.entities.character import Enemy, Trader
from config import Config, Player, Game
from commands.game_commands import GameCommand

Config.initialise()

#loops while player is still alive
while Player.dead == False:
    print("\n")
    #GameCommand.clear_terminal()
    
    Game.update_state()
    GameCommand.display_details()

    command = input("> ").lower().strip()
    
    match command:
        case "north" | "south" | "east" | "west":
            #move to new cave
            Player.current_cave = Player.current_cave.move(command)

        #talk with current inhabitant
        case "talk":
            #talk to 
            if Game.cave_inhabitant is not None:
                Game.cave_inhabitant.talk()
        
        #fight current inhabitant
        case "fight":
            #attempt to fight enemy
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

        #pat current inhabitant
        case "pat":
            if Game.cave_inhabitant is not None:
                if isinstance(Game.cave_inhabitant, Enemy):
                    print("I wouldn't do that if I were you...")

                else:
                    Game.cave_inhabitant.pat()

            else:
                print(f"There is no one here to pat :(")
            
        #take current item  
        case "take":
            if Game.cave_item is not None:
                print(f"You put the {Game.cave_item.get_name()} in your bag")
                Player.bag.append(Game.cave_item.get_name())
                Player.current_cave.set_item(None)
            
        #trade with current inhabitant   
        case "trade":
            if Game.cave_inhabitant is not None and isinstance(Game.cave_inhabitant, Trader):
                    print("What do you have to trade")
                    player_trades = input("> ")
                    
                    if player_trades not in Player.bag: 
                        print(f"You don't have a {player_trades}") 
                        continue
                    
                    if player_trades == Game.cave_inhabitant.get_item_wants():
                        print(f"You trade a {player_trades} for a {Game.cave_inhabitant.get_item_trades()}")
                        Player.bag.remove(player_trades)
                        Player.bag.append(Game.cave_inhabitant.get_item_trades())
                        
                    else:
                        print(f"{Game.cave_inhabitant.name} doesn't want a {player_trades}")
            else:
                print("There is no one here to trade with")
