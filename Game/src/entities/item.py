class Item:
    #constructor method
    def __init__(self, name):
        self.name = name
        self.description = None
        self.rarity = None
        
    #getter methods
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_rarity(self):
        return self.rarity
    
    #setter methods
    def set_name(self, name):
        self.name = name
        
    def set_description(self, description):
        self.description = description
        
    def set_rarity(self, rarity):
        self.rarity = rarity
        
    #describe item
    def describe(self):
        return f"You spot a {self.name}- {self.description}"