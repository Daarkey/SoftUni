"""1. Zeros to Back"""

# numbers = [int(i) for i in input().split(', ')]

# for i in numbers:
#     if i == 0:
#         numbers.remove(i)
#         numbers.append(i)

# print(numbers)


"""2. Messaging"""
# numbers = [int(i) for i in input().split('')]
# string_input = input()


"""3. Car Race"""


"""4. Josephus Permutation"""
# num_of_people = input().split(' ')
# k = int(input())

# dead_people = []
# counter = 0
# index = 0

# while len(num_of_people) > 0:
#     counter += 1

#     if counter % k == 0:
#         dead = num_of_people.pop(index)
#         dead_people.append(dead)

#     else:
#         index += 1

#     if index >= len(num_of_people):
#         index = 0

# print(str(dead_people).replace(' ', '').replace('\'', ''))


"""5. Tic-Tac-Toe"""
# first_line = [int(i) for i in input().split(' ')]
# second_line = [int(i) for i in input().split(' ')]
# third_line = [int(i) for i in input().split(' ')]

# count_1 = 0
# count_2 = 0

# for el in first_line:
#     if el == 1:
#         count_1 += 1
#     elif el == 2:
#         count_2 += 1

# for el in second_line:
#     if el == 1:
#         count_1 += 1
#     elif el == 2:
#         count_2 += 1

# for el in third_line:
#     if el == 1:
#         count_1 += 1
#     elif el == 2:
#         count_2 += 1

# if count_1 > count_2:
#     print("First player won")
# elif count_1 < count_2:
#     print("Second player won")
# elif count_1 == count_2:
#     print("Draw!")
