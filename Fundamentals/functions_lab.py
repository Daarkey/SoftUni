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
# def get_even_numbers(num):
#     return num % 2 == 0

# numbers = [int(x) for x in input().split()]
# print(list(filter(get_even_numbers, numbers)))

"""OR USING FILTER AND LAMBDA"""
# numbers = [int(x) for x in input().split()]
# print((list(filter(lambda number: (number % 2 == 0), numbers))))

"""6. Sort"""
# numbers = [int(x) for x in input().split()]
# print(sorted(numbers))

"""7. Min Max and Sum"""
# def min_max_sum(list_of_numbers):
#     min_num = min(list_of_numbers)
#     max_num = max(list_of_numbers)
#     sum_num = sum(list_of_numbers)
#     return min_num, max_num, sum_num

# numbers = [int(x) for x in input().split()]

# results = min_max_sum(numbers)
# print(f"The minimum number is {results[0]}")
# print(f"The maximum number is {results[1]}")
# print(f"The sum number is: {results[2]}")

"""8. Palindrome Integers"""
# def is_palindrome(list_of_numbers):
#     list_of_reversed_nums = []
#     list_of_palindromes = []

#     for number in list_of_numbers:
#         reversed_num = 0
#         while number != 0:
#             digit = number % 10
#             reversed_num = reversed_num * 10 + digit
#             number = number // 10
#         list_of_reversed_nums.append(reversed_num)

#     """This returns a list with only the reversed numbers"""
#     # for num in list_of_numbers:
#     #     for rev_num in list_of_reversed_nums:
#     #         if num == rev_num:
#     #             list_of_palindromes.append(num)

#     for num in range(0, len(list_of_numbers)):
#         for rev_num in range(0, len(list_of_reversed_nums)):
#             if num == rev_num:
#                 if list_of_numbers[num] == list_of_reversed_nums[rev_num]:
#                     list_of_palindromes.append("True")
#                 else:
#                     list_of_palindromes.append("False")

#     return list_of_palindromes


# numbers = [int(x) for x in input().split(", ")]
# print(is_palindrome(numbers))


"""9. Password Validator"""


def password_validator(password):
    is_valid = False
    digit_counter = sum(x.isdigit() for x in password)

    if 6 <= len(password) <= 10:
        is_valid = True
    else:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if password.isalnum():
        is_valid = True
    else:
        is_valid = False
        print("Password must consist only of letters and digits")
    if digit_counter >= 2:
        is_valid = True
    else:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid == "True":
        success = "Password is valid"
        return success


password_input = input()

result = password_validator(password_input)
print(result)

# """10. Perfect Number"""
