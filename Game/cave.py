class Cave:
    #constructor method
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = {}

    #Getter Methods
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    #Setter Methods
    def set_description(self, cave_description):
        self.description = cave_description

    def set_name(self, cave_description):
        self.description = cave_description

    def describe(self):
        print(self.description)

    #link cave methods
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link