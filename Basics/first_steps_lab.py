#1
# dollar = 1.79549

# lev = float(input())

# print(lev*dollar)

#2
# from math import pi

# radians = float(input())
# print(radians * 180/pi)

#3

# deposit = float(input())
# time = int(input())
# year_percent = float(input())

# year_percent = year_percent / 100
# interest_per_month = (deposit * year_percent)/12

# print(deposit + time * interest_per_month)

#4

# number_pages = int(input())
# pages_per_hour = int(input())
# number_days = int(input())

# total_time_book = (number_pages/pages_per_hour)
# hours_per_day = (total_time_book/number_days)

# print(int(hours_per_day))

#5

# price_packet_pens = 5.80
# price_packet_markers = 7.20
# price_cleaning_liquid = 1.20

# packet_pens = int(input())
# packet_markers = int(input())
# cleaning_liquid = int(input())
# discount = int(input())
# discount = discount / 100
# sum = price_packet_pens*packet_pens + price_packet_markers*packet_markers + price_cleaning_liquid*cleaning_liquid

# print(sum - (sum * discount))

#6

# price_naylon = 1.50
# price_paint = 14.50
# price_paint_desolver = 5
# plastic_bag = 0.4

# naylon = int(input())
# paint = int(input())
# paint_desolver = int(input())
# hours_work = int(input())

# naylon = naylon + 2
# paint = paint + (paint * (10/100))

# sum = naylon*price_naylon + paint*price_paint + paint_desolver*price_paint_desolver + plastic_bag

# price_work = ((sum * (30/100)) * hours_work)

# print(sum + price_work)

#7

# price_chicken = 10.35
# price_fish = 12.40
# price_vegetarian = 8.15
# delivery = 2.50

# num_chicken = int(input())
# num_fish = int(input())
# num_vegetarian = int(input())

# sum = num_chicken*price_chicken + num_fish*price_fish + num_vegetarian*price_vegetarian
# price_desert = sum * (20/100)

# print(sum + delivery + price_desert)

#8

# year_fee = int(input())
# shoes = year_fee - (year_fee * (40/100))
# clothes = shoes - (shoes * (20/100))
# ball = clothes * 0.25
# accessories = ball * 0.2

# print(year_fee + shoes + clothes + ball + accessories)

#9

# length = int(input())
# height = int(input())
# width = int(input())
# percent = float(input())
# percent = percent / 100

# aquarium_volume = length * height * width
# aquarium_liters = aquarium_volume / 1000

# print(aquarium_liters * (1 - percent))
