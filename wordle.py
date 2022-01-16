import random

# read words from https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
# or from https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/


def process_guess(guess, word):
    """
    Compares guess to word
    :param guess: the word that the user guessed
    :param word: the solution for the puzzle
    :return: a tuple: match: a boolean representing a match,
                      history_item: a list containing the guess and the colors associated with the guess
    """

    match = True
    characters = [char for char in guess]
    colors = []
    for index, character in enumerate(characters):
        try:
            if word[index] == character:
                colors.append("🟩")
            elif character in random_word:
                colors.append("🟧")
                match = False
            else:
                colors.append("⬛")
                match = False
        except IndexError:
            colors.append("⬛")
            match = False

    return match, colors


def run(word, max_guesses):

    history = []
    num_guesses = 0

    while True:
        if num_guesses > max_guesses:
            print(f"Sorry, you have run out of guesses. The correct word is: {random_word}")
            break

        print("----------------------------------------")

        guess = input(f"Your Guess: ").upper()
        if len(guess) != 5:
            print("5-letter words only.")
            continue

        num_guesses += 1
        match, colors = process_guess(guess, word)
        history.append(colors)

        for item in history:
            print("".join(item))

        if match:
            print("Correct!")


if __name__ == '__main__':
    with open("commonwords.txt") as f:
        words = f.read().splitlines()

    five_letter_words = [word for word in words if len(word) == 5]
    
    random_index = random.randrange(0, len(five_letter_words))
    random_word = five_letter_words[random_index].upper()

    run('PANIC', max_guesses=6)
