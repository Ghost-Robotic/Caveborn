class Item:
    item_list = []
    describe_options = ["You spot a", "Behind a boulder you spot a", "Under some dirt you see a", "Buried by rocks, you catch a glimpse of a", "in the centre of the room sits a"]
    #constructor method
    def __init__(self, name):
        self.name = name
        self.description = None
        self.rarity = None
        self.base_damage = 15
        self.durability = None
        self.item_list.append(self)
        
    #getter methods
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    #setter methods
    def set_name(self, name):
        self.name = name
        
    def set_description(self, description):
        self.description = description
        
    def set_base_damage(self, damage):
        self.damage = damage
        
    def set_durability(self, durability):
        self.durability = durability
        
    def use_item(self):
        """minus one durability from item
        """
        if self.durability is not None:
            self.durability -= 1
        
    def select_damage(self, num):
        match num:
            case 0: #weak attack
                self.use_item()
                return ["weak attack" , self.base_damage - self.base_damage*0.3] # -30%
            
            case 1: #strong attack
                self.use_item()
                return ["strong attack" , self.base_damage]
            
            case 2: #critical hit
                self.use_item()
                return ["critical hit" , self.base_damage + self.base_damage*0.3] # +30%
        
    #describe item
    @classmethod
    def describe(cls, num):
        """Takes a random number to return a describe item option

        Args:
            num (int): random number

        Returns:
            string: ____ a <item-name>
        """
        return cls.describe_options[num]
    
    @classmethod
    def get_item(cls, name):
        """If the name matches an existing Item it will return that Item

        Args:
            name (str): name of the item to be retrieved

        Returns:
            class instance: returns selected item object
        """
        for item in cls.item_list:
            if name == (item.name).lower():
                return item
            
        return None


class HealingItem(Item):
    def __init__(self, name):
        super().__init__(name)
        self.heals_for = None
        
    def set_heals_for(self, heals_for):
        self.heals_for = heals_for
        
    def get_heals_for(self):
        self.use_item()
        return self.heals_for