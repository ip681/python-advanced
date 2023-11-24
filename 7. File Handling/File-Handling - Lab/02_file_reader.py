def read_file_from_txt():
    with open("numbers.txt", "r") as file:
        result = sum([int(el.strip()) for el in file.readlines()])
        print(result)


read_file_from_txt()
