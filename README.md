# Turtle Racing Game (Python Turtle)

This repository contains a colourful turtle racing game built in Python using the built‑in `turtle` graphics module. After learning core ideas from earlier snake and pong games, this project was designed and implemented independently from scratch to practise structuring a complete mini‑game, handling user input, and working with simple randomness.[file:312]

---

## Game Overview

- Six turtles in different colours line up at the left side of the screen.
- The player places a bet by entering a colour in a text input box.
- Once the race starts, all turtles move forward by random amounts each step.
- The first turtle to cross the finish line on the right wins.
- The program prints whether the player’s chosen turtle won or lost.[file:312]

---

## File Structure

- `main.py`  
  - Sets up the screen size and title using `turtle.Screen()`.  
  - Prompts the player for a bet using a text input dialog (`screen.textinput`).  
  - Defines the list of turtle colours and their starting y‑positions.  
  - Creates six `Turtle` objects, one for each colour, positions them at the starting line, and stores them in a list.  
  - Runs the main race loop:
    - Each turtle moves forward by a random distance on each iteration.
    - Checks if any turtle has crossed the finish line.
    - Determines the winning turtle’s colour and compares it to the user’s bet.
    - Prints a win/lose message to the console, then stops the race.[file:312]  
  - Keeps the window open until the user clicks inside it (`screen.exitonclick()`).

There are no additional modules; the entire game logic is contained in `main.py` for simplicity.[file:312]

---

## Controls and Gameplay

1. When you run the game, a dialog asks:

   > “Which turtle will win the race? Enter a color:”

2. Type one of the available colours:
   - `red`, `orange`, `yellow`, `green`, `blue`, or `purple`.  
3. The race begins automatically and the turtles move forward with random step sizes.
4. When a turtle crosses the finish line, the program prints whether your chosen colour won or lost.[file:312]

---

## Requirements

- Python 3.10 or higher.
- Desktop environment that supports the built‑in `turtle` graphics window.
- No external libraries are required (`turtle` and `random` are from the standard library).[file:312]

---

## How to Run

1. Place `main.py` in a folder of your choice.
2. Open a terminal or command prompt in that folder.
3. Run:
4. Enter your colour bet in the dialog and watch the race

# Possible Extensions
Some ideas to extend this project:
Add multiple rounds and keep track of the number of wins for the player.
Draw a visible finish line and track lanes for each turtle.
Display the winning colour and result on the screen instead of only printing to the console.
Add simple sound effects or animations when a winner is declared.

This project serves as a self‑built step after earlier guided games, showing independent use of turtle, loops, and randomness to create a complete interactive mini‑game.
