from src.config import Config, CaveEntities, CharacterEntities, ItemEntities, PlayerEntity, Links
from src.game import Game

def startup(game_mode):
    Config.initialise()

    CaveEntities.initialise()
    ItemEntities.initialise()
    CharacterEntities.initialise()
    
    Links.initialise_cave_relationships() 
    Links.initialise_item_locations()
    Links.initialise_character_locations()
    
    PlayerEntity.initialise()  
     
    Game.initialise()
    
    Game.set_game_mode(game_mode)