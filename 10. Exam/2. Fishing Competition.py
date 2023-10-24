def is_valid_position(row, col, matrix_size):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def move_ship(row, col, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1

#num
n = int(input())
fishing_area = []
ship_row, ship_col = 0, 0
fish_caught = 0

for row in range(n):
    line = input()
    fishing_area.append(list(line))
    if 'S' in line:
        ship_row, ship_col = row, line.index('S')

commands = []
while True:
    command = input()
    if command == "collect the nets":
        break
    commands.append(command)

for command in commands:
    fishing_area[ship_row][ship_col] = '-'
    new_row, new_col = move_ship(ship_row, ship_col, command)

    if not is_valid_position(new_row, new_col, n):
        if command == "up":
            new_row = n - 1
        elif command == "down":
            new_row = 0
        elif command == "left":
            new_col = n - 1
        elif command == "right":
            new_col = 0

        ship_row, ship_col = new_row, new_col

    element = fishing_area[new_row][new_col]
    if isinstance(element, list):
        element = ''.join(element)

    if str(element).isdigit():
        fish_caught += int(element)
        fishing_area[new_row][new_col] = '-'

    if fishing_area[new_row][new_col] == 'W':
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_row},{new_col}]")
        exit()

    ship_row, ship_col = new_row, new_col
    fishing_area[ship_row][ship_col] = 'S'

if fish_caught >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")

if fish_caught>0:
    print(f"Amount of fish caught: {fish_caught} tons.")

# print(f"Amount of fish caught: {fish_caught} tons.")
for row in fishing_area:
    print(''.join(row))


# def is_inside(matrix_size, r, c):
#     return 0 <= r < matrix_size and 0 <= c < matrix_size
#
#
# def move_ship(matrix, row, col, command):
#     matrix[row][col] = '-'
#     if command == "up":
#         row -= 1
#     elif command == "down":
#         row += 1
#     elif command == "left":
#         col -= 1
#     elif command == "right":
#         col += 1
#
#     if not is_inside(len(matrix), row, col):
#         if row == -1:
#             row = len(matrix) - 1
#         elif row == len(matrix):
#             row = 0
#         if col == -1:
#             col = len(matrix) - 1
#         elif col == len(matrix):
#             col = 0
#
#     return row, col
#
#
# n = int(input())
# matrix = [list(input()) for _ in range(n)]
#
# ship_row, ship_col = None, None
# for r in range(n):
#     for c in range(n):
#         if matrix[r][c] == 'S':
#             ship_row, ship_col = r, c
#             break
#
# fish_caught = 0
# while True:
#     command = input()
#     if command == "collect the nets":
#         break
#
#     ship_row, ship_col = move_ship(matrix, ship_row, ship_col, command)
#
#     if matrix[ship_row][ship_col] == 'W':
#         print(
#             f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship_row},{ship_col}]")
#         exit()
#
#     if matrix[ship_row][ship_col].isdigit():
#         fish_caught += int(matrix[ship_row][ship_col])
#         matrix[ship_row][ship_col] = '-'
#
#     matrix[ship_row][ship_col] = 'S'
#
# if fish_caught < 20:
#     print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")
# elif fish_caught >= 20:
#     print("Success! You managed to reach the quota!")
#
# if fish_caught > 0:
#     print(f"Amount of fish caught: {fish_caught} tons.")
#
# for row in matrix:
#     print(''.join(row))