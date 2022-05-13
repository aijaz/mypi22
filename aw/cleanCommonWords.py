import random

# read words from https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
with open("allcommonwords.txt") as f:
    words = f.read().splitlines()

with open("../dirtywords.txt") as f:
    dirtywords = f.read().splitlines()[0].split(", ")

print(f"Number of words is {len(words)}")
five_words = [word for word in words if len(word) == 5]
result = []
# print(words)

for word in five_words:
    if word.lower() in dirtywords:
        print(f"Dropping word: {word}")
    else:
        result.append(word)

print("----")
for w in result:
    print(w)

# print(dirtywords)

