# from math import floor, ceil

# racket_price = float(input())
# num_rackets = int(input())
# num_sneakers = int(input())

# sneakers_price = racket_price / 6

# sum_sneakers_rackets = racket_price * num_rackets + sneakers_price * num_sneakers
# other_equipment = sum_sneakers_rackets * 0.2

# total_sum = sum_sneakers_rackets + other_equipment

# total_djokovic = total_sum / 8
# total_sponsors = total_sum - total_djokovic

# print(f'Price to be paid by Djokovic {floor(total_djokovic)}')
# print(f'Price to be paid by sponsors {ceil(total_sponsors)}')


# annual_fee = int(input())

# sneakers_price = annual_fee * 0.6
# equipment_price = sneakers_price * 0.8
# ball_price = equipment_price / 4
# accessories_price = ball_price / 5

# total = annual_fee + equipment_price + sneakers_price + ball_price + accessories_price

# print(f'{total:.2f}')


# first_score = input()
# second_score = input()
# third_score = input()

# wins = 0
# losts = 0
# draws = 0 

# if first_score[0] > first_score[2]:
#     wins += 1
# elif first_score[0] < first_score[2]:
#     losts += 1
# else:
#     draws += 1

# if second_score[0] > second_score[2]:
#     wins += 1
# elif second_score[0] < second_score[2]:
#     losts += 1
# else:
#     draws += 1

# if third_score[0] > third_score[2]:
#     wins += 1
# elif third_score[0] < third_score[2]:
#     losts += 1
# else:
#     draws += 1

# print(f'Team won {wins} games.')
# print(f'Team lost {losts} games.')
# print(f'Drawn games: {draws}')


# control_min = int(input())
# control_sec = int(input())
# pipe_meters = float(input())
# secs_per_100m = int(input())

# total_control_sec = control_min * 60 + control_sec
# acceleration = pipe_meters / 120
# total_acceleration = acceleration * 2.5

# marin_time = (pipe_meters / 100) * secs_per_100m - total_acceleration

# difference = abs(marin_time - total_control_sec)

# if marin_time <= total_control_sec:
#     print(f'Marin Bangiev won an Olympic quota!')
#     print(f'His time is {marin_time:.3f}.')
# else:
#     print(f'No, Marin failed! He was {difference:.3f} second slower.')


# country = input()
# type_object = input()

# max_score = 20

# if type_object == "ribbon":
#     if country == "Russia":
#         difficulty = 9.1
#         performance = 9.4
#     elif country == "Bulgaria":
#         difficulty = 9.6
#         performance = 9.4
#     elif country == "Italy":
#         difficulty = 9.2
#         performance = 9.5
# elif type_object == "hoop":
#     if country == "Russia":
#         difficulty = 9.3
#         performance = 9.8
#     elif country == "Bulgaria":
#         difficulty = 9.55
#         performance = 9.75
#     elif country == "Italy":
#         difficulty = 9.45
#         performance = 9.35
# elif type_object == "rope":
#     if country == "Russia":
#         difficulty = 9.6
#         performance = 9
#     elif country == "Bulgaria":
#         difficulty = 9.5
#         performance = 9.4
#     elif country == "Italy":
#         difficulty = 9.7
#         performance = 9.15

# total_score = difficulty + performance
# points_needed = max_score - total_score
# percent_needed = (points_needed / max_score) * 100

# print(f'The team of {country} get {total_score:.3f} on {type_object}.')
# print(f'{percent_needed:.2f}%')


# league_state = input()
# ticket_type = input()
# num_ticket = int(input())
# trophy_photo = input()

# if ticket_type == 'Standard':
#     if league_state == 'Quarter final':
#         ticket_price = 55.5
#     elif league_state == 'Semi final':
#         ticket_price = 75.88
#     elif league_state == 'Final':
#         ticket_price = 110.1
# elif ticket_type == 'Premium':
#     if league_state == 'Quarter final':
#         ticket_price = 105.2
#     elif league_state == 'Semi final':
#         ticket_price = 125.22
#     elif league_state == 'Final':
#         ticket_price = 160.66
# elif ticket_type == 'VIP':
#     if league_state == 'Quarter final':
#         ticket_price = 118.9
#     elif league_state == 'Semi final':
#         ticket_price = 300.4
#     elif league_state == 'Final':
#         ticket_price = 400

# total_tickets_price = num_ticket * ticket_price

# if total_tickets_price > 4000:
#     total_tickets_price -= total_tickets_price * 0.25
# elif total_tickets_price > 2500:
#     total_tickets_price -= total_tickets_price * 0.1

# if trophy_photo == 'Y':
#     if total_tickets_price > 4000:
#         trophy_photo_price = 0
#         total_sum = total_tickets_price
#     else:
#         trophy_photo_price = 40
#         total_sum = total_tickets_price + trophy_photo_price * num_ticket
# else:
#     total_sum = total_tickets_price

