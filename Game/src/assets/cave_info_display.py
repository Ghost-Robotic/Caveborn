from src.entities.character import Character, Enemy, Trader, Friend
from src.entities.item import Item
from src.commands.commands import Command

class CaveDisplay():
    """Display for the item and character information"""
    character_symbol = None
    character_name = None
    character_description = None
    
    item_name = None
    item_description = None
    item_durability = None
    
    character_display= []    
    item_display = []

    @classmethod
    def update_character_info(cls, character):
        if isinstance(character, Enemy):
            cls.character_symbol = "\x1b[38;5;196m୧༼ಠ益ಠ༽୨\x1b[0m"
            
        elif isinstance(character, Trader):
            cls.character_symbol = "\x1b[38;5;81m✿⊂(◉‿◉)つ🗝\x1b[0m"        
            
        elif isinstance(character, Friend):
            cls.character_symbol = f"\x1b[38;5;81m(｡◕‿‿◕｡)\x1b[0m"
            
        cls.character_name = "\x1b[38;5;81m"+character.name+"\x1b[0m " + Character.describe(Command.random_range(0, len(Character.describe_options)-1))
        cls.character_description = character.description
        
    @classmethod
    def update_item_info(cls, item):
        cls.item_name = Item.describe(Command.random_range(0, len(Item.describe_options)-1)) + " \x1b[38;5;207m"+item.name+"\x1b[0m" 
        cls.item_description = item.description
        
    @classmethod
    def update_character_display(cls):
        spacing_line_1 = len(cls.character_description) - (len(cls.character_name)-15)
        spacing_line_2 = 0
        spacing_line_edge = max(len(cls.character_description), len(cls.character_name)-15)
        if spacing_line_1 < 0:
            spacing_line_2 = abs(spacing_line_1)
            spacing_line_1 = 0
            
        cls.character_display = [
            cls.character_symbol,
            f"╔───" + spacing_line_edge * "─" + "╗  ",
            f"│ {cls.character_name}" + (spacing_line_1 * " ") + " │  ",
            f"│  {cls.character_description}" +  (spacing_line_2 * " ") + " │  ",
            f"╚───" + spacing_line_edge * "─" + "╝  "
        ]
        
    @classmethod
    def update_item_display(cls):
        spacing_line_1_2 = len(cls.item_description) - (len(cls.item_name)-16)
        spacing_line_2_2 = 0
        spacing_line_edge_2 = max(len(cls.item_description), len(cls.item_name)-16)
        if spacing_line_1_2 < 0:
            spacing_line_2_2 = abs(spacing_line_1_2)
            spacing_line_1_2 = 0        
        
        cls.item_display = [
            f"",
            f"╔───" + spacing_line_edge_2 * "─" + "╗",
            f"│ {cls.item_name}" + (spacing_line_1_2 * " ") +  " │",
            f"│  {cls.item_description}" +  (spacing_line_2_2 * " ") + " │",
            f"╚───" + spacing_line_edge_2 * "─" + "╝"
        ]
        
    @classmethod
    def display_character(cls):
        for line in cls.character_display:
            print(line)
            
    @classmethod
    def display_item(cls):
        for line in cls.item_display:
            print(line)
    
    @classmethod
    def display(cls):
        for i in range(len(cls.character_display)):
            print(cls.character_display[i] + cls.item_display[i])
            
            
class CombatDisplay(CaveDisplay):
    """Display character information during a fight"""
    character_health = None
    
    @classmethod
    def update_character_info(cls, character):
        cls.character_symbol = "\x1b[38;5;196m୧༼ಠ益ಠ༽୨\x1b[0m"
        cls.character_name = character.name
        cls.character_description = character.description
        cls.character_health = round(character.health, 1)
        
    @classmethod
    def update_display(cls):
        spacing_line_1 = len(cls.character_description) - len(cls.character_name) - len(str(cls.character_health)) - 9
        spacing_line_2 = 0
        spacing_line_edge = max(len(cls.character_description), len(cls.character_name) + len(str(cls.character_health)) + 10) + 1
        if spacing_line_1 < 0:
            spacing_line_2 = abs(spacing_line_1)
            spacing_line_1 = 0
            
        cls.character_display = [
            cls.character_symbol,
            f"╔──" + spacing_line_edge * "─" + "╗",
            f"│ \x1b[38;5;81m{cls.character_name}  \x1b[38;5;46mHealth: \x1b[1;38;5;201m{cls.character_health}\x1b[0m" + (spacing_line_1 * " ") + " │",
            f"│  {cls.character_description}" +  (spacing_line_2 * " ") + " │",
            f"╚──" + spacing_line_edge * "─" + "╝"
        ]
        
class DescriptionDisplay(CaveDisplay):
    """Display item or character information when asked by user"""
    @classmethod
    def update_character_info(cls, character):
        if isinstance(character, Enemy):
            cls.character_symbol = "\x1b[38;5;196m୧༼ಠ益ಠ༽୨\x1b[0m"
            
        elif isinstance(character, Trader):
            cls.character_symbol = "\x1b[38;5;81m✿⊂(◉‿◉)つ🗝\x1b[0m"        
            
        elif isinstance(character, Friend):
            cls.character_symbol = f"\x1b[38;5;81m(｡◕‿‿◕｡)\x1b[0m"
            
        cls.character_name = "\x1b[38;5;81m"+character.name+"\x1b[0m "
        cls.character_description = character.description
        
    @classmethod
    def update_item_info(cls, item):
        cls.item_durability = str(item.durability)
        if cls.item_durability is None:
            cls.item_durability = "∞"
                    
        cls.item_name = "\x1b[38;5;207m"+item.name+"\x1b[0m" 
        cls.item_description = item.description    
        
    @classmethod
    def update_character_display(cls):
        spacing_line_1 = len(cls.character_description) - (len(cls.character_name)-15)
        spacing_line_2 = 0
        spacing_line_edge = max(len(cls.character_description), len(cls.character_name)-15)
        if spacing_line_1 < 0:
            spacing_line_2 = abs(spacing_line_1)
            spacing_line_1 = 0
            
        cls.character_display = [
            cls.character_symbol,
            f"╔───" + spacing_line_edge * "─" + "╗  ",
            f"│ {cls.character_name}" + (spacing_line_1 * " ") + " │  ",
            f"│  {cls.character_description}" +  (spacing_line_2 * " ") + " │  ",
            f"╚───" + spacing_line_edge * "─" + "╝  "
        ]
        
    @classmethod
    def update_item_display(cls):
        spacing_line_1_2 = len(cls.item_description) - (len(cls.item_name) + len(cls.item_durability) -2)
        spacing_line_2_2 = 0
        spacing_line_edge_2 = max(len(cls.item_description), len(cls.item_name) + len(cls.item_durability)-2)
        if spacing_line_1_2 < 0:
            spacing_line_2_2 = abs(spacing_line_1_2)
            spacing_line_1_2 = 0        

        cls.item_display = [
            f"",
            f"╔───" + spacing_line_edge_2 * "─" + "╗",
            f"│ {cls.item_name}" + f"  \x1b[38;5;39mDurability:\x1b[0m {cls.item_durability}" + (spacing_line_1_2 * " ") +  " │",
            f"│  {cls.item_description}" +  (spacing_line_2_2 * " ") + " │",
            f"╚───" + spacing_line_edge_2 * "─" + "╝"
        ]