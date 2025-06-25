class Character():
    describe_options = ["is here!", "appears from the shadows...", "steps out from behind a boulder", "taps you on the shoulder", "appears in a corner"]
    #constructor methods
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    #set character conversation
    def set_conversation(self, conversation):
        self.conversation = conversation

    #describe character
    @classmethod
    def describe(cls, num):
        return cls.describe_options[num]

    #talk to character
    def talk(self):
        if self.conversation is not None:
            return [f"[{self.name} says]: " , f"{self.conversation}"]

        else:
            return (f"{self.name} doesn't want to talk to you")

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
        self.health = 25
        self.attacks = {}
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def get_weakness(self):
        return self.weakness
    
    def get_health(self):
        return self.health
    
    def set_weakness(self, weakness):
        self.weakness = weakness
        
    def set_health(self, health):
        self.health = health
        
    def set_attack(self, attack_name, damage):
        self.attacks.update({attack_name : damage})
        
    def damage(self, damage):
        self.health -= damage

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
        return [f"{self.name} ", "pats you back"]
        
#extends Character class, allows players to trade item with character
class Trader(Friend):
    #constructor method
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.item_trades = None
        self.item_wants = None
        self.trade_limit = None
        
    def get_item_trades(self):
        return self.item_trades
    
    def get_item_wants(self):
        return self.item_wants
    
    def get_trade_limit(self):
        return self.trade_limit
    
    def set_trade_limit(self, trade_limit):
        self.trade_limit = trade_limit
        
    def set_trade(self, item_trades, item_wants):
        self.item_trades = item_trades
        self.item_wants = item_wants