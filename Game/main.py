from cave import Cave
from character import Character
from character import Enemy, Friend

#create Cave instances
cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave.")

grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")

dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")

#Cave links
cavern.link_cave(dungeon, "south")
dungeon.link_cave(cavern, "north")

grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")

#characters
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

#main game loop
current_cave = cavern
dead = False

while dead == False:
    print("\n")
    current_cave.get_details()

    inhabitant = current_cave.get_character()

    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    
    #check and excecute command  given
    if command.lower() in ["north", "south", "east", "west"]:
        #move to new cave
        current_cave = current_cave.move(command)

    elif command == "talk":
        #talk to 
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "fight":
        #attempt to fight enemy
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            #Fight with the inhabitant if there is one
            print("What will you fight with")
            fight_with = input("> ")

            if inhabitant.fight(combat_item= fight_with):
                #win message
                print("Bravo, hero you won the fight!")
                current_cave.set_character(None)

            else:
                #loss message
                print("Scurry home, you lost the fight.")
                print("That's the end of the game")
                dead = True

        else:
            print("There is no one here to fight with")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")

            else:
                inhabitant.pat()

        else:
            print(f"There is no one here to pat :(")

