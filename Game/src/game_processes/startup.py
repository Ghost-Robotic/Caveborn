from src.config import Config, CaveEntities, CharacterEntities, ItemEntities, Links
from src.entities.player import Player
from src.game import Game
from src.commands.commands import Command

def startup(game_mode):
    Config.initialise()
    print("\x1b[=17h")

    CaveEntities.initialise()
    ItemEntities.initialise()
    CharacterEntities.initialise()
    
    Links.initialise_cave_relationships() 
    Links.initialise_item_locations()
    Links.initialise_character_locations()
    
    Player.initialise()  
     
    Game.initialise()
    
    Player.bag.append(ItemEntities.rock)
    Player.bag.append(ItemEntities.berries)
    
    Game.set_game_mode(game_mode)