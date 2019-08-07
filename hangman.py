import random

# Introduction to the game.
print("Welcome to Hangman! You will be given a category that your word falls under. You have a limited amount of guesses and with each incorrect guess, the man will lose a body part.\n")

# Possible categories.
categories = ["MOVIES", "CANDY", "COUNTRIES",
              "FRUITS", "VEGETABLES", "GAMES", "CELEBRITIES"]
category = random.randint(0, 6)
chosen_category = categories[category]
print("Your category is", chosen_category, "\n")

# Possible words from each category.
chosen_list = []
if chosen_category == "COUNTRIES":
    chosen_list = ["CANADA", "ITALY", "GERMANY", "INDIA", "CHINA"]
elif chosen_category == "CANDY":
    chosen_list = ["TWIX", "BUTTERFINGER", "LOLLIPOP", "LICORICE", "PEZ"]
elif chosen_category == "MOVIES":
    chosen_list = ["DEADPOOL", "TWILIGHT", "LOGAN", "CINDERELLA", "JUMANJI"]
elif chosen_category == "FRUITS":
    chosen_list = ["STRAWBERRY", "ORANGE", "APPLE", "PEACH", "GRAPE"]
elif chosen_category == "VEGETABLES":
    chosen_list = ["CELERY", "LETTUCE", "POTATO", "ONION", "GARLIC"]
elif chosen_category == "GAMES":
    chosen_list = ["FORTNITE", "CALL OF DUTY", "ZELDA", "SUPER MARIO", "SONIC"]
else:
    chosen_list = ["JUSTIN BIEBER", "CHANNING TATUM",
                   "JOHNNY DEPP", "JUSTIN TIMBERLAKE", "ARIANA GRANDE"]

# This is the hangman itself.
full = " _________\n|         |\n|         O\n|        /|\\ \n|        / \\ \n|"
leftLeg = " _________\n|         |\n|         O\n|        /|\\ \n|        / \n|"
rightArm = " _________\n|         |\n|         O\n|        /|\\ \n| \n|"
leftArm = " _________\n|         |\n|         O\n|        /|  \n| \n|"
torso = " _________\n|         |\n|         O\n|         |  \n| \n|"
head = " _________\n|         |\n|         O\n| \n| \n|"
empty = " _________\n|         |\n| \n| \n| \n|"

hangman = [empty, head, torso, leftArm, rightArm, leftLeg, full]

# This shows the user the amount of letters in the word without disclosing them.
word = random.choice(chosen_list)
length = len(word)
underscores = "_" * length

# This allows spaces to be shown.
while " " in word:
    index = word.index(" ")
    underscores = underscores[:index] + " " + underscores[index + 1:]

hangmanIndex = 0

# In order to keep track of letters incorrectly guessed:
incorrectGuesses = "Incorrect guesses so far: "

# This allows the user to guess letters:
while (hangmanIndex < len(hangman) - 1):
    print(hangman[hangmanIndex])
    print(incorrectGuesses)
    print("\nWord:", underscores)

# When the user has won:
    if "_" not in underscores:
        break
    guess = input("Guess one of the letters: ")
    guess = guess.upper()
    if guess in word:
        print("\nYou guessed correctly.")
        for i in range(len(word)):
            if word[i] == guess:
                underscores = underscores[:i] + guess + underscores[i + 1:]
    else:
        print("\nYou guessed incorrectly.")
        incorrectGuesses += guess + " "
        hangmanIndex += 1

# When the user has lost:
if ("_" in underscores):
    print(hangman[hangmanIndex])
    print("\nYou lost! The correct word was:", word)
else:
    print("You won!")
