import random

# read words from https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
with open("words.txt") as f:
    words = f.read().splitlines()

with open("dirtywords.txt") as f:
    dirtywords = f.read().splitlines()[0].split(", ")

print(f"Number of words is {len(words)}")
five_or_less_letter_words = [word for word in words if 3 <= len(word) <= 5]
print(f"Number of five_or_less_letter_words words is {len(five_or_less_letter_words)}")

five_words = [word for word in words if len(word) == 5]
result = []
# print(words)

for word in five_words:
    if word.lower() == 'fucks':
        print("Found fucks")
    if word.lower() in dirtywords:
        print(f"Dropping word: {word}")
    else:
        result.append(word)

print(f"Number of result words is {len(result)}")

result_to_print = [f"'{word}'" for word in result]
print(f"words = [{','.join(result_to_print)}]")

# print(dirtywords)

