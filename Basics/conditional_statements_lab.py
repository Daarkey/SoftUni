#1

# time1 = int(input())
# time2 = int(input())
# time3 = int(input())

# total_time = time1 + time2 + time3

# minutes = total_time // 60
# seconds = total_time % 60

# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')


#2

# number = int(input())
# bonus = 0

# if number <= 100:
#     bonus = 5
# elif 100 < number <= 1000:
#     bonus = number * 0.2
# elif number > 1000:
#     bonus = number * 0.1

# if number % 2 == 0:
#     bonus += 1
# elif number % 10 == 5:
#     bonus += 2

# print(bonus)
# print(number + bonus)


#3

# hours = int(input())
# minutes = int(input())

# future = minutes + 15

# if future >= 60:
#     hours += 1
# if hours >= 24:
#     hours = 0

# future = future % 60

# if future < 10:
#     print(f'{hours}:0{future}')
# else:
#     print(f'{hours}:{future}')


#4

# price_vacation = float(input())
# num_puzzle = int(input())
# num_doll = int(input())
# num_bear = int(input())
# num_minion = int(input())
# num_truck = int(input())

# price_puzzle = 2.6
# price_doll = 3
# price_bear = 4.1
# price_minion = 8.2
# price_truck = 2

# total_num = num_puzzle + num_doll + num_bear + num_minion + num_truck
# total_price = num_puzzle * price_puzzle + num_doll * price_doll + num_bear * price_bear + num_minion * price_minion + num_truck * price_truck


# if total_num >= 50:
#     total_price = total_price * 0.75

# rent = total_price * 0.1

# income = total_price - rent

# result_price = abs(price_vacation - income)

# if income >= price_vacation:
#     print(f'Yes! {result_price:.2f} lv left.')
# else:
#     print(f'Not enough money! {result_price:.2f} lv needed.')


#5

# budget = float(input())
# num_statist = int(input())
# clothes_cost_per_person = float(input())

# decor = budget * 0.1
# total_clothes_price = num_statist * clothes_cost_per_person

# if num_statist >= 150:
#     total_clothes_price = total_clothes_price * 0.9

# decor_and_clothes = decor + total_clothes_price

# difference = abs(decor_and_clothes - budget)

# if decor_and_clothes > budget:
#     print("Not enough money!")
#     print(f'Wingard needs {difference:.2f} leva more.')
# else:
#     print("Action!")
#     print(f'Wingard starts filming with {difference:.2f} leva left.')


#6

# record_in_sec = float(input())
# distance_in_m = float(input())
# time_for_1m = float(input())

# total_time = distance_in_m * time_for_1m

# current = distance_in_m // 15
# current = current * 12.5
# # print(current)
# total = total_time + current
# # print(total)
# difference = abs(total - record_in_sec)
# # print(difference)

# if record_in_sec <= total:
#     print(f'No, he failed! He was {difference:.2f} seconds slower.')
# else:
#     print(f'Yes, he succeeded! The new world record is {total:.2f} seconds.')


#7

# budget = float(input())
# num_gpu = int(input())
# num_cpu = int(input())
# num_ram = int(input())

# price_gpu = 250
# total_gpu = num_gpu * price_gpu
# price_cpu = total_gpu * 0.35
# price_ram = total_gpu * 0.1

# total_sum = total_gpu + num_cpu * price_cpu + num_ram * price_ram

# if num_gpu > num_cpu:
#     total_sum = total_sum * 0.85

# difference = abs(total_sum - budget)

# if total_sum > budget:
#     print(f'Not enough money! You need {difference:.2f} leva more!')
# else:
#     print(f'You have {difference:.2f} leva left!')

#8
# from math import ceil

# movie_name = input()
# episode_duration = int(input())
# break_time = int(input())

# lunch_time = break_time / 8
# rest_time = break_time / 4

# time_left = break_time - lunch_time - rest_time
# difference = ceil(abs(time_left - episode_duration))

# if time_left >= episode_duration:
#     print(f'You have enough time to watch {movie_name} and left with {difference} minutes free time.')
# else:
#     print(f'You don\'t have enough time to watch {movie_name}, you need {difference} more minutes.')
