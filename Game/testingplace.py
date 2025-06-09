from src.entities.Player import Player
from config import Config
from commands.game_commands import GameCommand
from commands.player_commands import PlayerCommand

Config.initialise()

GameCommand.update_state()
Player.damage(50)
GameCommand.update_state()
Player.heal(20)
GameCommand.update_state()
Player.heal(100)
GameCommand.update_state()
Player.damage(101)
GameCommand.update_state()

if Player.dead == True:
    print("dead")
    
print(" _ ")
print("|2|")
print(" ‾ ")



