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
    arcticPit = None
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
    chasmsEnd = None
    
    
    @classmethod 
    def initialise(cls):
        """Initialise Cave objects"""
        # zone 1
        cls.solace = Cave("Solace")
        cls.solace.set_description("A quiet, dim refuge before the journey began.")

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
    # Items
    torch = None
    pickaxe = None
    rock = None
    coal = None
    iridescentInferno = None
    shabbyShiv = None
    explodingSnowball = None
    iceSickle = None

    # Healing Items
    berries = None
    mysticalStick = None
    healingPotion = None
    blazeRod = None
    healingSpores = None
    
    @classmethod
    def initialise(cls):
        """Initialise Item objects"""
    # Items
        cls.rock = Item("Rock")
        cls.rock.set_description("It’s a rock! Deals 20 base damage.")
        cls.rock.set_base_damage(20)

        cls.pickaxe = Item("Pickaxe")
        cls.pickaxe.set_description("An iron pickaxe for mining stone. Deals base 33 damage.")
        cls.pickaxe.set_base_damage(33)

        cls.coal = Item("Coal")
        cls.coal.set_description("It’s coal…look I don’t know what else you want me to say. Deals 16 base damage. Deals 16 base damage.")
        cls.coal.set_base_damage(16)

        cls.iridescentInferno = Item("Iridescent Inferno")
        cls.iridescentInferno.set_description("A fiery sword forged by gods. Deals 40 base damage.")
        cls.iridescentInferno.set_base_damage(40)

        cls.shabbyShiv = Item("Shabby Shiv")
        cls.shabbyShiv.set_description("More of a threatening tool than a weapon. Deals 25 base damage.")
        cls.shabbyShiv.set_base_damage(25)
        cls.shabbyShiv.set_durability(20)

        cls.explodingSnowball = Item("Exploding Snowball")
        cls.explodingSnowball.set_description("Looks like a snowball but why do I hear something fizzing. Deals 50 base damage.")
        cls.explodingSnowball.set_base_damage(50)
        cls.explodingSnowball.set_durability(1)

        cls.iceSickle = Item("Ice Sickle")
        cls.iceSickle.set_description("A sickle made from ice. Deals 30 base damage.")
        cls.iceSickle.set_base_damage(30)

        cls.torch = Item("Torch")
        cls.torch.set_description("A light for the end of the tunnel. Deals 15 base damage.")

    # Healing Items
        cls.berries = HealingItem("Berries")
        cls.berries.set_description("Your only source of food, heals 3 health.")
        cls.berries.set_heals_for(3)
        cls.berries.set_durability(6)
    
        cls.mysticalStick = HealingItem("Mystical Stick")
        cls.mysticalStick.set_description("A stick with a subtle green glow. Heals 4 health.")
        cls.mysticalStick.set_heals_for(4)
        cls.mysticalStick.set_durability(10)

        cls.healingPotion = HealingItem("Healing Potion")
        cls.healingPotion.set_description("A glass vial with green liquid. Heals 16 health.")
        cls.healingPotion.set_heals_for(16)
        cls.healingPotion.set_durability(1)

        cls.healingSpores = HealingItem("Healing Spores")
        cls.healingSpores.set_description("Mysterious healing mushroom. Heals 10 health.")
        cls.healingSpores.set_heals_for(10)
        cls.healingSpores.set_durability(5)

        cls.blazeRod = HealingItem("Blaze Rod")
        cls.blazeRod.set_description("The energy source of an ancient city, still active. Heals 7 health.")
        cls.blazeRod.set_heals_for(7)
        cls.blazeRod.set_durability(15)


