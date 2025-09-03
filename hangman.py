from random import choice
import pyfiglet
import string

MAX_INCORRECT_GUESSES = 6

# Selects a word from word.txt
def select_word():
    with open("word.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip().lower()

# Continuously prompts for valid input
def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if validate_input(player_input, guessed_letters):
            return player_input

# Validates user input
def validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )

# Joins guessed letters
def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))

# Builds the display word
def build_guessed_word(target_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in target_word])

# Draws the hangman ASCII art
def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
 ----- 
 |   | 
     | 
     | 
     | 
     | 
     | 
     | 
     | 
     | 
------- 
""",
        r"""
 ----- 
 |   | 
 O   | 
     | 
     | 
     | 
     | 
     | 
     | 
     | 
------- 
""",
        r"""
 ----- 
 |   | 
 O   | 
 |   | 
 |   | 
     | 
     | 
     | 
     | 
------- 
""",
        r"""
 ----- 
 |   | 
 O   | 
/|   | 
 |   | 
     | 
     | 
     | 
     | 
------- 
""",
        r"""
 ----- 
 |   | 
 O   | 
/|\  | 
 |   | 
     | 
     | 
     | 
     | 
------- 
""",
        r"""
 ----- 
 |   | 
 O   | 
/|\  | 
 |   | 
/     | 
|     | 
     | 
------- 
""",
        r"""
 ----- 
 |   | 
 O   | 
/|\  | 
 |   | 
/ \  | 
| |  | 
     | 
------- 
"""
    ]
    print(hanged_man[wrong_guesses])

# Checks for game-over condition
def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if all(letter in guessed_letters for letter in target_word):
        return True
    return False

# Main function
def play_game():
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0

    print(pyfiglet.figlet_format("Welcome to Hangman!", font="slant"))
    print("=======================================================")

    while not game_over(wrong_guesses, target_word, guessed_letters):
        print(f"\nYour word is: {guessed_word}")
        print(f"Guessed letters: {join_guessed_letters(guessed_letters)}")
        print(f"Wrong guesses left: {MAX_INCORRECT_GUESSES - wrong_guesses}")
        draw_hanged_man(wrong_guesses)
        print("*******************************************************")

        player_guess = get_player_input(guessed_letters)

        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

        player_guess_word = input("\nWant to guess the full word? (Press Enter to skip): ").lower()
        if player_guess_word:
            if player_guess_word == target_word:
                break
            else:
                print("Wrong guess! Game over.")
                wrong_guesses = MAX_INCORRECT_GUESSES
                break

    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print(pyfiglet.figlet_format("You Lost! Try again next time", font="slant", width=100))
    else:
        print(pyfiglet.figlet_format("You Won!", font="slant", width=100))

    print(f"\nThe correct word was: {target_word}")

if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("Thanks for playing Hangman! Goodbye!")
            break
