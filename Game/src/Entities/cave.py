class Cave:
    #constructor method
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None

    #Getter Methods
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.item

    #Setter Methods
    def set_description(self, cave_description):
        self.description = cave_description

    def set_name(self, cave_description):
        self.description = cave_description

    def set_character(self, character):
        self.character = character
        
    def set_item(self, item):
        self.item = item

    #link cave methods
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    #get details of the cave
    def describe(self):
        print(self.name)
        print("----------")
        print(" " + self.description)

        for direction in self.linked_caves:
            cave = self.linked_caves[direction]

            print(f"The {cave.get_name()} is {direction}")

    #move to a different cave
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        
        else:
            print("You can't go that way")
            return self