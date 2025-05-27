class Character():
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