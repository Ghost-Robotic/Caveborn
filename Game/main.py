from src.entities.character import Enemy, Trader
from config import Config, Player

Config.initialise()

#loops while player is still alive
while Player.dead == False:
    print("\n")
    Player.current_cave.get_details()
    
    #get and store cave entities
    inhabitant = Player.current_cave.get_character()
    item = Player.current_cave.get_item()

    #describe entities within cave
    if inhabitant is not None:
        inhabitant.describe()
        
    if item is not None:
        item.describe()

    command = input("> ").lower()
    
    #check and execute command  given
    if command in ["north", "south", "east", "west"]:
        #move to new cave
        Player.current_cave = Player.current_cave.move(command)

    #talk with current inhabitant
    elif command == "talk":
        #talk to 
        if inhabitant is not None:
            inhabitant.talk()
    
    #fight current inhabitant
    elif command == "fight":
        #attempt to fight enemy
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            #Fight with the inhabitant if there is one
            print("What will you fight with")
            fight_with = input("> ")

            if fight_with in Player.bag:
                if inhabitant.fight(combat_item= fight_with) == True:
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
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")

            else:
                inhabitant.pat()

        else:
            print(f"There is no one here to pat :(")
          
    #take current item  
    elif command == "take":
        if item is not None:
            print(f"You put the {item.get_name()} in your bag")
            Player.bag.append(item.get_name())
            Player.current_cave.set_item(None)
         
    #trade with current inhabitant   
    elif command == "trade":
        if inhabitant is not None and isinstance(inhabitant, Trader):
                print("What do you have to trade")
                player_gives = input("> ")
                
                if player_gives not in Player.bag: 
                    print(f"You don't have a {player_gives}") 
                    continue
                
                if player_gives == inhabitant.get_item_takes():
                    print(f"You trade a {player_gives} for a {inhabitant.get_item_give()}")
                    Player.bag.remove(player_gives)
                    Player.bag.append(inhabitant.get_item_give())
                    
                else:
                    print(f"{inhabitant.name} doesn't want a {player_gives}")
        else:
            print("There is no one here to trade with")