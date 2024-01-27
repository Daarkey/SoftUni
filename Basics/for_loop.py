#1

# for num in range(1, 101):
#     print(num)


# #2

# num = int(input())

# for n in range(1, num + 1 ,3):
#     print(n)

#3

# num = int(input())

# for n in range(0, num + 1):
#     if n % 2 == 0:
#         print(2**n)

#4

# num = int(input())

# for i in range(num, 0, -1):
#     print(i)

#5

# user_input = input()

# for i in user_input:
#     print(i)


#6

# user_input = input()

# value = 0

# for i in user_input:
#     if i == 'a':
#         value += 1
#     elif i == 'e':
#         value += 2
#     elif i == 'i':
#         value += 3
#     elif i == 'o':
#         value += 4
#     elif i == 'u':
#         value += 5

# print(value)


#7

# num = int(input())

# value = 0

# for n in range(1, num + 1):
#     n = int(input())
#     value += n

# print(value)


#8

# from sys import maxsize

# num = int(input())

# max_num = - maxsize
# min_num = maxsize

# for i in range(num):
#     current_num = int(input())
#     if current_num >max_num:
#         max_num = current_num

#     if current_num < min_num:
#         min_num = current_num

# print(f'Max number: {max_num}')
# print(f'Min number: {min_num}')


#9

# num = int(input())

# result_left = 0
# result_right = 0


# for i in range(num):
#     num1 = int(input())
#     result_left += num1

# for i in range(num):
#     num2 = int(input())
#     result_right += num2

# if result_left == result_right:
#     print(f'Yes, sum = {result_right}')
# else:
#     difference = abs (result_left - result_right)
#     print(f'No, diff = {difference}')


#10

# num = int(input())

# sum_odd = 0
# sum_even = 0

# for i in range(num):
#     current_num = int(input())
#     if i % 2 == 0:
#         sum_even += current_num
#     else:
#         sum_odd += current_num

# if sum_odd == sum_even:
#     print('Yes')
#     print(f'Sum = {sum_even}')
# else:
#     print('No')
#     difference = abs(sum_odd - sum_even)
#     print(f'Diff = {difference}')