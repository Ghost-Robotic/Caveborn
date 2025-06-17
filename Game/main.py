from src.game_processes.startup import startup
from src.game_processes.game_loop import game_loop
from src.game_processes.menu_loop import menu_loop

#menu loop
#create game instance (win_condition)
#initialise config
#loop game
    #game
    #check win_condition
#defeat/win message
#loop


def main():
    
    game_mode = menu_loop()
    
    startup(game_mode)
    
    game_loop()
    
    #game_over_message()


if __name__ == "__main__":
    main()