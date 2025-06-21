from src.config import PlayerEntity, Config
from src.entities.character import Enemy
from src.game import Game
from src.assets.player_info_display import PlayerDisplay
from src.assets.title import Title
from os import system, name
from time import sleep
from sys import stdout

class GameCommand():
    def display_decorator(func):
        def wrapper(): 
            Title.output()
            PlayerDisplay.update_info(Game.current_cave, PlayerEntity.health, PlayerEntity.bag) 
            PlayerDisplay.update_display()                    
            PlayerDisplay.output()
            
            print("----------")
            print("\x1b[1;38;5;196m", Game.current_cave.get_name(), "\x1b[0m")
            print("----------")
            func()
        return wrapper
    
    
    @display_decorator
    @staticmethod
    def display_details():
        print(Game.current_cave.describe())
        
        if Game.cave_inhabitant is not None:
            print(Game.cave_inhabitant.describe())
            
        if Game.cave_item is not None:
            print(Game.cave_item.describe())
            
            
    @staticmethod
    def sequential_print(string, speed, colour):
        """
        Sequentially prints each character of a string at a given speed and colour.
        
        Args:
            string (str): String to be printed
            speed (float): Amount of time to pause before printing next character
            colour (str | escape code): Colour and formatting you want text to have
        """
        for character in string:
            stdout.write(f"{colour}{character}\x1b[0m_")
            stdout.write("\b \b")
            stdout.flush()
            sleep(speed)
        sleep(0.1)
          
            
    @staticmethod
    def sequential_print_segments(segments, strings, speeds, colours):
        """
        Sequentially prints each character of a string that has been split into segments
        with each segment being printed at different speeds and colours.
        
        strings, speeds and colours must be given in list and the length of those lists must match the given segments integer.
        
        The position of each speed and colour in their respective list will correspond to the position of each item in the strings list.

        Args:
            segments (int): Number of string segments to be printed
            strings (list [str]): String to be printed list
            speeds (list [float]): Amount of time to pause before printing next character
            colours (list [str | escape code]): Colour and formatting you want text to have

        Raises:
            Exception: Number of segments does not match strings, speeds or colours given
        """
        try:
            if len(range(segments)) != len(speeds):
                for i in range(segments):
                    for character in strings[i]:
                        stdout.write(f"{colours[i]}{character}\x1b[0m_")
                        stdout.write("\b \b")
                        stdout.flush()
                        sleep(speeds[0])
            else:
                for i in range(segments):
                    for character in strings[i]:
                        stdout.write(f"{colours[i]}{character}\x1b[0m_")
                        stdout.write("\b \b")
                        stdout.flush()
                        sleep(speeds[i])
        except:
            raise Exception("Number of segments does not match strings, speeds or colours given")
        
        sleep(0.1)               
    
    
    @staticmethod
    def clear_terminal():
        """clears the terminal of all previous output"""
        system('cls' if name == 'nt' else 'clear')
        
    @staticmethod
    def pause(seconds):
        """
        Pauses code for a specified amount of time.
        
        Args:
            seconds (float): number of seconds you want to pause code for.
        """
        sleep(seconds)
           
            
    @staticmethod
    def wait_for_enter():
        """
        Waits for enter key to be pressed before continuing execution of code.
        
        Does not actually pause code, only prints a blank input and waits for input to be submitted.
        """
        print("\n")
        sleep(0.06)
        GameCommand.sequential_print("Press ", 0.04, "")
        GameCommand.sequential_print("Enter ", 0.04, "\x1b[38;5;226m")
        GameCommand.sequential_print("to Continue", 0.04, "")
        input("\033[?25l")
        print('\033[?25h', end = '')
        
        
    @staticmethod
    def update_state():
        """
        Updates Game class variables.
        
        Updates:
        -------
            cave_inhabitant : Inhabitant residing in the current_cave.
            cave_item : Item contained in the current_cave.
            health : Limits health to below 100.
        """
        Game.cave_inhabitant = Game.current_cave.get_character()
        Game.cave_item = Game.current_cave.get_item()
        
        PlayerEntity.health = (PlayerEntity.health if PlayerEntity.health <= 100 else 100)
        
        
    @staticmethod
    def get_input():
        """
        Gets input from user, text of input is yellow.

        Returns:
            str: command inputted by user
        """
        command = str(input(">\x1b[38;5;226m ")).lower().strip()
        print('\x1b[0m', end="")
        return command
    
    
    @staticmethod
    def print_last_command(last_command):
        """
        Prints the last command the user has inputted with a faded look.

        Args:
            last_command (str): Last action the the user has inputted e.g. move.
        """
        if last_command is not None:
            print("\n\x1b[38;5;241m>\x1b[38;2;148;150;65m", last_command, "\x1b[0m")
        else:
            print("")  
            
    @staticmethod
    def check_win_condition():
        """
        Checks to see if the condition for winning or losing has been met for the chosen game mode

        Raises:
            Exception: no game mode set

        Returns:
            bool: returns false if win/lose condition is met else it returns True
        """
        match Game.game_mode:
            
            case "default":
                if Enemy.enemies_to_defeat == 0:
                    return False
                elif PlayerEntity.health <= 0:
                    PlayerEntity.dead = True
                    return False 
                else:
                    return True
                  
            case _:
                raise Exception("no game mode set")
    
    @staticmethod
    def print_game_over():
        GameCommand.clear_terminal()
        Title.output()
        match Game.game_mode:
            case "default":
                if PlayerEntity.dead == True:
                    GameCommand.sequential_print("YOU DIED", 0.1, "\x1b[38;5;196m")
                    sleep(0.2)
                    print("")
                    GameCommand.sequential_print("Better Luck Next Time", Config.standard_print_speed, Config.standard_text_colour)
                else:
                    GameCommand.sequential_print("CONGRATULATIONS!", 0.1, "\x1b[38;5;203m")
                    sleep(0.2)
                    print("")
                    GameCommand.sequential_print("You defeated all the enemies!", Config.standard_print_speed, Config.standard_text_colour)