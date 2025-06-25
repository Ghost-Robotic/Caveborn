from os import system, name
from time import sleep
from sys import stdout
from random import randint, choice

class Command():         
            
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
        
        The position of each speed and colour in their respective list will correspond to the position of each item in the strings list unless.

        Args:
            segments (int): Number of string segments to be printed
            strings (list [str]): String to be printed list
            speeds (list [float]): Amount of time to pause before printing next character, if only one speed is given all segments will print at the same speed 
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
        Command.sequential_print("Press ", 0.02, "")
        Command.sequential_print("Enter ", 0.02, "\x1b[38;5;226m")
        Command.sequential_print("to Continue", 0.02, "")
        input("\033[?25l")
        print('\033[?25h', end = '')
                
        
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
    def random_dict_key(dictionary):
        return choice(list(dictionary.keys()))
    
    @staticmethod
    def random_range(a, b):
        return randint(a, b)
    
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False