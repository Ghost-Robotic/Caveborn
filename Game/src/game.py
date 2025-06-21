from .config import CaveEntities

class Game():
    """This class store Game wide variable"""
    current_cave = None
    cave_inhabitant = None
    cave_item = None
    
    run_game = None
    game_mode = None
    
    last_command = None
    
    @classmethod
    def set_game_mode(cls, game_mode):
        cls.game_mode = game_mode
    
    @classmethod
    def initialise(cls):
        """Initialise Game objects"""
        cls.run_game = True
        cls.current_cave = CaveEntities.cavern
        cls.last_command = None
        
    @classmethod
    def update_state(cls):
        """
        Updates Game variables.
        """
        cls.cave_inhabitant = cls.current_cave.get_character()
        cls.cave_item = cls.current_cave.get_item()
        