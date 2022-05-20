import random
import hangman_functions


def menu(attempts):
    wins = 0
    loses = 0
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        option = input()
        if option == "play":
            if play(attempts):
                wins += 1
            else:
                loses += 1
        elif option == "results":
            hangman_functions.show_results(wins, loses)
        elif option == "exit":
            break


def play(_attempts):
    words = ("python", "java", "swift", "javascript")
    correct_word = random.choice(words)
    guesses = set()
    game_over = False
    while _attempts > 0 and not game_over:
        print("\n" + hangman_functions.show_hidden_word(correct_word, guesses))
        guess = input("Input a letter: ")
        if not guess.islower() and len(guess) == 1:
            print("Please, enter a lowercase letter from the English alphabet.")
        elif len(guess) != 1:
            print("Please, input a single letter")
        else:
            if guess in guesses:
                print("You've already guessed this letter.")
            elif guess not in correct_word:
                guesses.add(guess)
                _attempts -= 1
                print(f"That letter doesn't appear in the word.  # {_attempts} attempts")
            elif guess in correct_word and guess not in guesses:
                guesses.add(guess)
                if set(guesses).issuperset(correct_word):
                    game_over = True
                    print(f"You guessed the word {correct_word}!")

    if _attempts > 0:
        print("You survived!")
        return True
    else:
        print("\nYou lost!")
        return False


print(f"H A N G M A N # 8 attempts")
menu(8)


