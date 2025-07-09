# Caveborn

## Description
You are a child who has been living in Solace for your whole life. Your parents disappeared when you were younger and you have no recollection of them. Now, after 20 years, you feel curious about your past and what lies beyond the complex cave system that you are trapped in.

However, as you find your way out, you will meet many formidable foes, determined to stop you in your tracks. You must find powerful weapons to continue your fight for freedom.

Do you think you have a shot?

## Game Modes
### Default
- In the default game mode you must defeat all enemies to win the game

## How to play

### The Compass
<img src="assets\example_compass.PNG" alt="Image showing what the compass looks like in-game.">

The cardinal directions with red text indicates the directions the player is able to move.  
(e.g. In the image above; North, East and West are the directions the player is able to move)

### Player Information Popup
<img src="assets\example_display.PNG" width="385px" alt="Image showing how player information is show in-game.">   

This area of the display shows import player information such as your health and the items currently in your bag

<img src="assets\bag_example.PNG" width = "385px" alt="Image highlighting location of player bag with example items">

The items you pick up you appear here with their durability displayed next to the item name. Items with infinite durability have the ∞ symbol!

<img src="assets\enemies_to_defeat.PNG" width = "385px" alt="Image highlighting location of enemy counter">

The number of enemies left is displayed here

### Tips
- Talk!!! you may find some useful information
- Healing does not count as a turn so heal as much as you want
- If you are about to die you can always retreat

## Game Mechanics
### Attacking Enemies
When using items to attack enemies you have equal chances of rolling a weak attack, strong attack or a critical hit. A weak attack is -30% of the item's base damage, a strong attack is the same as the base damage and a critical hit is +30% of base damage.

### Healing
You may only heal during a fight but healing does not count as a turn so you can heal as many times as you want!

## Available Commands
* __north, south, east, west__: move the player in the cardinal directions
* __take__: places the item located in the current cave in the players bag
* __fight__: fight the current inhabitant of the cave is enemy with a chosen item
* __trade__: if the current inhabitant of the cave is a trader you can give it an item in your bag in exchange for a different item
* __talk__: talk with the current inhabitant of the cave
* __pat__: pat the current inhabitant of the cave
* __retreat__: allows you to escape from a fight
* __about <character/item name>__: displays a description of the item/character
* __exit__: closes the game
