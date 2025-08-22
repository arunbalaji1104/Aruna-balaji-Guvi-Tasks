import random

# List of words for the game
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Pick a random word from the list
original_word = random.choice(words)

# Scramble the word by shuffling its letters
letters = list(original_word)      # Turn the word into a list of letters
random.shuffle(letters)            # Shuffle the letters randomly
scrambled_word = ''.join(letters)  # Join the shuffled letters back into a string

print("Welcome to the Word Scramble Game!")
print("Unscramble this word:", scrambled_word)

attempts = 0  # Counts the number of guesses
guess = ""    # Stores the player's guess

# Loop until the player guesses the word correctly
while guess != original_word:
    guess = input("Your guess: ").strip()  # Get the player's guess and remove whitespace
    attempts += 1

    # Check if the guess matches the original word
    if guess == original_word:
        print("Congratulations! You unscrambled the word in", attempts, "tries.")
    else:
        print("Wrong guess, try again.")

# The game ends when the correct word is guessed.