from src.commands.commands import Command
from src.config import Config
from src.assets.title import Title

def title_display():
    Title.output()
    print("Welcome to caveborn, a text based game where you can")
    print("navigate the networks of deadly caves, fight monsters")
    print("and find keys to escape to the surface.\n")
    

def start_sequence():
    Command.clear_terminal()
    print("\033[?25l")
    Title.cascade_output()
    Command.sequential_print("Welcome to caveborn, a text based game where you can", 0.03, "")
    print("")
    Command.sequential_print("navigate the networks of deadly caves, fight monsters", 0.03, "")
    print("")
    Command.sequential_print("and find keys to escape to the surface.", 0.03, "")
    print("\033[?25h")
    Command.pause(0.5)

def end_sequence():
    for i in range(3):
        Command.clear_terminal()
        Title.output()
        print("\nEntering the caves", end = "")
        Command.sequential_print("...", 0.2, "") 


def menu_loop():
    
    start_sequence()
        
    game_mode = None    
    while True:
        Command.clear_terminal()
        title_display()
        print('Select a game mode from the list below or type "\x1b[38;5;226mEnter the caves\x1b[0m" to start the game.')
        print("Type exit any time to quit the game.")
        print(" (\x1b[38;5;226m1\x1b[0m) default")
        print("")
        
        if game_mode is not None:
            print(f"Selected game mode: \x1b[38;5;226m{game_mode}\x1b[0m")
        
        command = Command.get_input()
        
        match command:
            case "1" | "default":
                game_mode = "default"
                
            case "enter the caves":
                if game_mode is not None:
                    end_sequence()
                    return game_mode
                else:
                    print("No game mode selected")
                    Command.wait_for_enter()
                    
            case "exit" | "quit":
                return "exit"
            
            case _:
                print('\nSelect a game mode by typing in its name or type "\x1b[38;5;226mEnter the caves\x1b[0m" to start the game')
                Command.wait_for_enter()   