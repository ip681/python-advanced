import re


def get_file_content(path):
    with open(path, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


def count_words(words, text):
    res = {}
    for word in words:
        if word in text:
            res[word] = text.count(word)
    return res


def sort_result(res):
    sorted_result = sorted(res.items(), key=lambda x: -x[1])
    return sorted_result


def print_result(res):
    for key, val in res:
        print(f"{key} - {val}")


path_to_words = "words.txt"
path_to_text = "text.txt"

words_file = get_file_content(path_to_words)
text_file = get_file_content(path_to_text)
result = sort_result(count_words(words_file, text_file))
print_result(result)
