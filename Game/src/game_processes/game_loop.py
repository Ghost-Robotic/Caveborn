from src.entities.player import Player
from src.game import Game
from src.commands.commands import Command
from src.commands.player_commands import PlayerCommand


def game_loop():
    while Game.run_game == True:
        Command.clear_terminal()
        Game.update_state()   
        
        Player.update_state()
        
        Game.display_details()
        
        Game.print_last_command()
        
        command = Command.get_input()
        
        Game.last_command = command
        
        command_split = command.split(" ", 1)
        
        #Command.clear_terminal()
        if command is not "":
            match command_split[0]:
                case "north" | "south" | "east" | "west":
                    PlayerCommand.move(command)

                case "talk" | "grab":
                    PlayerCommand.talk()
                
                case "fight" | "attack":
                    PlayerCommand.fight()

                case "pat":
                    PlayerCommand.pat()
                    
                case "take":
                    PlayerCommand.take()
                    
                case "trade":
                    PlayerCommand.trade()
                    
                case "about" | "info" | "information" | "details" | "stats" | "inspect":
                    try:
                        PlayerCommand.about(command_split[1])
                    except:   
                        PlayerCommand.invalid()
                        
                case "exit" | "quit":
                    Game.game_mode = "exit"
                
                case _:
                    PlayerCommand.invalid()
                            
        Game.run_game = Game.check_win_condition()
    Game.print_game_over()