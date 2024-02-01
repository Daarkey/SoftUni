#1

# def absolute_number(number):
#     return abs(number)

# numbers = [float(num) for num in input().split()]

# final_list  = []

# for num in numbers:
#     final_list.append(absolute_number(num))

# print(final_list)


#2

# def grade_to_category(number):
#     grade = ''
#     if 2.00 <= number <= 2.99:
#         grade = 'Fail'
#     elif 3.00 <= number <= 3.49:
#         grade = 'Poor'
#     elif 3.50 <= number <= 4.49:
#         grade = 'Good'
#     elif 4.50 <= number <= 5.49:
#         grade = 'Very Good'
#     elif 5.50 <= number <= 6.00:
#         grade = 'Excellent'
#     return grade

# grade_input = float(input())

# print(grade_to_category(grade_input))


#3

# def calculator(operator, num_1, num_2):

#     if operator == 'multiply':
#         result = num_1 * num_2
#     elif operator == 'divide':
#         result = num_1 // num_2
#     elif operator == 'add':
#         result = num_1 + num_2
#     elif operator == 'subtract':
#         result = num_1 - num_2

#     return print(result)

# operator = input()
# number_1, number_2 = int(input()), int(input())

# calculator(operator, number_1, number_2)


#4

# def string_replicator(string, times):
#     return print(string * times)

# string_input = input()
# counter = int(input())

# string_replicator(string_input, counter)


#5


# def total_price(product, quantity):
#     final_price = 0
    
#     if product == 'coffee':
#         final_price = quantity * 1.50
#     elif product == 'water':
#         final_price = quantity * 1
#     elif product == 'coke':
#         final_price = quantity * 1.4
#     elif final_price == 'snacks':
#         final_price = quantity * 2

#     return print(f'{final_price:.2f}')

# product = input()
# quantity = int(input())

# total_price(product, quantity)


#6

# def rec_area(width, height):
#     return print(width * height)

# width_input = int(input())
# height_input = int(input())

# rec_area(width_input, height_input)


#7

# def rounding_numbers(number):
#     return round(number)

# numbers = [float(num) for num in input().split(' ')]

# final_list  = []

# for num in numbers:
#     final_list.append(rounding_numbers(num))

# print(final_list)