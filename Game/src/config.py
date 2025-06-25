from src.entities.cave import Cave
from src.entities.character import Character, Enemy, Friend, Trader
from src.entities.item import Item
from src.entities.player import Player

class Config():
    """This class initialise all game entities"""
        
    @classmethod
    def initialise(cls):
        """Initialise game entities"""
        CaveEntities.initialise()
        ItemEntities.initialise()
        CharacterEntities.initialise()
        
        Links.initialise_cave_relationships() 
        Links.initialise_item_locations()
        Links.initialise_character_locations()
        
        PlayerEntity.initialise()    
        Game.initialise()


class CaveEntities(Cave):
    """This class contains all the Cave objects"""
    
    # zone 1
    solace = None
    cavern = None
    dungeon = None

    # zone 2
    grotto = None
    evergreenGrove = None
    lushCave = None
    overgrownTemple = None
    mushroomMellows = None

    # zone 3
    tundraTunnels = None
    frozenLake = None
    glacierGeodes = None
    polarCove = None
    articPit = None
    crystalCrypt = None
    
    # zone 4
    lavaLagoon = None
    emberRift = None
    magmaMines = None
    hellfireHollows = None
    basaltBurrows = None
    georgesRoom = None
    ashenVault = None
    stalactiteShaft = None
    theChasamsEnd = None
    
    
    @classmethod 
    def initialise(cls):
        """Initialise Cave objects"""
        # zone 1
        cls.solace = Cave("Solace")
        cls.solace.set_description("")

        cls.cavern = Cave("Cavern")
        cls.cavern.set_description("A damp and dirty cave.")

        cls.dungeon = Cave("Dungeon")
        cls.dungeon.set_description("A large cave with a rack.")

        # zone 2
        cls.grotto = Cave("Grotto")
        cls.grotto.set_description("A small cave with ancient graffiti.")

        cls.evergreenGrove = Cave("Evergreen Grove")
        cls.evergreenGrove.set_description("Verdant tunnels wrapped in moss and roots.")

        cls.lushCave = Cave("Lush Cave")
        cls.lushCave.set_description("Exotic plants and waterfalls thrive underground.")

        cls.overgrownTemple = Cave("Overgrown Temple")
        cls.overgrownTemple.set_description("Ancient ruins overtaken by vines.")

        cls.mushroomMellows = Cave("Mushroom Mellows")
        cls.mushroomMellows.set_description("Towering mushrooms glow in the mist.")

        # zone 3
        cls.tundraTunnels = Cave("Tundra Tunnels")
        cls.tundraTunnels.set_description("Frozen paths lined with creeping frost.")

        cls.frozenLake = Cave("Frozen Lake")
        cls.frozenLake.set_description("A vast icy expanse reflecting faint light.")

        cls.glacierGeodes = Cave("Glacier Geodes")
        cls.glacierGeodes.set_description("Shimmering ice crystals embedded in rock.")

        cls.polarCove = Cave("Polar Cove")
        cls.polarCove.set_description("A cold, windswept cavern of stone.")

        cls.arcticPit = Cave("Arctic Pit")
        cls.arcticPit.set_description("A sheer drop into frozen depths.")

        cls.crystalCrypt = Cave("Crystal Crypt")
        cls.crystalCrypt.set_description("Jagged crystals refract fractured light.")

        # zone 4
        cls.lavaLagoon = Cave("Lava Lagoon")
        cls.lavaLagoon.set_description("Molten rivers churn, steam rising.")

        cls.emberRift = Cave("Ember Rift")
        cls.emberRift.set_description("Blackened rock split by glowing embers.")

        cls.magmaMines = Cave("Magma Mines")
        cls.magmaMines.set_description("Tunnels wind dangerously near lava veins.")

        cls.hellfireHollows = Cave("Hellfire Hollows")
        cls.hellfireHollows.set_description("A scorched cavern of fire and embers.")

        cls.basaltBurrows = Cave("Basalt Burrows")
        cls.basaltBurrows.set_description("Volcanic tunnels carved by magma.")

        cls.georgesRoom = Cave("George's Room")
        cls.georgesRoom.set_description("George is here.")

        cls.ashenVault = Cave("Ashen Vault")
        cls.ashenVault.set_description("Soot-stained walls whisper of past flames.")

        cls.stalactiteShaft = Cave("Stalactite Shaft")
        cls.stalactiteShaft.set_description("A towering vertical cave lined with stone teeth.")

        cls.chasmsEnd = Cave("The Chasm's End")
        cls.chasmsEnd.set_description("Light breaks; the final fight is here.")
        
