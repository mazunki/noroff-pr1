dictionary = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

examples = ["one", "two", "three"]
translated = []
for item_to_translate in examples:
    for original, new in dictionary.items():
        if item_to_translate == original:
            translated.append(new)
print(translated)
