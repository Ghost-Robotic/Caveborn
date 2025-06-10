class Player():
    """This class is used to interact with Player Entity"""
    bag = None
    dead = None
    health = None    
    
    @classmethod
    def damage(cls, damage):
        cls.health = cls.health - damage
        
    @classmethod
    def heal(cls, heal):
        cls.health = cls.health + heal