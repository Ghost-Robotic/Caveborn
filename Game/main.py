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
    if last_command != None:
        print("\n> ", last_command)
    else:
        print("")
    
    print("\x1b[5m", end='')
    command = input(">\x1b[93m ").lower().strip()
    print('\x1b[0m', end="")
    
    last_command = command
    
    match command:
        case "north" | "south" | "east" | "west":
            PlayerCommand.move(command)

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
            print("Invalid Command")
            GameCommand.wait_for_enter()