class ItemEntities(Item):
    """""This class contains all Item objects:"""""
    vegemite = None
    torch = None
    sunken_treasure = None
    pickaxe = None
    
    @classmethod
    def initialise(cls):
        """Initialise Item objects"""
        cls.vegemite = Item("vegemite")
        cls.vegemite.set_description("A Wumpuses worst nightmare")

        cls.torch = Item("torch")
        cls.torch.set_description("A light for the end of the tunnel")

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
        # solace links
        cls.solace.link_cave(cls.grotto, "north")
        cls.solace.link_cave(cls.cavern, "east")
        cls.solace.link_cave(cls.tundraTunnels, "south")
        cls.solace.link_cave(cls.lavaLagoon, "west")

        # cavern links
        cls.cavern.link_cave(cls.dungeon, "north")
        cls.cavern.link_cave(cls.solace, "west")

        # dungeon links
        cls.dungeon.link_cave(cls.cavern, "south")

        # grotto links
        cls.grotto.link_cave(cls.evergreenGrove, "east")
        cls.grotto.link_cave(cls.solace, "south")

        # evergreen grove links
        cls.evergreenGrove.link_cave(cls.grotto, "west")
        cls.evergreenGrove.link_cave(cls.lushCave, "north")

        # lush cave links
        cls.lushCave.link_cave(cls.overgrownTemple, "east")
        cls.lushCave.link_cave(cls.mushroomMellows, "west")

        # overgrown temple links
        cls.overgrownTemple.link_cave(cls.lushCave, "west")

        # mushroom mellows links
        cls.mushroomMellows.link_cave(cls.lushCave, "east")

        # tundra tunnels links
        cls.tundraTunnels.link_cave(cls.solace, "north")
        cls.tundraTunnels.link_cave(cls.frozenLake, "east")
        cls.tundraTunnels.link_cave(cls.polarCove, "west")

        # frozen lake links
        cls.frozenLake.link_cave(cls.glacierGeodes, "north")
        cls.frozenLake.link_cave(cls.tundraTunnels, "west")

        # glacier geodes links
        cls.glacierGeodes.link_cave(cls.frozenLake, "south")

        # polar cove links
        cls.polarCove.link_cave(cls.tundraTunnels, "east")
        cls.polarCove.link_cave(cls.arcticPit, "south")

        # arctic pit links
        cls.arcticPit.link_cave(cls.polarCove, "north")
        cls.arcticPit.link_cave(cls.crystalCrypt, "east")

        # crystal crypt links
        cls.crystalCrypt.link_cave(cls.arcticPit, "west")

        # lava lagoon links
        cls.lavaLagoon.link_cave(cls.emberRift, "north")
        cls.lavaLagoon.link_cave(cls.solace, "east")
        cls.lavaLagoon.link_cave(cls.hellfireHollows, "west")

        # hellfire hollows links
        cls.hellfireHollows.link_cave(cls.basaltBurrows, "north")
        cls.hellfireHollows.link_cave(cls.lavaLagoon, "east")

        # basalt burrows links
        cls.basaltBurrows.link_cave(cls.georgesRoom, "north")
        cls.basaltBurrows.link_cave(cls.ashenVault, "east")
        cls.basaltBurrows.link_cave(cls.hellfireHollows, "south")

        # george’s room links
        cls.georgesRoom.link_cave(cls.basaltBurrows, "south")

        # ashen vault links
        cls.ashenVault.link_cave(cls.stalactiteShaft, "north")
        cls.ashenVault.link_cave(cls.basaltBurrows, "west")

        # stalactite shaft links
        cls.stalactiteShaft.link_cave(cls.emberRift, "east")
        cls.stalactiteShaft.link_cave(cls.chasmsEnd, "west")

        # ember rift links
        cls.emberRift.link_cave(cls.magmaMines, "east")
        cls.emberRift.link_cave(cls.stalactiteShaft, "west")

        # magma mines links
        cls.magmaMines.link_cave(cls.emberRift, "west")

        # the chasm’s end links
        cls.chasmsEnd.link_cave(cls.stalactiteShaft, "east")

        
    @classmethod
    def initialise_item_locations(cls):
        """Initialise location of items in the caves"""
        cls.dungeon.set_item(cls.torch)        
     
    
    @classmethod
    def initialise_character_locations(cls):
        """Initialise location of characters in the caves"""
        cls.dungeon.set_character(cls.harry) 

          
        
class PlayerEntity(Player):
    """This class contains all the information about the Player"""
    
    @classmethod
    def initialise(cls):
        """Initialise Player object"""
        cls.bag = []
        cls.dead = False
        cls.health = 100
        
        
class Game():
    """This class store Game wide variable"""
    current_cave = None
    cave_inhabitant = None
    cave_item = None
    
    standard_text_colour = None
    standard_print_speed = None
    
    item_text_colour = None
    character_text_colour = None
    
    @classmethod
    def initialise(cls):
        """Initialise Game objects"""
        cls.current_cave = CaveEntities.solace
        cls.standard_text_colour = ""
        cls.standard_print_speed = 0.06
        cls.item_text_colour = "\x1b[38;5;207m"
        cls.character_text_colour = "\x1b[38;5;81m"