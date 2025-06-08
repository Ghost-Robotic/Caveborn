from src.entities.character import Enemy, Trader
from config import Config, Player, Game
from commands.game_commands import GameCommand
from commands.player_commands import PlayerCommand

Config.initialise()

#loops while player is still alive
while Player.dead == False:
    print("\n")
    #GameCommand.clear_terminal()
    
    Game.update_state()
    GameCommand.display_details()

    command = input("> ").lower().strip()
    
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
