from src.game_processes.startup import startup
from src.game_processes.game_loop import game_loop
from src.game_processes.menu_loop import menu_loop

def main():
    
    game_mode = menu_loop()
    #game_mode = "default"
    if game_mode != "exit":
        startup(game_mode)
        
        game_loop()
    

if __name__ == "__main__":
    main()