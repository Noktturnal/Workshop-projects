from random import randint

#greet the user for data collection
user_name = input("Welcome to LOTTO game! What is your name?: ")
print(f"Hello {user_name}!")

user_guess = []
#loop until user inputs all data in required format
while len(user_guess) < 6:
    number = int(input(f"Please enter a unique number in range 1 to 49 ({len(user_guess) +1} of 6): "))

    if number <1 or number > 49:
        print("Please enter a valid number.")
    elif number in user_guess:
        print("Please enter a unique number.")
    else:
        user_guess.append(number)

user_guess.sort()
print(f"{user_name} your guess was: {user_guess}")


computer_guess = []
while len(computer_guess) < 6:
    number = randint(1, 49)
    if number not in computer_guess:
        computer_guess.append(number)

# Convert lists to sets to find common elements
common_elements = set(computer_guess) & set(user_guess)

print(f"Computer draw: {sorted(computer_guess)}")
# Print common elements
print(f"Guessed numbers {len(common_elements)}: {sorted(common_elements)}")

# Check if all elements are the same
if set(computer_guess) == set(user_guess):
    print("LOTTO!")
