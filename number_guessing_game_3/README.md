# Reverse Number Guessing Game

## Description

This is a web-based reverse number guessing game built with the Flask framework. In this game, the computer tries to guess a number you have in mind within a range of 1 to 1000. You provide feedback on each guess, indicating whether it is too high, too low, or correct. The game continues until the computer correctly guesses your number.

## How to Play

1. **Start the Game**: Run the Flask application.
2. **Think of a Number**: Choose a number between 1 and 1000 but keep it secret.
3. **Interact with the Game**:
   - The web page will display the current guess of the computer.
   - Use the buttons to provide feedback:
     - Click `Too small` if the guess is lower than your number.
     - Click `Too big` if the guess is higher than your number.
     - Click `You win` if the guess is correct.
4. **Continue**: The computer will adjust its guesses based on your feedback until it guesses the correct number.

## Features

- **Binary Search Algorithm**: Efficiently narrows down the possible number range.
- **Interactive Feedback**: Real-time adjustment of guesses based on user input.
- **User-Friendly Interface**: Simple buttons for providing feedback.

## Example Usage

1. Start the Flask application by running `python app.py` in your terminal.
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. Think of a number between 1 and 1000.
4. Use the provided buttons to give feedback on the computer's guesses.

## Prerequisites

- Python 3.12 or higher

## How to Run

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Save the script as `guessing_game.py`.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the command:

   ```bash
   python guessing_game.py
   ```
   
### AUTHOR 
# NOKTTURNAL

   ```bash

⠀⠀⠀⠀⠀⣀⣠⠤⠶⠶⣖⡛⠛⠿⠿⠯⠭⠍⠉⣉⠛⠚⠛⠲⣄⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠋⠁⠀⡉⠁⢐⣒⠒⠈⠁⠀⠀⠀⠈⠁⢂⢅⡂⠀⠀⠘⣧⠀⠀⠀⠀
⠀⠀⣼⠀⠀⠀⠁⠀⠀⠀⠂⠀⠀⠀⠀⢀⣀⣤⣤⣄⡈⠈⠀⠀⠀⠘⣇⠀⠀⠀
⢠⡾⠡⠄⠀⠀⠾⠿⠿⣷⣦⣤⠀⠀⣾⣋⡤⠿⠿⠿⠿⠆⠠⢀⣀⡒⠼⢷⣄⠀
⣿⠊⠊⠶⠶⢦⣄⡄⠀⢀⣿⠀⠀⠀⠈⠁⠀⠀⠙⠳⠦⠶⠞⢋⣍⠉⢳⡄⠈⣧
⢹⣆⡂⢀⣿⠀⠀⡀⢴⣟⠁⠀⢀⣠⣘⢳⡖⠀⠀⣀⣠⡴⠞⠋⣽⠷⢠⠇⠀⣼
⠀⢻⡀⢸⣿⣷⢦⣄⣀⣈⣳⣆⣀⣀⣤⣭⣴⠚⠛⠉⣹⣧⡴⣾⠋⠀⠀⣘⡼⠃
⠀⢸⡇⢸⣷⣿⣤⣏⣉⣙⣏⣉⣹⣁⣀⣠⣼⣶⡾⠟⢻⣇⡼⠁⠀⠀⣰⠋⠀⠀
⠀⢸⡇⠸⣿⡿⣿⢿⡿⢿⣿⠿⠿⣿⠛⠉⠉⢧⠀⣠⡴⠋⠀⠀⠀⣠⠇⠀⠀⠀
⠀⢸⠀⠀⠹⢯⣽⣆⣷⣀⣻⣀⣀⣿⣄⣤⣴⠾⢛⡉⢄⡢⢔⣠⠞⠁⠀⠀⠀⠀
⠀⢸⠀⠀⠀⠢⣀⠀⠈⠉⠉⠉⠉⣉⣀⠠⣐⠦⠑⣊⡥⠞⠋⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠒⠈⠁⣀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠶⢤⣤⣤⣤⣤⡤⠴⠖⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ```