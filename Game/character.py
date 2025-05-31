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
    
#extends Character class
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def get_weakness(self):
        return self.weakness
    
    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
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