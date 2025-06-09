from config import PlayerEntity

class Player(PlayerEntity):
    """This class is used to interact with Player Entity"""
    @classmethod
    def damage(cls, damage):
        cls.health = cls.health - damage
        
    @classmethod
    def heal(cls, heal):
        cls.health = cls.health + heal