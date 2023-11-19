def repeat_text(txt, cnt):
    return txt * int(cnt)


text = "Hello"
count = "asd"  # "asd"

try:
    print(repeat_text(text, count))
except ValueError:
    print("Variable times must be an integer")
