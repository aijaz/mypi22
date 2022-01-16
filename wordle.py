import random

# read words from https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
with open("commonwords.txt") as f:
    words = f.read().splitlines()

print(f"Number of words is {len(words)}")
five_letter_words = [word for word in words if len(word) == 5]
print(f"Number of five-letter words is {len(five_letter_words)}")

random_index = random.randrange(0, len(five_letter_words))

random_word = five_letter_words[random_index].upper()

num_guesses = 0
max_guesses = 6

history = []
random_word = 'SOLVE'

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
    colors = [guess, " "]

    if guess == random_word:
        print("Correct!")
        colors.extend(["🟩", "🟩", "🟩", "🟩", "🟩"])
        history.append(colors)
        for item in history:
            print("".join(item))
        break
    else:
        characters = [char for char in guess]
        for index, character in enumerate(characters):
            if random_word[index] == character:
                colors.append("🟩")
            elif character in random_word:
                colors.append("🟧")
            else:
                colors.append("⬛")
        history.append(colors)
        for item in history:
            print("".join(item))

