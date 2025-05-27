from cave import Cave

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


current_cave = cavern

while True:
    print("\n")
    current_cave.get_details()
    
    command = input(">")

    current_cave = current_cave.move(command)