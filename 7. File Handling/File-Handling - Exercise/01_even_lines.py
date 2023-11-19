import re


def replace_punctuation(row):
    return re.sub(r"[.\,\!\?-]", "@", row)


def print_even_lines():
    with open("text.txt", "r") as file:
        rows = file.readlines()
        for row in range(len(rows)):
            if row % 2 == 0:
                replaced = replace_punctuation(rows[row]).split()
                print(" ".join(replaced[::-1]))


print_even_lines()
