#1

# for num in range(1, 1000):
#     if num % 10 == 7:
#         print(num)


#2

# from sys import maxsize

# num = int(input())

# max_num = - maxsize
# sum_nums = 0

# for n in range(num):
#     number = int(input())
#     if number > max_num:
#         max_num = number
#     sum_nums += number

# if max_num == sum_nums - max_num:
#     print("Yes")
#     print(f'Sum = {max_num}')
# else:
#     difference = abs(max_num - (sum_nums - max_num))
#     print("No")
#     print(f'Diff = {abs(difference)}')


#3

# number = int(input())

# counter_200 = 0
# counter_399 = 0
# counter_599 = 0
# counter_799 = 0
# counter_800 = 0

# if 1 <= number <= 1000:
#     for i in range(number):
#         num = int(input())
#         if num < 200:
#             counter_200 += 1
#         elif 200 <= num <= 399:
#             counter_399 += 1
#         elif 400 <= num <= 599:
#             counter_599 += 1
#         elif 600 <= num <= 799:
#             counter_799 += 1
#         else:
#             counter_800 += 1

# print(f'{((counter_200 / number) * 100):.2f}%')
# print(f'{((counter_399 / number) * 100):.2f}%')
# print(f'{((counter_599 / number) * 100):.2f}%')
# print(f'{((counter_799 / number) * 100):.2f}%')
# print(f'{((counter_800 / number) * 100):.2f}%')


#4

# age = int(input())
# price_laundrymachine = float(input())
# price_toy = int(input())

# savings = 0
# received_money = 0
# toys_num = 0

# for i in range(1, age + 1):
#     if i % 2 == 0:
#         received_money += 10
#         savings += received_money - 1
#     else:
#         toys_num += 1

# total_toys_sum = toys_num * price_toy
# total_sum = savings + total_toys_sum

# difference = abs(total_sum - price_laundrymachine)

# if total_sum >= price_laundrymachine:
#     print(f'Yes! {difference:.2f}')
# else:
#     print(f'No! {difference:.2f}')


#5

# tabs_open = int(input())
# salary = int(input())

# for i in range(tabs_open):
#     site = input()
#     if site == 'Facebook':
#         salary -= 150
#     elif site == 'Instagram':
#         salary -= 100
#     elif site == 'Reddit':
#         salary -= 50
#     if salary <= 0:
#         break

# if salary <= 0:
#     print("You have lost your salary.")
# else:
#     print(salary)


#6

# actor_name = input()
# academy_points = float(input())
# jury_number = int(input())

# points_received = academy_points

# for i in range(jury_number):
#     jury_name = input()
#     jury_points = float(input())
#     points_received += (((len(jury_name)) * jury_points) / 2)
#     if points_received > 1250.5:
#         break

# if points_received > 1250.5:
#     print(f'Congratulations, {actor_name} got a nominee for leading role with {points_received:.1f}!')
# else:
#     points_needed = 1250.5 - points_received
#     print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')


#7

# groups_number = int(input())

# total_number_people = 0
# mussala_group = 0
# montblanc_group = 0
# killimanjaro_group = 0
# k2_group = 0
# everest_group = 0

# for i in range(groups_number):
#     number_people = int(input())
#     total_number_people += number_people
#     if number_people <= 5:
#         mussala_group += number_people
#     elif 6 <= number_people <= 12:
#         montblanc_group += number_people
#     elif 13 <= number_people <= 25:
#         killimanjaro_group += number_people
#     elif 26 <= number_people <= 40:
#         k2_group += number_people
#     else:
#         everest_group += number_people

# mussala_percent = (mussala_group / total_number_people) * 100
# montblanc_group = (montblanc_group / total_number_people) * 100
# killimanjaro_group = (killimanjaro_group / total_number_people) * 100
# k2_group = (k2_group / total_number_people) * 100
# everest_group = (everest_group / total_number_people) * 100

# print(f'{mussala_percent:.2f}%')
# print(f'{montblanc_group:.2f}%')
# print(f'{killimanjaro_group:.2f}%')
# print(f'{k2_group:.2f}%')
# print(f'{everest_group:.2f}%')

#8
# from math import floor

# tournaments_number = int(input())
# starting_points = int(input())

# total_points = starting_points
# wins = 0

# for i in range(tournaments_number):
#     tournament_stage = input()
#     if tournament_stage == 'W':
#         total_points += 2000
#         wins += 1
#     elif tournament_stage == 'F':
#         total_points += 1200
#     elif tournament_stage == 'SF':
#         total_points += 720

# average_points = (total_points - starting_points) / tournaments_number
# percent_wins = (wins / tournaments_number) * 100

# print(f'Final points: {total_points}')
# print(f'Average points: {floor(average_points)}')
# print(f'{percent_wins:.2f}%')
