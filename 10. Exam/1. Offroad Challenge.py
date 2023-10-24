# initial_fuel = list(map(int, input().split()))
# consumption_index = list(map(int, input().split()))
# needed_fuel = list(map(int, input().split()))
#
# reached_altitudes = []
#
# #t
# for i in range(len(needed_fuel)):
#     available_fuel = initial_fuel[-1] - consumption_index[0]
#
#     if available_fuel >= needed_fuel[i]:
#         print(f"John has reached: Altitude {i+1}")
#         reached_altitudes.append(i+1)
#         initial_fuel.pop()
#         consumption_index.pop(0)
#     else:
#         print(f"John did not reach: Altitude {i+1}")
#         break
#
# if not needed_fuel:
#     print("John has reached all the altitudes and managed to reach the top!")
# else:
#     if reached_altitudes:
#         print("John failed to reach the top.")
#         print("Reached altitudes:", end=' ')
#         print(*[f"Altitude {alt}" for alt in reached_altitudes], sep=', ')
#     else:
#         print("John failed to reach the top.")
#         print("John didn't reach any altitude.")

from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())

reached_altitudes = []

while initial_fuel and additional_consumption_index:
    current_fuel = initial_fuel.pop()
    current_index = additional_consumption_index.popleft()
    current_fuel_needed = amount_of_fuel_needed.popleft()
    current_result = current_fuel - current_index

    altitude_number = len(reached_altitudes) + 1

    if current_result >= current_fuel_needed:
        reached_altitudes.append(altitude_number)
        print(f"John has reached: Altitude {altitude_number}")
    else:
        print(f"John did not reach: Altitude {altitude_number}")
        break

if len(reached_altitudes) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print(f"John failed to reach the top.")
    if reached_altitudes:
        altitudes_str = ", ".join([f"Altitude {alt}" for alt in reached_altitudes])
        print(f"Reached altitudes: {altitudes_str}")
    else:
        print("John didn't reach any altitude.")
