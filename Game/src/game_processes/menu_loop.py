from src.commands.commands import Command
from src.config import Config
from src.assets.title import Title

def title_display():
    Title.output()
    print("Welcome to Caveborn")
    print("Your parents disappeared when you were younger, leaving you to fend for yourself.")
    print("Curious at what lies beyond the solace, you venture out into the caves")
    print("As you explore you will meet formidable foes determined to stop your escape.")
    print("Make friends, find weapons and escape the caves!\n")
    

start_dialogue = [
    "You take your first breath and open your eyes...",
    "The air is still and silent...",
    "You make out the shape of a dimly lit cave...",
    "Living only off berries and water from dripping stalactites, you survive in the relative safety of the solace",
    "20 years later, you yearn for adventure...",
    "Picking up a rock and a handful of berries you venture off into a tunnel..."
]

def start_sequence():
    Command.clear_terminal()
    Command.pause(0.7)
    print("\033[?25l")    
    
    for line in start_dialogue:
        Command.clear_terminal()
        print("")
        Command.sequential_print(line, 0.08, "")
        Command.pause(0.7)


    Title.cascade_output()
    print("\033[?25h")
    Command.pause(0.9)

def end_sequence():
    for i in range(3):
        Command.clear_terminal()
        Title.output()
        print("\nEntering the caves", end = "")
        Command.sequential_print("...", 0.2, "") 


def menu_loop():
    
    start_sequence()
        
    game_mode = None    
    game_tip = None
    while True:
        Command.clear_terminal()
        title_display()
        print('Select a game mode from the list below or type "\x1b[38;5;226mEnter the caves\x1b[0m" to start the game.')
        print("Type exit any time to quit the game.")
        print(" (\x1b[38;5;226m1\x1b[0m) default")
        print("")
        
        if game_mode is not None:
            print(f"Selected game mode: \x1b[38;5;226m{game_mode}\x1b[0m")
            print(f"    {game_tip}")
        
        command = Command.get_input()
        
        match command:
            case "1" | "default":
                game_mode = "default"
                game_tip = "Defeat all enemies"
                
            case "enter the caves" | "start" | "begin":
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