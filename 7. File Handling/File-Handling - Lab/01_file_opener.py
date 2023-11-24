def open_file(file_name):
    try:
        with open(file_name, "r") as file:
            print("File found")
    except FileNotFoundError:
        print("File not found")


searched_name = "text.txt"
open_file(searched_name)
