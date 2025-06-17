from .config import Config, PlayerEntity
from .game import Game
from .commands.game_commands import GameCommand
from .commands.player_commands import PlayerCommand


def game_loop():
    while Game.run_game == True:
        GameCommand.clear_terminal()
        
        GameCommand.update_state()   
        
        GameCommand.display_details()
        
        GameCommand.print_last_command(Game.last_command)
        
        command = GameCommand.get_input()
        
        Game.last_command = command
        
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
                            
                
        Game.run_game = GameCommand.check_win_condition()   