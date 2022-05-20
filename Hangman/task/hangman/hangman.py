import random
import hangman_functions

words = ("python", "java", "swift", "javascript")
correct_word = random.choice(words)
guesses = set()
attempts = 8
game_over = False

print(f"H A N G M A N # {attempts} attempts")

while attempts > 0 and not game_over:
    print("\n" + hangman_functions.show_hidden_word(correct_word, guesses))
    guess = input("Input a letter: ")
    if not guess.islower() and len(guess) == 1:
        print("Please, enter a lowercase letter from the English alphabet.")
    elif len(guess) != 1:
        print("Please, input a single letter")
    else:
        if guess in correct_word and guess in guesses:
            print("You've already guessed this letter.")
        elif guess not in correct_word:
            guesses.add(guess)
            attempts -= 1
            print(f"That letter doesn't appear in the word.  # {attempts} attempts")
        elif guess in correct_word and guess not in guesses:
            guesses.add(guess)
            if set(guesses).issuperset(correct_word):
                game_over = True
                print(f"You guessed the word {correct_word}!")

print("You survived!" if attempts > 0 else "\nYou lost!")