class CharacterEntities(Character):
    """This class contains all Character objects"""
    
    """Enemy"""
    caveRats = None
    graffitiGoblin = None
    giantVenusFlytrap = None
    templeRaider = None
    shroomWalker = None
    iceWraith = None
    crystalCrawler = None
    frostGiant = None
    moltenMulloway = None
    cinderBug = None
    george = None
    emberMaw = None
    flameImp = None
    runedSkeletonKing = None

    """Trader"""
    snowman = None
    nickSaint = None
    coalMiner = None
    pyroAlchemist = None

    """Friends"""
    lonelyMage = None
    mossMan = None
    yeti = None
    salamander = None

    @classmethod
    def initialise(cls):
        """Initialise Character objects"""
    # Enemies
        cls.caveRats = Enemy("Cave Rats", "A small group of rats swiftly scurry around you.")
        cls.caveRats.set_conversation("*squeak, squeak!!*")
        cls.caveRats.set_health(37)
        cls.caveRats.set_attack("ratapult", 10)
        cls.caveRats.set_attack("crown of claws", 6)
        cls.caveRats.set_attack("toe tickle", 3)

        cls.graffitiGoblin = Enemy("Graffiti Goblin", "A lean, mean and green goblin.")
        cls.graffitiGoblin.set_conversation("Hey, just let me express myself, yo. Or else.")
        cls.graffitiGoblin.set_health(25)
        cls.graffitiGoblin.set_attack("paint spray", 4)
        cls.graffitiGoblin.set_attack("can throw", 2)

        cls.giantVenusFlytrap = Enemy("Giant Venus Flytrap", "A towering carnivorous plant that snaps at anything warm-blooded.")
        cls.giantVenusFlytrap.set_conversation("*snaps shut with a deep squelch*")
        cls.giantVenusFlytrap.set_health(60)
        cls.giantVenusFlytrap.set_attack("bite", 6)
        cls.giantVenusFlytrap.set_attack("slap", 3)

        cls.templeRaider = Enemy("Temple Raider", "A greedy bandit looting the temple.")
        cls.templeRaider.set_conversation("Hey, this is my temple only!")
        cls.templeRaider.set_health(50)
        cls.templeRaider.set_attack("slash", 8)
        cls.templeRaider.set_attack("kick", 5)

        cls.shroomWalker = Enemy("Shroom Walker", "A lumbering mushroom creature with glowing spores and sluggish steps.")
        cls.shroomWalker.set_conversation("*pitter, patter*")
        cls.shroomWalker.set_health(55)
        cls.shroomWalker.set_attack("spore cloud", 6)
        cls.shroomWalker.set_attack("stomp", 4)

        cls.iceWraith = Enemy("Ice Wraith", "A ghostly figure made of wind and frost, gliding silently through the cold.")
        cls.iceWraith.set_conversation("Your warmth... it will not last.")
        cls.iceWraith.set_health(60)
        cls.iceWraith.set_attack("frost pierce", 10)
        cls.iceWraith.set_attack("chilling touch", 7)
        cls.iceWraith.set_attack("wither wind", 4)

        cls.crystalCrawler = Enemy("Crystal Crawler", "A nimble beetle-like creature, shimmering brightly.")
        cls.crystalCrawler.set_conversation("*chitters, crystal legs tapping*")
        cls.crystalCrawler.set_health(25)
        cls.crystalCrawler.set_attack("bite", 10)
        cls.crystalCrawler.set_attack("scratch", 5)

        cls.frostGiant = Enemy("Frost Giant", "A towering brute of ice and stone with a deep, rumbling growl.")
        cls.frostGiant.set_conversation("Tiny thing. Easy to crush.")
        cls.frostGiant.set_health(115)
        cls.frostGiant.set_attack("ice fist", 14)
        cls.frostGiant.set_attack("snow quake", 11)
        cls.frostGiant.set_attack("roar", 6)

        cls.moltenMulloway = Enemy("Molten Mulloway", "A large fish leaps from the lava and flops angrily on the floor ahead.")
        cls.moltenMulloway.set_conversation("Blub blub blub.")
        cls.moltenMulloway.set_health(30)
        cls.moltenMulloway.set_attack("bite", 8)
        cls.moltenMulloway.set_attack("tail slap", 4)


        cls.cinderBug = Enemy("Cinder Bug", "A small insect glowing with embers, ready to explode when threatened.")
        cls.cinderBug.set_conversation("*hisses softly*")
        cls.cinderBug.set_health(20)
        cls.cinderBug.set_attack("ignite", 20)
        cls.cinderBug.set_attack("ember dash", 2)

        cls.george = Enemy("George", "A friendly fellow content with his life.")
        cls.george.set_conversation("Hi, I’m George.")
        cls.george.set_health(100)
        cls.george.set_attack("the Jaws of George", 15)
        cls.george.set_attack("friendly tap", 2)
        cls.george.set_attack("hesitant hit", 3)

        cls.emberMaw = Enemy("Ember Maw", "A massive, lava-jawed beast that lurks below, waiting to lunge.")
        cls.emberMaw.set_conversation("Your bones will roast in my gut.")
        cls.emberMaw.set_health(80)
        cls.emberMaw.set_attack("lava chomp", 16)
        cls.emberMaw.set_attack("magma roar", 11)
        cls.emberMaw.set_attack("tail crack", 8)

        cls.flameImp = Enemy("Flame Imp", "A mischievous creature born of smoke and sparks.")
        cls.flameImp.set_conversation("Catch me if you can—hothead!")
        cls.flameImp.set_health(35)
        cls.flameImp.set_attack("fire poke", 6)
        cls.flameImp.set_attack("devious lick", 5)

        cls.runedSkeletonKing = Enemy("Runed Skeleton King", "An ancient skeletal monarch, etched with glowing runes of binding and fire.")
        cls.runedSkeletonKing.set_conversation("You trespass in death’s last kingdom.")
        cls.runedSkeletonKing.set_health(150)
        cls.runedSkeletonKing.set_attack("arrow of reckoning", 15)
        cls.runedSkeletonKing.set_attack("bone barrage", 10)
        cls.runedSkeletonKing.set_attack("skeletal smash", 6)

    # Traders
        cls.snowman = Trader("Snowman", "A round snow figure with a carrot as a nose and a missing stick arm.")
        cls.snowman.set_conversation("…")
        cls.snowman.set_trade(
            item_trades="exploding snowballs",
            item_wants="mystical stick"
        )

        cls.nickSaint = Trader("Nick Saint", "A shady figure in festive rags and a glowing red nose.")
        cls.nickSaint.set_conversation("Oh, oh, oh, It’s so dark in here. Hi there, wanna look under my coat?")
        cls.nickSaint.set_trade(
            item_trades="healing potion",
            item_wants="torch"
        )

        cls.coalMiner = Trader("Coal Miner", "Soot-streaked dwarf with glowing goggles and an aching back.")
        cls.coalMiner.set_conversation("I’ve got tools straight from the heart of the mines.")
        cls.coalMiner.set_trade(
            item_trades="pickaxe",
            item_wants="coal"
        )

        cls.pyroAlchemist = Trader("Pyro Alchemist", "A flashy robed alchemist snickering with a smoldering grin.")
        cls.pyroAlchemist.set_conversation("Fire isn't dangerous—until you make it into a sword. Want a sample?")
        cls.pyroAlchemist.set_trade(
            item_trades="iridescent inferno",
            item_wants="blaze Rod"
)
        
    # Friends
        cls.lonelyMage = Friend("Lonely Mage", "A weird friendless cloaked man.")
        cls.lonelyMage.set_conversation("Chasm’s End leads to the surface, but you must defeat all threats first, no danger can be allowed to escape.")

        cls.mossMan = Friend("Moss Man", "")
        cls.mossMan.set_conversation("People drop all sorts of stuff, healing items, weapons. Even if you don’t need them, someone else might.")

        cls.yeti = Friend("Yeti", "A friendly, snow-covered beast with glowing eyes and a chilling roar.")
        cls.yeti.set_conversation("People drop all sorts of stuff, healing items, weapons. Even if you don’t need them, someone else might.")

        cls.salamander = Friend("Salamander", "A friendly, fiery lizard that slinks between flames and stone.")
        cls.salamander.set_conversation("People drop all sorts of stuff, healing items, weapons. Even if you don’t need them, someone else might.")
        
        
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
        cls.lushCave.link_cave(cls.evergreenGrove, "south")

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
        cls.emberRift.link_cave(cls.lavaLagoon, "south")

        # magma mines links
        cls.magmaMines.link_cave(cls.emberRift, "west")

        # the chasm’s end links
        cls.chasmsEnd.link_cave(cls.stalactiteShaft, "east")

        
    @classmethod
    def initialise_item_locations(cls):
        """Initialise location of items in the caves"""
        cls.grotto.set_item(cls.mysticalStick)
        cls.evergreenGrove.set_item(cls.shabbyShiv)
        cls.mushroomMellows.set_item(cls.healingSpores)
        cls.glacierGeodes.set_item(cls.iceSickle)
        cls.lavaLagoon.set_item(cls.blazeRod)
        cls.dungeon.set_item(cls.torch)
        cls.basaltBurrows.set_item(cls.coal)       
     
    
    @classmethod
    def initialise_character_locations(cls):
        """Initialise location of characters in the caves"""
        cls.cavern.set_character(cls.caveRats)

        cls.grotto.set_character(cls.graffitiGoblin)

        cls.evergreenGrove.set_character(cls.mossMan)

        cls.lushCave.set_character(cls.giantVenusFlytrap)

        cls.overgrownTemple.set_character(cls.templeRaider)

        cls.mushroomMellows.set_character(cls.shroomWalker)

        cls.tundraTunnels.set_character(cls.iceWraith)

        cls.glacierGeodes.set_character(cls.crystalCrawler)

        cls.polarCove.set_character(cls.frostGiant)

        cls.crystalCrypt.set_character(cls.yeti)

        cls.lavaLagoon.set_character(cls.moltenMulloway)

        cls.hellfireHollows.set_character(cls.salamander)

        cls.basaltBurrows.set_character(cls.cinderBug)

        cls.georgesRoom.set_character(cls.george)

        cls.stalactiteShaft.set_character(cls.emberMaw)

        cls.emberRift.set_character(cls.flameImp)

        cls.chasmsEnd.set_character(cls.runedSkeletonKing)

        cls.dungeon.set_character(cls.lonelyMage)
        
        cls.frozenLake.set_character(cls.snowman)

        cls.arcticPit.set_character(cls.nickSaint)

        cls.ashenVault.set_character(cls.coalMiner)

        cls.magmaMines.set_character(cls.pyroAlchemist)


 
 
# class PlayerEntity(Player):
#     """This class contains all the information about the Player"""
    
#     @classmethod
#     def initialise(cls):
#         """Initialise Player object"""
#         cls.bag = []
#         cls.dead = False
#         cls.health = 100
        
        
# class Game():
#     """This class store Game wide variable"""
#     current_cave = None
#     cave_inhabitant = None
#     cave_item = None
    
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
#         cls.current_cave = CaveEntities.solace
#         cls.last_command = None
        
#         cls.standard_text_colour = ""
#         cls.standard_print_speed = 0.06
#         cls.item_text_colour = "\x1b[38;5;207m"
#         cls.character_text_colour = "\x1b[38;5;81m"