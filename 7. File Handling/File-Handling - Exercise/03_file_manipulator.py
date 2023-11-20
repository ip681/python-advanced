import os

"""Using this while debugging"""


# def read_file(path):
#     if os.path.exists(path):
#         with open(path, "r") as file:
#             open_file = file.readlines()
#             return open_file
#     return "Can't find the f..... file!"


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


def add_content(file_name, content):
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(f"{content}\n")
    else:
        create_file(file_name)
        with open(file_name, "a") as file:
            file.write(f"{content}\n")


def replace_string(file_name, old_string, new_string):
    if not os.path.exists(file_name):
        print("An error occurred")
    else:
        with open(file_name, "r") as file:
            text_rows = file.readlines()
            for row in range(len(text_rows)):
                if old_string in text_rows[row]:
                    text_rows[row] = text_rows[row].replace(old_string, new_string)
                    with open(file_name, "w") as new_file:
                        new_file.write(''.join(text_rows))


def delete_file(file_name):
    if not os.path.exists(file_name):
        print("An error occurred")
    else:
        os.remove(file_name)


def looping_thru_actions(command):
    actions = command.split("-")
    action = actions[0]
    file_name = actions[1]
    if action == "Create":
        create_file(file_name)
    elif action == "Add":
        content = actions[2]
        add_content(file_name, content)
    elif action == "Replace":
        old_string = actions[2]
        new_string = actions[3]
        replace_string(file_name, old_string, new_string)
    elif action == "Delete":
        delete_file(file_name)


def read_commands():
    while True:
        command = input()
        if command == "End":
            break

        looping_thru_actions(command)


read_commands()
