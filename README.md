# Battleships
## Battleships computer game

Battleship is a computer game written in python in console interface.

## How to play

Player after inserted his name can start the game against the computer. The goal is to guess oponents ships positions. 
Game is going in rounds. The rules are listed [here](https://en.wikipedia.org/wiki/Battleship_(game)): 

## Features

- Board generation. Random for player and computer.
- Playing against computer
- Validating user input
- Displays current scores
- Maintaining history of moves
- Displaying winner of the game


## Future Features

- Allow player to select board size and number of ships
- Allow player to position ships themselves
- Have ships larger than 1x1

## Data model

The ships and board fields are in twodimensional list of numbers and empty field is represented by 0 and ship is
represented by 1. In console field is represented by '.' char and ship is represented by '@' char.

## Functions 

- generate_arr - generate array with 4 ships in random places
- display_arr - print the board on the screen function
- hit - hit opponents board function
- check if board contains only zeros function
- check_coords - check if coordinates are valid and they are not in history already function


## Bugs

- History of moves was not stored correct, we changed the way to store every single move to store it in list in a numbers tuple with number of row and number of columns 
- after players guess there was an error if the coordinates were outside the board. We fixed it with validation function and while loop allowing the player to enter coordinates once again.

## Remaining Bugs 
- No Bugs remaining






