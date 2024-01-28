#1
#first try
# tail, body, head = input(), input(), input()

# right_order = [head, body, tail]

# print(right_order)

#second try
# right_order = []

# for i in range(3):
#     body_part = input()
#     right_order.append(body_part)

# right_order[0], right_order[2] = right_order[2], right_order[0]
# print(right_order)


#2

# number = int(input())

# list_of_courses = []

# for name in range(number):
#     course = input()
#     list_of_courses.append(course)

# print(list_of_courses)


#3
# number = int(input())

# positives = []
# negatives = []

# for n in range(number):
#     num = int(input())
#     if num >= 0:
#         positives.append(num)
#     else:
#         negatives.append(num)

# print(f"{positives} \n{negatives}")
# print(f"Count of positives: {len(positives)}")
# print(f'Sum of negatives: {sum(negatives)}')


#4

# number = int(input())
# word = input()
# string_list = []

# for n in range(number):
#     strings =  input()
#     string_list.append(strings)

# print(string_list)

# for i in range(len(string_list) - 1, -1, -1):
#     new_string = string_list[i]
#     if word not in new_string:
#         string_list.remove(new_string)

# print(string_list)


#5

# number = int(input())
# odd = []
# even = []
# negative = []
# positive = []

# for n in range(number):
#     num = int(input())
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#     if num >= 0:
#         positive.append(num)
#     else:
#         negative.append(num)

# command = input()

# if command == 'even':
#     print(even)
# elif command == 'odd':
#     print(odd)
# elif command == 'negative':
#     print(negative)
# elif command == 'positive':
#     print(positive)
# else:
#     print('Incorrect command!')
