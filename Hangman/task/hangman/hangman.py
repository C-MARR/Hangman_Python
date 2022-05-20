import random

print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
correct_word = random.choice(words)
guess = input("Guess the word: ")
print("You survived!" if guess == correct_word else "You lost!")
