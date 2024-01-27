#1

# num = int(input())

# if num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wednesday")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")
# else:
#     print("Error")


#2

# day_of_week = input()

# if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
#     print("Working day")
# elif day_of_week == "Saturday" or day_of_week == "Sunday":
#     print("Weekend")
# else:
#     print("Error")


#3

# animal = input()

# if animal == "dog":
#     print("mammal")
# elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
#     print("reptile")
# else:
#     print("unknown")


#4

# age = float(input())
# gender = input()

# if gender == "m":
#     if age < 16:
#         print("Master")
#     else:
#         print("Mr.")
# else:
#     if age < 16:
#         print("Miss")
#     else:
#         print("Ms.")


#5

# product = input()
# city = input()
# quantity = float(input())

# price = 0

# if city == "Sofia":
#     if product == "coffee":
#         price = 0.5
#     elif product == "water":
#         price = 0.8
#     elif product == "beer":
#         price = 1.2
#     elif product == "sweets":
#         price = 1.45
#     elif product == "peanuts":
#         price = 1.6
# elif city == "Plovdiv":
#     if product == "coffee":
#         price = 0.4
#     elif product == "water":
#         price = 0.7
#     elif product == "beer":
#         price = 1.15
#     elif product == "sweets":
#         price = 1.3
#     elif product == "peanuts":
#         price = 1.5
# elif city == "Varna":
#     if product == "coffee":
#         price = 0.45
#     elif product == "water":
#         price = 0.7
#     elif product == "beer":
#         price = 1.10
#     elif product == "sweets":
#         price = 1.35
#     elif product == "peanuts":
#         price = 1.55

# print(price*quantity)


#6

# num = int(input())

# if - 100 <= num <= 100 and num != 0:
#     print("Yes")
# else:
#     print("No")


#7

# hours = int(input())
# day_of_week = input()

# if 10 <= hours <= 18 and (day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday"):
#     print("open")
# else:
#     print("closed")


#8

# day_of_week = input()

# ticket = 0

# if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
#     ticket = 12
# elif day_of_week == "Wednesday" or day_of_week == "Thursday":
#     ticket = 14
# else:
#     ticket = 16

# print(ticket)


#9

# user_input = input()

# if user_input == "banana" or user_input == "apple" or user_input == "kiwi" or user_input == "cherry" or user_input == "lemon" or user_input == "grapes":
#     print("fruit")
# elif user_input == "tomato" or user_input == "cucumber" or user_input == "pepper" or user_input == "carrot":
#     print("vegetable")
# else:
#     print("unknown")


#10

# num = int(input())

# if 100 <= num <= 200 or num == 0:
#     pass
# else:
#     print("invalid")

# #or
    
# if not(100 <= num <= 200 or num == 0):
#     print("invalid")


#11

# fruit = input()
# day_of_week = input()
# quantity = float(input())

# price = 0

# if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
#     if fruit == "banana":
#         price = 2.5
#     elif fruit == "apple":
#         price = 1.2
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.7
#     elif fruit == "pineapple":
#         price = 5.5
#     elif fruit == "grapes":
#         price = 3.85
#     else:
#         print("error")
# elif day_of_week == "Saturday" or day_of_week == "Sunday":
#     if fruit == "banana":
#         price = 2.7
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.9
#     elif fruit == "grapefruit":
#         price = 1.6
#     elif fruit == "kiwi":
#         price = 3
#     elif fruit == "pineapple":
#         price = 5.6
#     elif fruit == "grapes":
#         price = 4.2
#     else:
#         print("error")
# else:
#     print("error")

# if price != 0:
#     print(f'{(price * quantity):.2f}')


#12

# city = input()
# quantity = float(input())

# percent = 0

# if city == "Sofia":
#     if 0 <= quantity <= 500:
#         percent = 5
#     elif 500 < quantity <= 1000:
#         percent = 7
#     elif 1000 < quantity <= 10000:
#         percent = 8
#     elif quantity > 10000:
#         percent = 12
#     elif quantity < 0:
#         print("error")
# elif city == "Varna":
#     if 0 <= quantity <= 500:
#         percent = 4.5
#     elif 500 < quantity <= 1000:
#         percent = 7.5
#     elif 1000 < quantity <= 10000:
#         percent = 10
#     elif quantity > 10000:
#         percent = 13
#     elif quantity < 0:
#         print("error")
# elif city == "Plovdiv":
#     if 0 <= quantity <= 500:
#         percent = 5.5
#     elif 500 < quantity <= 1000:
#         percent = 8
#     elif 1000 < quantity <= 10000:
#         percent = 12
#     elif quantity > 10000:
#         percent = 14.5
#     elif quantity < 0:
#         print("error")
# else:
#     print("error")

# if quantity > 0 and (city == "Plovdiv" or city == "Sofia" or city == "Varna"):
#     print(f'{((percent * quantity) / 100):.2f}')