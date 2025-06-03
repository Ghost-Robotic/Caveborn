from src.entities.cave import Cave
from src.entities.character import Character, Enemy, Friend, Trader
from src.entities.item import Item

class Config():
    """This class initialise all game entities"""
        
    @classmethod
    def initialise(self):
        """Initialise game entities"""
        Cave_Entities.initialise()
        Item_Entities.initialise()
        Character_Entities.initialise()
        
        Links.initialise_cave_relationships() 
        Links.initialise_item_locations()
        Links.initialise_character_locations()
        
        Player.initialise()    


class Cave_Entities(Cave):
    """This class contains all the Cave objects"""
    
    cavern = None
    grotto = None
    dungeon = None
    underground_lake = None
    abandoned_mine = None
    
    @classmethod 
    def initialise(self):
        """Initialise Cave objects"""
        self.cavern = Cave( "Cavern")
        self.cavern.set_description("A damp and dirty cave.")

        self.grotto = Cave("Grotto")
        self.grotto.set_description("A small cave with ancient graffiti")

        self.dungeon = Cave("Dungeon")
        self.dungeon.set_description("A large cave with a rack")

        self.underground_lake = Cave("Underground Lake")
        self.underground_lake.set_description("A massive cave with a mysterious lake in the centre")

        self.abandoned_mine = Cave("Abandoned Mine")
        self.abandoned_mine.set_description("An old mine covered in dust and cobwebs")    
        
        
class Item_Entities(Item):
    """""This class contains all Item objects:"""""
    vegemite = None
    torch = None
    sunken_treasure = None
    pickaxe = None
    
    @classmethod
    def initialise(self):
        """Initialise Item objects"""
        self.vegemite = Item("vegemite")
        self.vegemite.set_description("A Wumpuses worst nightmare")

        self.torch = Item("torch")
        self.torch.set_description("A light for the end of the tunnel")

        self.sunken_treasure = Item("sunken treasure")
        self.sunken_treasure.set_description("A waterlogged chest filled with gold coins")

        self.pickaxe = Item("pickaxe")
        self.pickaxe.set_description("A sturdy iron pickaxe")


class Character_Entities(Character):
    """This class contains all Character objects"""
    
    harry = None 
    """_Enemy_"""
    
    josephine = None
    """_Friend_"""
    
    josh = None
    """Trader"""
    
    @classmethod
    def initialise(self):
        """Initialise Character objects"""
        self.harry = Enemy("Harry", "A smelly Wumpus")
        self.harry.set_conversation("Hangry...Hanggrry")
        self.harry.set_weakness("vegemite")

        self.josephine = Friend("Josephine", "A friendly bat")
        self.josephine.set_conversation("Gidday")        

        self.josh = Trader("Josh", "An undead miner looking for gold")
        self.josh.set_conversation("GOLLLD!")
        self.josh.set_trade(
            item_give= "pickaxe", 
            item_takes = "sunken treasure") 
        
        
class Links(Cave_Entities, Item_Entities, Character_Entities):
    """This class contains the relationship between Cave objects"""
    
    @classmethod
    def initialise_cave_relationships(self):
        """Initialise the links between caves"""
        self.cavern.link_cave(self.dungeon, "south")
        self.dungeon.link_cave(self.cavern, "north")

        self.grotto.link_cave(self.dungeon, "east")
        self.dungeon.link_cave(self.grotto, "west")

        self.underground_lake.link_cave(self.grotto, "east")
        self.grotto.link_cave(self.underground_lake, "west")

        self.abandoned_mine.link_cave(self.dungeon, "west")
        self.dungeon.link_cave(self.abandoned_mine, "east")  
        
    @classmethod
    def initialise_item_locations(self):
        """Initialise location of items in the caves"""
        self.grotto.set_item(self.vegemite)
        self.dungeon.set_item(self.torch)        
        self.underground_lake.set_item(self.sunken_treasure)        
    
    @classmethod
    def initialise_character_locations(self):
        """Initialise location of characters in the caves"""
        self.dungeon.set_character(self.harry) 
        self.grotto.set_character(self.josephine)
        self.abandoned_mine.set_character(self.josh)
          
        
class Player():
    """This class contains all the information about the Player"""
    current_cave = None
    bag = None
    dead = None
    
    @classmethod
    def initialise(self):
        """Initialise Player object"""
        self.current_cave = Cave_Entities.cavern
        self.bag = []
        self.dead = False