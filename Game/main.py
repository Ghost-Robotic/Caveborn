#from src.entities.Player import Player
from src.config import Config, PlayerEntity
from src.commands.game_commands import GameCommand
from src.commands.player_commands import PlayerCommand

Config.initialise()
last_command = None

#loops while player is still alive
while PlayerEntity.dead == False:
    GameCommand.clear_terminal()
    GameCommand.update_state()
    GameCommand.display_details()
    GameCommand.print_last_command(last_command)
    
    command = GameCommand.get_input()
    
    last_command = command
    
    GameCommand.clear_terminal()
    
    match command:
        case "north" | "south" | "east" | "west":
            PlayerCommand.move(command)
            continue

        case "talk":
            PlayerCommand.talk()
        
        case "fight":
            PlayerCommand.fight()

        case "pat":
            PlayerCommand.pat()
            
        case "take":
            PlayerCommand.take()
            
        case "trade":
            PlayerCommand.trade()
        
        case _:
            PlayerCommand.invalid()