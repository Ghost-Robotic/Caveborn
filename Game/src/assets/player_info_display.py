class PlayerDisplay():
    north = None
    east = None
    south = None
    west = None
    
    health = None
    bag = None
    enemies = None
    
    height = 7
    
    player_compass = []
    player_info = []
    
    @classmethod
    def update_info(cls, current_cave, health, bag, enemies):
        cls.health = health
        cls.enemies = enemies
        
        if bag == []:
            cls.bag = "Empty"            
        else:
            if bag[0].durability is None:
                durability = "∞"
            else:
                durability = str(bag[0].durability)
            cls.bag = bag[0].name + " " + durability
            
            for i in range(len(bag)-1):
                if bag[i+1].durability is None:
                    durability = "∞"
                else:
                    durability = str(bag[i+1].durability)
                cls.bag = cls.bag + "\x1b[39m, \x1b[38;5;207m" + bag[i+1].name + " " + durability
        
        linked_caves = current_cave.get_linked_caves()
        
        if "north" in linked_caves:
            cls.north = "\x1b[38;5;196mN\x1b[0m"       
        else:
            cls.north = "N"
        
        if "east" in linked_caves:
            cls.east = "\x1b[38;5;196mE\x1b[0m"
        else:
            cls.east = "E"
        
        if "south" in linked_caves:
            cls.south = "\x1b[38;5;196mS\x1b[0m"
        else:
            cls.south = "S"
        
        if "west" in linked_caves:
            cls.west = "\x1b[38;5;196mW\x1b[0m"
        else:
            cls.west = "W"    
            
            
    @classmethod
    def update_display(cls):
        cls.player_compass = [
            f" ╔═══════════╗",                   #R1 len:12
            f" ║     {cls.north}     ║",         #R1 
            f" ║     ʌ     ║",                   #R2 
            f" ║ {cls.west} < o > {cls.east} ║", #R3 
            f" ║     v     ║",                   #R4 
            f" ║     {cls.south}     ║",         #R5 
            f" ╚═══════════╝"                    #R5 
        ]
        
        cls.player_info = [
            f"",
            f" \x1b[38;5;46mHealth\x1b[0m: \x1b[1;38;5;201m{cls.health}\x1b[0m",
            f" \x1b[38;5;39mBag\x1b[0m: [\x1b[38;5;207m{cls.bag}\x1b[0m]",
            f" ",
            f" \x1b[38;5;196mEnemies to defeat\x1b[0m: \x1b[38;5;129m{cls.enemies}\x1b[0m",    
            f" ",
            f"" 
        ]                        
          
            
    @classmethod 
    def output(cls):
        for line in range(cls.height):
            print(cls.player_compass[line] , cls.player_info[line])