# print(f'{total_sum:.2f}')


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


# visitors_number = int(input())

# back_train = 0
# chest_train = 0
# legs_train = 0
# abs_train = 0
# protein_shakes = 0
# protein_bars = 0

# for i in range(visitors_number):
#     activity = input()
#     if activity == 'Back':
#         back_train += 1
#     elif activity == 'Chest':
#         chest_train += 1
#     elif activity == 'Legs':
#         legs_train += 1
#     elif activity == 'Abs':
#         abs_train += 1
#     elif activity == 'Protein shake':
#         protein_shakes += 1
#     elif activity == 'Protein bar':
#         protein_bars += 1

# people_training = back_train + chest_train + legs_train + abs_train
# training_percent = (people_training / visitors_number) * 100

# people_buying = protein_shakes + protein_bars
# buying_percent = (people_buying / visitors_number) * 100

# print(f'{back_train} - back')
# print(f'{chest_train} - chest')
# print(f'{legs_train} - legs')
# print(f'{abs_train} - abs')
# print(f'{protein_shakes} - protein shake')
# print(f'{protein_bars} - protein bar')
# print(f'{training_percent:.2f}% - work out')
# print(f'{buying_percent:.2f}% - protein')


# bought_food = int(input())

# bought_food_grams = bought_food * 1000
# food_eaten = 0
# total_food_eaten = 0

# while True:
#     command = input()

#     if command == 'Adopted':
#         break

#     food_eaten = int(command)

#     total_food_eaten += food_eaten

#     leftovers = abs(bought_food_grams - total_food_eaten)

# if bought_food_grams >= total_food_eaten:
#     print(f'Food is enough! Leftovers: {leftovers} grams.')
# else:
#     print(f'Food is not enough. You need {leftovers} grams more.')


# budget = float(input())

# while True:
#     command = input()

#     if command == 'ACTION' or budge <= 0:
#         break

#     actor_name = command

#     if len(actor_name) <= 15:
#         actor_salary = float(input())
#     else:
#         actor_salary = budget * 0.2
    
#     budget -= actor_salary

# if budget >= 0:
#     print(f'We are left with {budget:.2f} leva.')
# else:
#     print(f'We need {abs(budget):.2f} leva for our actors.')


# desired_income = float(input())

# current_income = 0

# while True:
#     cocktail_name = input()

#     if cocktail_name == 'Party!':
#         print(f'We need {needed_money:.2f} leva more.')
#         break

#     cocktail_quantity = int(input())

#     cocktail_price = len(cocktail_name)

#     order = cocktail_price * cocktail_quantity

#     if order % 2 != 0:
#         order = order - (order * 0.25)

#     current_income += order

#     needed_money = abs(desired_income - current_income)

#     if current_income >= desired_income:
#         print("Target acquired.")
#         break

# print(f"Club income - {current_income:.2f} leva.")


# number_egg = int(input())

# red_eggs = 0
# orange_eggs = 0
# blue_eggs = 0
# green_eggs = 0

# for i in range(number_egg):

#     color = input()

#     if color == 'red':
#         red_eggs += 1
#     elif color == 'orange':
#         orange_eggs += 1
#     elif color == 'blue':
#         blue_eggs += 1
#     elif color == 'green':
#         green_eggs += 1

#     number_egg -= 1

# max_color_num = max(red_eggs, orange_eggs, green_eggs, blue_eggs)
# if max_color_num == red_eggs:
#     max_color = 'red'
# elif max_color_num == orange_eggs:
#     max_color = 'orange'
# elif max_color_num == blue_eggs:
#     max_color = 'blue'
# elif max_color_num == green_eggs:
#     max_color = 'green'

# print(f'Red eggs: {red_eggs}')
# print(f'Orange eggs: {orange_eggs}')
# print(f'Blue eggs: {blue_eggs}')
# print(f'Green eggs: {green_eggs}')
# print(f'Max eggs: {max_color_num} -> {max_color}')


# player_name = input()

# starting_points = 301
# successful_shots = 0
# unsuccessful_shots = 0

# while True:
#     field = input()

#     if field == 'Retire':
#         print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
#         break

#     points = int(input())

#     total_hit = 0

#     if field == 'Single':
#         total_hit = points
#     elif field == 'Double':
#         total_hit = points * 2
#     elif field == 'Triple':
#         total_hit = points * 3

#     if total_hit < starting_points:
#         starting_points -= total_hit
#         successful_shots += 1
#     elif total_hit == starting_points:
#         starting_points -= total_hit
#         successful_shots += 1
#         print(f'{player_name} won the leg with {successful_shots} shots.')
#         break
#     else:
#         unsuccessful_shots += 1
#         continue

#     if starting_points == 0:
#         print(f'{player_name} won the leg with {successful_shots} shots.')
#         break

print(3242352%10)