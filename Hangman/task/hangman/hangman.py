import random
import hangman_functions

words = ("python", "java", "swift", "javascript")
correct_word = random.choice(words)
guesses = set()
attempts = 8
game_over = False

print(f"H A N G M A N # {attempts} attempts\n")

while attempts > 0 and not game_over:
    print(hangman_functions.show_hidden_word(correct_word, guesses))
    guess = input("Input a letter: ").lower()
    guesses.add(guess)
    attempts -= 1
    if len(guess) != 1 or guess not in correct_word:
        print(f"\nThat letter doesn't appear in the word.  # {attempts} attempts\n")
    elif guess in correct_word:
        print(f" # {attempts} attempts\n")
        # if set(guesses).issuperset(correct_word):
        #     game_over = True

print("Thanks for playing!")


