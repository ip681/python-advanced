numbers_dictionary = {}

while True:
    line = input()

    if line == "Search":
        break

    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except:
        print("The variable number must be an integer")

while True:
    line = input()

    if line == "Remove":
        break

    searched = line

    if searched not in numbers_dictionary:
        print("Number does not exist in dictionary")
    else:
        print(numbers_dictionary[searched])

while True:
    line = input()

    if line == "End":
        break

    searched = line

    if searched not in numbers_dictionary:
        print("Number does not exist in dictionary")
    else:
        del numbers_dictionary[searched]

print(numbers_dictionary)
