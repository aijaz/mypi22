import wordle

words = wordle.read_dictionary()
word_length = 5
random_word = wordle.get_random_word(words, word_length)
num_guesses = wordle.run(random_word, max_guesses=word_length + 1, word_length=word_length)

if num_guesses is None:
    print(f"Sorry, you have run out of guesses. The correct word is: {random_word}")
    exit(1)

responses = ['Did you cheat?', 'Incredible!', 'Impressive', 'Not bad!', 'Nicely done!', 'Phew.']
if num_guesses <= 6:
    print(responses[num_guesses - 1])
else:
    print("Correct!")

exit(0)