from random import randint

# Computer selects a random number between 1 and 100
computer_guess = randint(1, 100)

while True:
    try:
        # Ask the player to guess the number
        player_guess = int(input("Guess the number: "))
    except ValueError:
        # If the input is not a number, display an error message
        print("It's not a number!")
        continue  # Return to point 1

    # Compare player's guess with the computer's number
    if player_guess < computer_guess:
        print("Too small!")
    elif player_guess > computer_guess:
        print("Too big!")
    else:
        print("You win!")
        break  # Terminate the program
