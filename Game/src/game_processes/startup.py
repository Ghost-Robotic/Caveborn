from src.config import Config, CaveEntities, CharacterEntities, ItemEntities, Links
from src.entities.player import Player
from src.game import Game

def startup(game_mode):
    # initialise config variables
    Config.initialise()

    # initialise entities
    CaveEntities.initialise()
    ItemEntities.initialise()
    CharacterEntities.initialise()
    
    # initialise links
    Links.initialise_cave_relationships() 
    Links.initialise_item_locations()
    Links.initialise_character_locations()
    
    # initialise player and game defaults
    Player.initialise()  
    Game.initialise()
    
    Player.bag.append(ItemEntities.rock)
    Player.bag.append(ItemEntities.berries)
    
    Game.set_game_mode(game_mode)