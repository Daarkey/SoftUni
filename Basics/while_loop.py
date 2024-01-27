#1

# while True:
#     text = input()

#     if text == 'Stop':
#         break
#     else:
#         print(text)

#2

# username = input()
# set_password = input()

# while True:
#     password = input()

#     if password == set_password:
#         print(f'Welcome {username}!')
#         break

#3

# number = int(input())

# counter = 0

# while True:
#     number2 = int(input())
#     counter += number2
#     if counter >= number:
#         print(counter)
#         break


#4

# number = int(input())

# counter = 1

# while counter <= number:
#     print(counter)
#     counter = counter * 2 + 1


#5

# balance = 0

# while True:

#     income = input()

#     if income == 'NoMoreMoney':
#         break

#     income_money = float(income)

#     if income_money >= 0: 
#         balance += income_money
#         print(f'Increase: {income_money:.2f}')
#     else:
#         print('Invalid operation!')
#         break
    

# print(f'Total: {balance:.2f}')


#6

# from sys import maxsize

# text_input = input()

# max_num = -maxsize

# while text_input != 'Stop':

#     number = int(text_input)

#     if number > max_num:
#         max_num = number
#     text_input = input()

# print(max_num)


#7

# from sys import maxsize

# text_input = input()

# min_num = maxsize

# while text_input != 'Stop':

#     number = int(text_input)

#     if number < min_num:
#         min_num = number
#     text_input = input()

# print(min_num)


#8

# student_name = input()

# year = 0
# grades_counter = 0
# expelled = 0

# while year <=12:
#     grade = float(input())

#     if grade < 4.00:
#         expelled += 1
#         if expelled > 1:
#             print(f'{student_name} has been excluded at {year + 1} grade')
#             break
#         continue

#     year += 1
#     grades_counter += grade

#     if year == 12:
#         average_grade = grades_counter / 12
#         print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
#         break




