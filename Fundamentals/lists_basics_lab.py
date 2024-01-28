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

factor = int(input())
count = int(input())

# my_list = [factor]

# for i in range(factor, count + 1):
#     new_num = i * factor
#     my_list.append(new_num)

# print(my_list)

my_list = []

for i in range(1, count + 1):
    new_num = i * factor
    my_list.append(new_num)

print(my_list)