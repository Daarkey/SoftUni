"""1. Smallest of Three Numbers"""

# def smallest_num(num1, num2, num3):
#     return min(num1, num2, num3)


# number1, number2, number3 = int(input()), int(input()), int(input())

# print(smallest_num(number1, number2, number3))


"""2. Add and Subtract"""
# def sum_numbers(num1, num2):
#     return num1 + num2


# def subtract(num1, num2, num3):
#     return (num1 + num2) - num3


# def add_and_subtract(num1, num2, num3):
#     return subtract(num1, num2, num3)


# number1, number2, number3 = int(input()), int(input()), int(input())
# print(add_and_subtract(number1, number2, number3))

"""3. Characters in Range"""
# def ascii_range(starting_char, ending_char):
#     for char in range(ord(starting_char) + 1, ord(ending_char)):
#         print(chr(char), end=" ")

# first_char = input()
# second_char = input()
# ascii_range(first_char, second_char)


"""4. Odd and Even Sum"""
# def sum_of_even_and_odd(num):

#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0

#     for n in num:
#         number = int(n)
#         if number % 2 == 0:
#             sum_of_even_digits += number
#         else:
#             sum_of_odd_digits += number

#     return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


# number = input()
# print(sum_of_even_and_odd(number))


"""5. Even Numbers"""
# def get_even_numbers(list_of_numbers):

#     even_numbers = []
#     for number in list_of_numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)

#     return even_numbers


# numbers = [int(x) for x in input().split()]
# print(get_even_numbers(numbers))

"""OR USING FILTER()"""


def get_even_numbers(num):
    return num % 2 == 0


numbers = [int(x) for x in input().split()]
print(list(filter(get_even_numbers, numbers)))

"""6. Sort"""


"""7. Min Max and Sum"""


"""8. Palindrome Integers"""


"""9. Password Validator"""


"""10. Perfect Number"""
