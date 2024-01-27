#1

# projection = input()
# rows = int(input())
# columns = int(input())

# premiere_price = 12
# normal_price = 7.5
# discount_price = 5

# total_price = 0

# if projection == "Premiere":
#     total_price = rows * columns * premiere_price
# elif projection == "Normal":
#     total_price = rows * columns * normal_price
# elif projection == "Discount":
#     total_price = rows * columns * discount_price

# print(f'{total_price:.2f} leva')


#2

# temperature = int(input())
# time_of_day = input()

# if 10 <= temperature <= 18:
#     if time_of_day == "Morning":
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif time_of_day == "Afternoon" or time_of_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
# elif 18 < temperature <= 24:
#     if time_of_day == "Afternoon":
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "Morning" or time_of_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
# elif temperature >= 25:
#     if time_of_day == "Morning":
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "Afternoon":
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
#     elif time_of_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"

# print(f'It\'s {temperature} degrees, get your {outfit} and {shoes}.')


#3

# flower = input()
# num_flowers = int(input())
# budget = int(input())

# price = 0

# if flower == "Roses":
#     if  num_flowers > 80:
#         price = (num_flowers * 5) * 0.9
#     else:
#         price = (num_flowers * 5)
# elif flower == "Dahlias":
#     if num_flowers > 90:
#         price = (num_flowers * 3.8) * 0.85
#     else:
#         price = (num_flowers * 3.8)
# elif flower == "Tulips":
#     if num_flowers > 80:
#         price = (num_flowers * 2.8) * 0.85
#     else:
#         price = (num_flowers * 2.8)
# elif flower == "Narcissus":
#     if num_flowers < 120:
#         price = (num_flowers * 3) + ((num_flowers * 3) * 0.15)
#     else:
#         price = (num_flowers * 3)
# elif flower == "Gladiolus":
#     if num_flowers < 80:
#         price = (num_flowers * 2.5) + ((num_flowers * 2.5) * 0.2)
#     else:
#         price = (num_flowers * 2.5)

# difference = abs(budget - price)

# if budget >= price:
#     print(f'Hey, you have a great garden with {num_flowers} {flower} and {difference:.2f} leva left.')
# else:
#     print(f'Not enough money, you need {difference:.2f} leva more.')


#4

# budget = int(input())
# season = input()
# fishermen = int(input())

# if season == "Spring": 
#     if fishermen <= 6:
#         price = 3000 * 0.9
#     elif 7 <= fishermen <= 11:
#         price = 3000 * 0.85
#     else:
#         price = 3000 * 0.75
# elif season == "Summer" or season == "Autumn": 
#     if fishermen <= 6:
#         price = 4200 * 0.9
#     elif 7 <= fishermen <= 11:
#         price = 4200 * 0.85
#     else:
#         price = 4200 * 0.75
# elif season == "Winter": 
#     if fishermen <= 6:
#         price = 2600 * 0.9
#     elif 7 <= fishermen <= 11:
#         price = 2600 * 0.85
#     else:
#         price = 2600 * 0.75

# if fishermen % 2 == 0 and season != "Autumn":
#     price = price * 0.95

# difference = abs(budget - price)

# if budget >= price:
#     print(f'Yes! You have {difference:.2f} leva left.')
# else:
#     print(f'Not enough money! You need {difference:.2f} leva.')


#5

# budget = float(input())
# season = input()

# destination = ''
# accommodation = ''

# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         price = budget * 0.3
#         accommodation = "Camp"
#     else:
#         price = budget * 0.7
#         accommodation = "Hotel"
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         price = budget * 0.4
#         accommodation = "Camp"
#     else:
#         price = budget * 0.8
#         accommodation = "Hotel"
# else:
#     destination = "Europe"
#     price = budget * 0.9
#     accommodation = "Hotel"

# print(f'Somewhere in {destination}')
# print(f'{accommodation} - {price:.2f}')


#6

