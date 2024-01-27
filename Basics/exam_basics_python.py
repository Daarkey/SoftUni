#1

# from math import ceil

# gpu_price = int(input())
# convertor_price = int(input())
# electricity_per_card_per_day = float(input())
# gain_per_card_per_day = float(input())

# total_gpu_price = gpu_price * 13
# total_convertor_price = convertor_price * 13

# total_sum = total_gpu_price + total_convertor_price + 1000

# print(total_sum)

# clean_gain_per_card_per_day = gain_per_card_per_day - electricity_per_card_per_day

# total_gain_per_day = clean_gain_per_card_per_day * 13

# days_needed = total_sum / total_gain_per_day

# print(ceil(days_needed))


#2

# from math import ceil

# name = input()
# budget = float(input())
# num_bottles = int(input())
# num_packets_chips = int(input())

# beer_price = 1.2
# total_beer_price = beer_price * num_bottles
# chips_price = total_beer_price * 0.45
# total_chips_price = ceil(chips_price * num_packets_chips)

# total_sum = total_beer_price + total_chips_price

# difference = abs(total_sum - budget)

# if budget >= total_sum:
#     print(f'{name} bought a snack and has {difference:.2f} leva left.')
# else:
#     print(f'{name} needs {difference:.2f} more leva!')


#3

# team = input()
# souvenir = input()
# num_souvenirs = int(input())

# price = 0

# if souvenir == 'flags':
#     if team == 'Argentina':
#         price = 3.25
#     elif team == 'Brazil':
#         price = 4.2
#     elif team == 'Croatia':
#         price = 2.75
#     elif team == 'Denmark':
#         price = 3.10
#     else:
#         print("Invalid country!")
# elif souvenir == 'caps':
#     if team == 'Argentina':
#         price = 7.2
#     elif team == 'Brazil':
#         price = 8.5
#     elif team == 'Croatia':
#         price = 6.9
#     elif team == 'Denmark':
#         price = 6.5
#     else:
#         print("Invalid country!")
# elif souvenir == 'posters':
#     if team == 'Argentina':
#         price = 5.1
#     elif team == 'Brazil':
#         price = 5.35
#     elif team == 'Croatia':
#         price = 4.95
#     elif team == 'Denmark':
#         price = 4.8
#     else:
#         print("Invalid country!")
# elif souvenir == 'stickers':
#     if team == 'Argentina':
#         price = 1.25
#     elif team == 'Brazil':
#         price = 1.2
#     elif team == 'Croatia':
#         price = 1.1
#     elif team == 'Denmark':
#         price = 0.9
#     else:
#         print("Invalid country!")
# else:
#     print("Invalid stock!")

# total_sum = price * num_souvenirs

# if total_sum > 0:
#     print(f'Pepi bought {num_souvenirs} {souvenir} of {team} for {total_sum:.2f} lv.')


#4

# num_cats = int(input())

# food_price_kg = 12.45

# group1 = 0
# group2 = 0
# group3 = 0
# total_food_eaten = 0

# for cats in range(num_cats):

#     food_eaten = float(input())

#     if 100 <= food_eaten < 200:
#         group1 += 1
#     elif 200 <= food_eaten < 300:
#         group2 += 1
#     elif 300 <= food_eaten < 400:
#         group3 += 1

#     total_food_eaten += food_eaten

# total_food_eaten_kg = total_food_eaten / 1000
# total_sum = total_food_eaten_kg * food_price_kg

# print(f'Group 1: {group1} cats.')
# print(f'Group 2: {group2} cats.')
# print(f'Group 3: {group3} cats.')
# print(f'Price for food per day: {total_sum:.2f} lv.')


#5

# kids = 0
# adults = 0

# while True:
#     command = input()

#     if command == 'Christmas':
#         break

#     age = int(command)

#     if age <= 16:
#         kids += 1
#     else:
#         adults += 1

# total_toys_sum = kids * 5
# total_sweaters_sum = adults * 15

# print(f'Number of adults: {adults}')
# print(f'Number of kids: {kids}')
# print(f'Money for toys: {total_toys_sum}')
# print(f'Money for sweaters: {total_sweaters_sum}')


#6

# location_number = int(input())

# collected_gold = 0

# for num in range(location_number):
#     expected_gold_per_day = float(input())
#     days_in_location = int(input())

#     collected_gold = 0

#     for day in range(days_in_location):
#         gained_gold = float(input())
#         collected_gold += gained_gold

#         average_gold = collected_gold / days_in_location

#     if average_gold >= expected_gold_per_day:
#         print(f'Good job! Average gold per day: {average_gold:.2f}.')
#     else:
#         needed_gold = expected_gold_per_day - average_gold
#         print(f'You need {needed_gold:.2f} gold.')
