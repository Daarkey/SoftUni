"""1. Number Definer"""

# number = float(input())

# if number == 0:
#     print("zero")
# elif number > 0:
#     if number < 1:
#         print("small positive")
#     elif number > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     if abs(number) < 1:
#         print("small negative")
#     elif abs(number) > 1000000:
#         print("large negative")
#     else:
#         print("negative")


"""2. Largest of Three Numbers"""
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# print(max(num1, num2, num3))


"""3. Word Reverse"""
# word = input()

# for i in range(len(word) - 1, -1, -1):
#     print(word[i], end='')


"""4. Even Numbers"""
# number = int(input())

# for n in range(number):
#     num = int(input())

#     if num % 2 != 0:
#         print(f'{num} is odd!')
#         break

# else:
#     print("All numbers are even.")


"""5. Number Between 1 and 100"""
# number = float(input())

# while number < 1 or number > 100:
#     number = float(input())

#     if 1 <= number <= 100:
#         print(f'The number {number} is between 1 and 100')
#         break


"""6. Shopping"""
# budget = int(input())
# total_spent = 0

# while True:
#     command = input()

#     if command == 'End':
#         print("You bought everything needed.")
#         break

#     price = int(command)

#     if total_spent + price > budget:
#         print("You went in overdraft!")
#         break
#     else:
#         total_spent += price


"""7. Patterns"""
# number = int(input())

# for i in range(1, number + 1):
#     for j in range(0, i):
#         print("*", end='')
#     print()

# for i in range(number - 1, 0, -1):
#     for j in range(0, i):
#         print("*", end='')
#     print()
