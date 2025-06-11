class Bitmap():
    north = None
    east = None
    south = None
    west = None
    
    health = None
    
    height = 7
    
    bitmap_direction = []
    
    bitmap_info = []
    
    @classmethod
    def update_map(cls, current_cave, health):
        cls.health = health
        linked_caves = current_cave.get_linked_caves()
        
        if "north" in linked_caves:
            cls.north = "\x1b[91mN\x1b[0m"       
        else:
            cls.north = "N"
        
        if "east" in linked_caves:
            cls.east = "\x1b[91mE\x1b[0m"
        else:
            cls.east = "E"
        
        if "south" in linked_caves:
            cls.south = "\x1b[91mS\x1b[0m"
        else:
            cls.south = "S"
        
        if "west" in linked_caves:
            cls.west = "\x1b[91mW\x1b[0m"
        else:
            cls.west = "W"

        cls.bitmap_direction = [
            f"",
            f"    {cls.north}    ",     #R1 len:9
            f"    ʌ    ",           #R2 len:9
            f"{cls.west} < o > {cls.east}", #R3 len:9
            f"    v    ",           #R4 len:9
            f"    {cls.south}    ",      #R5 len:9
            f""
        ]
        
        cls.bitmap_info = [
            f"",
            f"| \x1b[92mHealth\x1b[0m: \x1b[1m\x1b[95m{cls.health}\x1b[0m",
            f"| ",
            f"| ",
            f"| ",    
            f"| ",
            f"" 
        ]                        
            
    @classmethod 
    def display_bitmap(cls):
        for line in range(cls.height):
            print(cls.bitmap_direction[line] , cls.bitmap_info[line])