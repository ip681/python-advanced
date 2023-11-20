from string import punctuation
from string import ascii_letters


def read_file_content():
    with open("text.txt", "r") as file:
        return file.readlines()


def find_punctuations(txt):
    return [ch for ch in txt if ch in punctuation]


def find_letters(txt):
    return [ch for ch in txt if ch in ascii_letters]


def print_result():
    file_content = read_file_content()

    counter = 1
    for row in file_content:
        punctuations = find_punctuations(row)
        letters = find_letters(row)
        print(f"Line {counter}: {row[:-1]} ({len(letters)})({len(punctuations)})")
        counter += 1


print_result()
