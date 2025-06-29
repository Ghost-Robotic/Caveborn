from src.entities.cave import Cave
from src.entities.character import Character, Enemy, Friend, Trader
from src.entities.item import HealingItem, Item
from src.entities.player import Player

class Config():
    """This class initialise all game entities"""
    
    standard_text_colour = None
    standard_print_speed = None
    
    item_text_colour = None
    character_text_colour = None
    health_text_colour = None
        
    @classmethod
    def initialise(cls):
        """Initialise game entities"""
        cls.standard_text_colour = ""
        cls.standard_print_speed = 0.06
        cls.item_text_colour = "\x1b[38;5;207m"
        cls.character_text_colour = "\x1b[38;5;81m"
        cls.health_text_colour = "\x1b[1;38;5;201m"

class CaveEntities(Cave):
    """This class contains all the Cave objects"""
    
    cavern = None
    grotto = None
    dungeon = None
    underground_lake = None
    abandoned_mine = None
    
    @classmethod 
    def initialise(cls):
        """Initialise Cave objects"""
        cls.cavern = Cave("Cavern")
        cls.cavern.set_description("A damp and dirty cave.")

        cls.grotto = Cave("Grotto")
        cls.grotto.set_description("A small cave with ancient graffiti")

        cls.dungeon = Cave("Dungeon")
        cls.dungeon.set_description("A large cave with a rack")

        cls.underground_lake = Cave("Underground Lake")
        cls.underground_lake.set_description("A massive cave with a mysterious lake in the centre")

        cls.abandoned_mine = Cave("Abandoned Mine")
        cls.abandoned_mine.set_description("An old mine covered in dust and cobwebs")    
        
        
class ItemEntities(Item):
    """""This class contains all Item objects:"""""
    vegemite = None
    torch = None
    sunken_treasure = None
    pickaxe = None
    
    @classmethod
    def initialise(cls):
        """Initialise Item objects"""
        cls.vegemite = HealingItem("vegemite")
        cls.vegemite.set_description("A Wumpuses worst nightmare")
        cls.vegemite.set_heals_for(50)

        cls.torch = Item("torch")
        cls.torch.set_description("A light for the end of the tunnel")
        cls.torch.set_base_damage(22)

        cls.sunken_treasure = Item("sunken treasure")
        cls.sunken_treasure.set_description("A waterlogged chest filled with gold coins")

        cls.pickaxe = Item("pickaxe")
        cls.pickaxe.set_description("A sturdy iron pickaxe")


class CharacterEntities(Character):
    """This class contains all Character objects"""
    
    harry = None 
    """_Enemy_"""
    
    josephine = None
    """_Friend_"""
    
    josh = None
    """Trader"""
    
    @classmethod
    def initialise(cls):
        """Initialise Character objects"""
        cls.harry = Enemy("Harry", "A smelly Wumpus")
        cls.harry.set_conversation("Hangry...Hanggrry")
        cls.harry.set_weakness("vegemite")
        cls.harry.set_attack("super punch", 20)
        cls.harry.set_attack("body slam", 10)
        cls.harry.set_attack("rock fall", 15)
        cls.harry.set_health(40)

        cls.josephine = Friend("Josephine", "A friendly bat")
        cls.josephine.set_conversation("Gidday")        

        cls.josh = Trader("Josh", "An undead miner looking for gold")
        cls.josh.set_conversation("GOLLLD!")
        cls.josh.set_trade(
            item_trades= "pickaxe", 
            item_wants = "sunken treasure") 
        
        
class Links(CaveEntities, ItemEntities, CharacterEntities):
    """This class contains the relationship between Cave objects"""
    
    @classmethod
    def initialise_cave_relationships(cls):
        """Initialise the links between caves"""
        cls.cavern.link_cave(cls.dungeon, "south")
        cls.dungeon.link_cave(cls.cavern, "north")

        cls.grotto.link_cave(cls.dungeon, "east")
        cls.dungeon.link_cave(cls.grotto, "west")

        cls.underground_lake.link_cave(cls.grotto, "east")
        cls.grotto.link_cave(cls.underground_lake, "west")

        cls.abandoned_mine.link_cave(cls.dungeon, "west")
        cls.dungeon.link_cave(cls.abandoned_mine, "east")  
        
    @classmethod
    def initialise_item_locations(cls):
        """Initialise location of items in the caves"""
        cls.grotto.set_item(cls.vegemite)
        cls.dungeon.set_item(cls.torch)        
        cls.underground_lake.set_item(cls.sunken_treasure)        
    
    @classmethod
    def initialise_character_locations(cls):
        """Initialise location of characters in the caves"""
        cls.dungeon.set_character(cls.harry) 
        cls.grotto.set_character(cls.josephine)
        cls.abandoned_mine.set_character(cls.josh)
        
        
# class Game():
#     """This class store Game wide variable"""
#     current_cave = None
#     cave_inhabitant = None
#     cave_item = None
    
#     run_game = None
#     win_condition = None
    
#     last_command = None
    
#     standard_text_colour = None
#     standard_print_speed = None
    
#     item_text_colour = None
#     character_text_colour = None
    
#     @classmethod
#     def set_win_condition(cls, win_condition):
#         cls.win_condition = win_condition
    
#     @classmethod
#     def initialise(cls):
#         """Initialise Game objects"""
#         cls.run_game = True
#         cls.current_cave = CaveEntities.cavern
#         cls.last_command = None
        
#         cls.standard_text_colour = ""
#         cls.standard_print_speed = 0.06
#         cls.item_text_colour = "\x1b[38;5;207m"
#         cls.character_text_colour = "\x1b[38;5;81m"