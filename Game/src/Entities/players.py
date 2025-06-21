class Player():
    """This class is used to interact with Player Entity"""
    bag = None
    dead = None
    health = None  
    
    @classmethod
    def initialise(cls):
        """Initialise Player object"""
        cls.bag = []
        cls.dead = False
        cls.health = 100    
    
    @classmethod
    def update_state(cls):
        """
        Updates player variables
        """
        cls.health = (cls.health if cls.health <= 100 else 100)
    
    @classmethod
    def damage(cls, damage):
        cls.health = cls.health - damage
        
    @classmethod
    def heal(cls, heal):
        cls.health = cls.health + heal