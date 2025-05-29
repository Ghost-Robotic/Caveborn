from cave import Cave
from character import Character
from character import Enemy

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

harry = Enemy(char_name= "Harry", 
              char_description= "A smelly Wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")

dungeon.set_character(harry)

current_cave = cavern

while True:
    print("\n")
    current_cave.get_details()

    inhabitant = current_cave.get_character()

    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ")

    current_cave = current_cave.move(command)