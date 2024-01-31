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

# cards = input().split()

# team_a = ["A-" + str(number) for number in range(1,12)]
# team_b = ["B-" + str(number) for number in range(1,12)]

# is_game_terminated = False

# for card in cards:
#     if card in team_a:
#         team_a.remove(card)
#     elif card in team_b:
#         team_b.remove(card)
#     if len(team_a) < 7 or len(team_b) < 7:
#         is_game_terminated = True
#         break

# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if is_game_terminated:
#     print('Game was terminated')

#4

# to_take = [int(taken) for taken in input().split(', ')]
# count_beggars = int(input())

# final_sum = []
# starting_index = 0

# for beggar in range(count_beggars):
#     beggar_sum = 0

#     for i in range(starting_index, len(to_take), count_beggars):
#         beggar_sum += to_take[i]

#     final_sum.append(beggar_sum)
#     starting_index += 1

# print(final_sum)

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

my_list = [1,2,3]
for i in range(len(my_list)):
    print(i)