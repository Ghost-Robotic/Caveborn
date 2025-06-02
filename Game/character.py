class Character():
    #constructor methods
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    #set character conversation
    def set_conversation(self, conversation):
        self.conversation = conversation

    #describe character
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    #talk to character
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")

        else:
            print(f"{self.name} doesn't want to talk to you")

    #fight character
    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True
    
#extends Character class, allows players to fight character
class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def get_weakness(self):
        return self.weakness
    
    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True

        else:
            print(f"{self.name} swallows you, little wimp")
            return False
        
    def steal(self):
        print(f"You steal from {self.name}")

#extends Character class
class Friend(Character):
    #constructor method
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def pat(self):
        print(f"{self.name} pats you back")
        
#extends Character class, allows players to trade item with character
class Trader(Character):
    #constructor method
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.item_give = None
        self.item_takes = None
        
    def get_item_give(self):
        return self.item_give
    
    def get_item_takes(self):
        return self.item_takes
        
    def set_trade(self, item_give, item_takes):
        self.item_give = item_give
        self.item_takes = item_takes