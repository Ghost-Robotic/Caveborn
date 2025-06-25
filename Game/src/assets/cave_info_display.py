from src.entities.character import Character
from src.entities.item import Item
from src.commands.commands import Command

class CaveDisplay():
    character_name = None
    character_description = None
    
    item_name = None
    item_description = None
    
    character_display = []
    character_display= []    
    item_display = []

    @classmethod
    def update_character_info(cls, name, description):
        cls.character_name = "\x1b[38;5;81m"+name+"\x1b[0m " + Character.describe(Command.random_range(0, len(Character.describe_options)-1))
        cls.character_description = description
        
    @classmethod
    def update_item_info(cls, name, description):
        cls.item_name = Item.describe(Command.random_range(0, len(Item.describe_options)-1)) + " \x1b[38;5;207m"+name+"\x1b[0m" 
        cls.item_description = description
        
    @classmethod
    def update_display(cls):
        spacing_line_1 = len(cls.character_description) - (len(cls.character_name)-15)
        spacing_line_2 = 0
        spacing_line_edge = max(len(cls.character_description), len(cls.character_name)-15)
        if spacing_line_1 < 0:
            spacing_line_2 = abs(spacing_line_1)
            spacing_line_1 = 0
            
        cls.character_display = [
            f"╔───" + spacing_line_edge * "─" + "╗",
            f"│ {cls.character_name}" + (spacing_line_1 * " ") + " │",
            f"│  {cls.character_description}" +  (spacing_line_2 * " ") + " │",
            f"╚───" + spacing_line_edge * "─" + "╝"
        ]
        
        spacing_line_1_2 = len(cls.item_description) - (len(cls.item_name)-16)
        spacing_line_2_2 = 0
        spacing_line_edge_2 = max(len(cls.item_description), len(cls.item_name)-16)
        if spacing_line_1_2 < 0:
            spacing_line_2_2 = abs(spacing_line_1_2)
            spacing_line_1_2 = 0        
        
        cls.item_display = [
            f"  ╔───" + spacing_line_edge_2 * "─" + "╗",
            f"  │ {cls.item_name}" + (spacing_line_1_2 * " ") +  " │",
            f"  │  {cls.item_description}" +  (spacing_line_2_2 * " ") + " │",
            f"  ╚───" + spacing_line_edge_2 * "─" + "╝"
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
    character_health = None
    
    @classmethod
    def update_character_info(cls, name, description, health):
        cls.character_name = name
        cls.character_description = description
        cls.character_health = health
        
    @classmethod
    def update_display(cls):
        spacing_line_1 = len(cls.character_description) - len(cls.character_name) - len(str(cls.character_health)) - 9
        spacing_line_2 = 0
        spacing_line_edge = max(len(cls.character_description), len(cls.character_name) + len(str(cls.character_health)) + 10)
        if spacing_line_1 < 0:
            spacing_line_2 = abs(spacing_line_1)
            spacing_line_1 = 0
            
        cls.character_display = [
            f"╔──" + spacing_line_edge * "─" + "╗",
            f"│ \x1b[38;5;81m{cls.character_name}  \x1b[38;5;46mHealth: \x1b[1;38;5;201m{cls.character_health}\x1b[0m" + (spacing_line_1 * " ") + " │",
            f"│  {cls.character_description}" +  (spacing_line_2 * " ") + " │",
            f"╚──" + spacing_line_edge * "─" + "╝"
        ]