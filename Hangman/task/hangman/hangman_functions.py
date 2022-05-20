def show_hidden_word(correct_word, guesses):
    hidden_word = []
    for index in range(len(correct_word)):
        if correct_word[index] not in guesses:
            hidden_word.append("-")
        else:
            hidden_word.append(correct_word[index])
    return "".join(hidden_word)