# num1 = int(input())
# num2 = int(input())
# operator = input()

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 == 0:
#         print(f'Cannot divide {num1} by zero')
#     else:
#         result = num1 / num2
#         print(f'{num1} / {num2} = {result:.2f}')
# elif operator == "%":
#     if num2 == 0:
#         print(f'Cannot divide {num1} by zero')
#     else:
#         result = num1 % num2
#         print(f'{num1} % {num2} = {result}')

# if operator == "+" or operator == "-" or operator == "*":
#     if result % 2 == 0:
#         print(f'{num1} {operator} {num2} = {result} - even')
#     else:
#         print(f'{num1} {operator} {num2} = {result} - odd')


#7

# month = input()
# days = int(input())

# if month == "May" or month == "October":
#     studio_price = 50
#     apartment_price = 65
#     if days > 14:
#         studio_price = studio_price * 0.7
#         apartment_price = apartment_price * 0.9
#     elif days > 7:
#         studio_price = studio_price * 0.95
# elif month == "June" or month == "September":
#     studio_price = 75.2
#     apartment_price = 68.7
#     if days > 14:
#         studio_price = studio_price * 0.8
#         apartment_price = apartment_price * 0.9
# elif month == "July" or month == "August":
#     studio_price = 76
#     apartment_price = 77
#     if days > 14:
#         apartment_price = apartment_price * 0.9

# total_apartment = apartment_price * days
# total_studio = studio_price * days

# print(f'Apartment: {total_apartment:.2f} lv.')
# print(f'Studio: {total_studio:.2f} lv.')


#8

# exam_hour = int(input())
# exam_minute = int(input())
# arrival_hour = int(input())
# arrival_minute = int(input())

# total_exam_min = exam_hour * 60 + exam_minute
# total_arrival_min = arrival_hour * 60 + arrival_minute

# minutes_difference = abs(total_exam_min - total_arrival_min)

# early_time = total_exam_min - 30

# if total_arrival_min < early_time:
#     print("Early")
#     if minutes_difference >= 60: 
#         hour = minutes_difference // 60
#         minutes = minutes_difference % 60
#         if minutes < 10:
#             print(f'{hour}:0{minutes} hours before the start')
#         else:
#             print(f'{hour}:{minutes} hours before the start')
#     else:
#         print(f'{minutes_difference} minutes before the start')
# elif total_arrival_min >= early_time and total_arrival_min <= total_exam_min:
#     if total_arrival_min == total_exam_min:
#         print("On time")
#     else:
#         print("On time")
#         print(f'{minutes_difference} minutes before the start')
# else:
#     print("Late")
#     if minutes_difference >= 60: 
#         hour = minutes_difference // 60
#         minutes = minutes_difference % 60
#         if minutes < 10:
#             print(f'{hour}:0{minutes} hours after the start')
#         else:
#             print(f'{hour}:{minutes} hours after the start')
#     else:
#         print(f'{minutes_difference} minutes after the start')


#9

# days = int(input())
# accommodation = input()
# feedback = input()

# nights = days - 1

# if days < 10:
#     if accommodation == 'room for one person':
#         price = 18 * nights
#     elif accommodation == 'apartment':
#         price = (25 * nights) * 0.7
#     elif accommodation == 'president apartment':
#         price = (35 * nights) * 0.9
# elif 10 <= days <= 15:
#     if accommodation == 'room for one person':
#         price = 18 * nights
#     elif accommodation == 'apartment':
#         price = (25 * nights) * 0.65
#     elif accommodation == 'president apartment':
#         price = (35 * nights) * 0.85
# elif days > 15:
#     if accommodation == 'room for one person':
#         price = 18 * nights
#     elif accommodation == 'apartment':
#         price = (25 * nights) * 0.5
#     elif accommodation == 'president apartment':
#         price = (35 * nights) * 0.8

# if feedback == 'positive':
#     price = price + (price * 0.25)
# else:
#     price = price * 0.9

# print(f'{price:.2f}')