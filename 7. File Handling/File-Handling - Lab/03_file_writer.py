def create_write_file():
    with open("my_first_file.txt", "w") as file:
        file.write("I just created my first file!")
    # with open("my_first_file.txt", "a") as file:
    #     file.write("This is my second row\n")
    #     file.write("And this is the third one\n")


create_write_file()
