print("Think about a number between 1 and 1000, and let me guess it! Hit enter to continue!")
input()

# Initialize the range for guessing
min_value = 1
max_value = 1000

user_input = ""
while user_input != "you won":
    # Calculate the guess
    guess = (min_value + max_value) // 2
    print(f"Guessing: {guess}")

    # Get the user's feedback
    user_input = input("Is my guess too high, too low, or did I win? ").strip().lower()

    if user_input == "too high":
        max_value = guess - 1
    elif user_input == "too low":
        min_value = guess + 1
    elif user_input == "you won":
        print("Great, humanity will never win against silicon!")
    else:
        print("Please enter 'too high', 'too low', or 'you won'.")
