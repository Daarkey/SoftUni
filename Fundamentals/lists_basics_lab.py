#1

# string = input()
# list_of_string = []
# new_list = []

# for i in string.split():
#     list_of_string.append(int(i))

# for num in list_of_string:
#     current_num = num
#     current_num = -1 * current_num
#     new_list.append(current_num)

# print(new_list)


#2

# factor = int(input())
# count = int(input())

# # my_list = [factor]

# # for i in range(factor, count + 1):
# #     new_num = i * factor
# #     my_list.append(new_num)

# # print(my_list)

# my_list = []

# for i in range(1, count + 1):
#     new_num = i * factor
#     my_list.append(new_num)

# print(my_list)


#3

# red_card = input()

# list_of_red_cards = red_card.split()

# print(f"Team A - {final_a_players}; Team B - {final_b_players}")

# if team_a_player_count >= 7 and team_b_player_count >=7:


#4

# int_string = input()
# count_beggars = int(input())
# splitted_string_list = int_string.split(", ")

# # for i in range(0, len(splitted_string_list) - 1):
# #     if i % 2 == 0:
# #         splitted_string_list[i] =
# more_beggars = len(splitted_string_list) - count_beggars
# if more_beggars < 0:
    


#5

# cards_string = input()
# num_shuffles = int(input())

# cards_list = cards_string.split()

# for i in range(num_shuffles):
#     first_half = cards_list[:len(cards_list)//2]
#     second_half = cards_list[len(cards_list)//2:]
#     cards_list = [c for pair in zip(first_half, second_half) for c in pair]

# print(cards_list)


#6

# list_nums = input()
# numbers = int(input())

# int_list_nums = [int(i) for i in list_nums.split()]

# for _ in range(numbers):
#     small_num = min(int_list_nums)
#     int_list_nums.remove(small_num)

# str_list_nums = [str(j) for j in int_list_nums]
# print((", ").join(str_list_nums))


