class Bitmap():
    north = None
    east = None
    south = None
    west = None
    
    health = None
    bag = None
    
    height = 7
    
    bitmap_direction = []
    bitmap_info = []
    
    @classmethod
    def update_info(cls, current_cave, health, bag):
        cls.health = health
        
        if bag == []:
            cls.bag = "Empty"            
        else:
            cls.bag = bag[0]
            for i in range(len(bag)-1):
                cls.bag = cls.bag + "\x1b[39m, \x1b[38;5;207m" + bag[i+1]    
        
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
    def update_map(cls):
        cls.bitmap_direction = [
            f" ___________",                  #R1 len:11
            f"|     {cls.north}    ",         #R1 
            f"|     ʌ    ",                   #R2 
            f"| {cls.west} < o > {cls.east}", #R3 
            f"|     v    ",                   #R4 
            f"|     {cls.south}    ",         #R5 
            f" ‾‾‾‾‾‾‾‾‾‾‾"                   #R5 
        ]
        
        cls.bitmap_info = [
            f"",
            f"| \x1b[38;5;46mHealth\x1b[0m: \x1b[1;38;5;201m{cls.health}\x1b[0m",
            f"| \x1b[38;5;39mBag\x1b[0m: [\x1b[38;5;207m{cls.bag}\x1b[0m]",
            f"| ",
            f"| ",    
            f"| ",
            f"" 
        ]                        
          
            
    @classmethod 
    def display_bitmap(cls):
        for line in range(cls.height):
            print(cls.bitmap_direction[line] , cls.bitmap_info[line])