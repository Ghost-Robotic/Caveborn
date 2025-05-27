class Cave:
    #constructor method
    def __init__(self, name):
        self.name = name
        self.description = None

    #Getter Methods
    def get_description(self):
        return self.description

    #Setter Methods
    def set_description(self, cave_description):
        self.description = cave_description

