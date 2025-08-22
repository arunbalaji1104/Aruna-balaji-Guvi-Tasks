import random
def guess_the_number():
    """
    This function runs the 'Guess the Number' game.
    The computer randomly selects a number from 1 to 10.
    The player tries to guess it with hints.
    """

    # The number to guess (random from 1 to 10)
    secret_number = random.randint(1, 10)
    guess = None  # Initialize player's guess
    attempts = 0  # Count the number of guesses

    print("Welcome to Guess the Number!")
    print("I have chosen a number between 1 and 10.")

    # Loop until the player guesses the correct number
    while guess != secret_number:
        player_input = input("Enter your guess: ")  # Read player input (string)

        # Check if input contains only digits (string manipulation for validation)
        if not player_input.isdigit():
            print("Invalid input, please enter a number.")
            continue  # If invalid, repeat the loop without counting this guess

        # Convert input string to integer type
        guess = int(player_input)
        attempts += 1  # Increment attempts counter

        # Conditions to check player's guess
        if guess < secret_number:
            print("Your guess is too low. Try again.")
        elif guess > secret_number:
            print("Your guess is too high. Try again.")

    # When the correct guess is made
    print(
        "Congratulations! You guessed the number "
        + str(secret_number)
        + " in "
        + str(attempts)
        + " tries."
    )


if __name__ == "__main__":
    guess_the_number()