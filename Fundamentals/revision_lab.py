#1

# name = input()

# if name == 'Johnny':
#     print('Hello, my love!')
# else:
#     print(f'Hello, {name}!')


#2

# age = int(input())

# if age <= 14:
#     print('drink toddy')
# elif age <= 18:
#     print('drink coke')
# elif age <= 21:
#     print('drink beer')
# else:
#     print('drink whisky')


#3

# messages = int(input())

# for i in range(messages):
#     number = int(input())

#     if number == 88:
#         print('Hello')
#     elif number == 86:
#         print('How are you?')
#     elif number != 88 and number != 86 and number < 88:
#         print('GREAT!')
#     elif number > 88:
#         print('Bye.')


#4

# divisor = int(input())
# boundary = int(input())

# largest = 0

# while True:

#     if boundary % divisor != 0:
#         boundary -= 1
#     else:
#         print(boundary)
#         break


#5

# orders = int(input())

# total_price = 0

# for i in range(orders):

#     capsule_price = float(input())
#     days = int(input())
#     capsules_per_day = int(input())

#     if capsule_price < 0.01 or capsule_price > 100:
#         continue
#     if days < 1 or days > 31:
#         continue
#     if capsules_per_day < 1 or capsules_per_day > 2000:
#         continue

#     price = capsule_price * days * capsules_per_day

#     print(f'The price for the coffee is: ${price:.2f}')

#     total_price += price

# print(f'Total: ${total_price:.2f}')


#6

# string_num = int(input())

# for i in range(string_num):

#     string = input()

#     for char in string:
#         if char == ',' or char == '.' or char == '_':
#             print(f'{string} is not pure!')
#             break
#     else:
#         print(f'{string} is pure.')


#7

# command = ''

# while True:

#     command = input()

#     if command == 'End':
#         break

#     if command != 'SoftUni':
#         for char in command:
#             print(char * 2, end='')
#     else:
#         continue

#     print()


#8

# command = ''
# coffees = 0

# while True:

#     command = input()

#     if command == 'END':
#         print(coffees)
#         break

#     if coffees > 5:
#         print("You need extra sleep")
#         break

#     if command in ['coding', 'dog', 'cat', 'movie']:
#         coffees += 1
#     elif command in ['CODING', 'DOG', 'CAT', 'MOVIE']:
#         coffees += 2
#     else:
#         continue


#9

# command = ''

# while True:

#     command = input()

#     if command == 'Welcome!':
#         print("Welcome to Hogwarts.")
#         break

#     if command == 'Voldemort':
#         print("You must not speak of that name!")
#         break

#     if len(command) < 5:
#         print(f'{command} goes to Gryffindor.')
#     elif len(command) == 5:
#         print(f'{command} goes to Slytherin.')
#     elif len(command) == 6:
#         print(f'{command} goes to Ravenclaw.')
#     elif len(command) > 6:
#         print(f'{command} goes to Hufflepuff.')


#10

string1 = input()
string2 = input()

current_string = ''

for i in range(0, len(string2)):

    for j in range(0,len(string1)):

        if string2[j] != string1[i]:

            if current_string == string2:
                continue

            current_string = string2.replace(string2[j], string1[i], 1)
            print(current_string)
        else:
            continue
    


#11

# budget = float(input())
# price_flour = float(input())

# price_eggs = price_flour * 0.75
# price_milk_1l = price_flour + price_flour * 0.25

# price_milk_250ml = price_milk_1l / 4

# bread_cost = price_eggs + price_milk_250ml + price_flour

# current_sum  = 0
# colored_eggs = 0
# bread_counter = 0

# while True:

#     if (current_sum + bread_cost) >= budget:
#         break

#     if (current_sum + bread_cost) < budget:
#         bread_counter += 1
#         colored_eggs += 3
#         current_sum += bread_cost

#         if bread_counter % 3 == 0:
#             colored_eggs -= bread_counter - 2

# print(f'You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {(budget - current_sum):.2f}BGN left.')


#12

