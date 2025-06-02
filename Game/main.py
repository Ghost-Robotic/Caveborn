from cave import Cave
from character import Enemy, Friend, Trader
from item import Item

#create Cave instances
cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave.")

grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")

dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")

underground_lake = Cave("Underground Lake")
underground_lake.set_description("A massive cave with a mysterious lake in the centre")

abandoned_mine = Cave("Abandoned Mine")
abandoned_mine.set_description("An old mine covered in dust and cobwebs")

#Cave links
cavern.link_cave(dungeon, "south")
dungeon.link_cave(cavern, "north")

grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")

underground_lake.link_cave(grotto, "east")
grotto.link_cave(underground_lake, "west")

abandoned_mine.link_cave(dungeon, "west")
dungeon.link_cave(abandoned_mine, "east")

#item instances
vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")
grotto.set_item(vegemite)

torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)

sunken_treasure = Item("sunken treasure")
sunken_treasure.set_description("A waterlogged chest filled with gold coins")
underground_lake.set_item(sunken_treasure)

pickaxe = Item("pickaxe")
pickaxe.set_description("A sturdy iron pickaxe")

#characters instances
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

josh = Trader("Josh", "An undead miner looking for gold")
josh.set_conversation("GOLLLD!")
josh.set_trade(
    item_give= "pickaxe", 
    item_takes = "sunken treasure"
    )
abandoned_mine.set_character(josh)

#main game loop
current_cave = cavern
dead = False
bag = []

#loops while player is still alive
while dead == False:
    print("\n")
    current_cave.get_details()
    
    #get and store cave entities
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()

    #describe entities within cave
    if inhabitant is not None:
        inhabitant.describe()
        
    if item is not None:
        item.describe()

    command = input("> ")
    
    #check and execute command  given
    if command.lower() in ["north", "south", "east", "west"]:
        #move to new cave
        current_cave = current_cave.move(command)

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

            if fight_with in bag:
                if inhabitant.fight(combat_item= fight_with) == True:
                    #win message
                    print("Bravo, hero you won the fight!")
                    current_cave.set_character(None)
                    
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")  
                        dead = True                  

                else:
                    #loss message
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
                    
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
            bag.append(item.get_name())
            current_cave.set_item(None)
         
    #trade with current inhabitant   
    elif command == "trade":
        if inhabitant is not None and isinstance(inhabitant, Trader):
                print("What do you have to trade")
                player_gives = input("> ")
                
                if player_gives not in bag: 
                    print(f"You don't have a {player_gives}") 
                    continue
                
                if player_gives == inhabitant.get_item_takes():
                    print(f"You trade a {player_gives} for a {inhabitant.get_item_give()}")
                    bag.remove(player_gives)
                    bag.append(inhabitant.get_item_give())
                    
                else:
                    print(f"{inhabitant.name} doesn't want a {player_gives}")
        else:
            print("There is no one here to trade with")
            
            
    