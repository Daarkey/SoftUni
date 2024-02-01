#1

# numbers = [int(i) for i in input().split(', ')]

# for i in numbers:
#     if i == 0:
#         numbers.remove(i)
#         numbers.append(i)

# print(numbers)


#2

# numbers = [int(i) for i in input().split('')]
# string_input = input()


#3


#4

num_of_people = [int(i) for i in input().split(' ')]
k = int(input())

dead_people = []
while len(num_of_people) > 0:

    for person in range(k, len(num_of_people), k):
        num_of_people.remove(person)
        dead_people.append(person)

print(dead_people)

#5

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