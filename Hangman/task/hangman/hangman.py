import random

print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
correct_word = random.choice(words)
hidden_word = []
for char in range(len(correct_word)):
    if char > 2:
        hidden_word.append("-")
    else:
        hidden_word.append(correct_word[char])
guess = input(f'Guess the word: {"".join(hidden_word)}')
print("You survived!" if guess == correct_word else "You lost!")
