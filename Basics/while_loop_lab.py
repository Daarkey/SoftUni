#1

# text = input()

# book_counter = 0

# while True:
#     current_book = input()

#     if current_book == "No More Books":
#         print(f'The book you search is not here!')
#         print(f'You checked {book_counter} books.')
#         break

#     if text == current_book:
#         print(f'You checked {book_counter} books and found it.')
#         break

#     if current_book != text:
#         book_counter += 1


#2

# allowed_bad_grades = int(input())

# grades_sum = 0
# grade_counter = 0
# bad_grades_counter = 0
# exercise_counter = 0

# while True:
#     exercise_name = input()

#     if exercise_name == "Enough":
#         print(f'Average score: {average_grade:.2f}')
#         print(f'Number of problems: {exercise_counter}')
#         print(f'Last problem: {last_exercise}')
#         break

#     grade = int(input())

#     grade_counter += 1
#     if grade <= 4:
#         bad_grades_counter += 1
#         if bad_grades_counter >= allowed_bad_grades:
#             print(f'You need a break, {bad_grades_counter} poor grades.')
#             break
#         else:
#             grades_sum += grade
#     else:
#         grades_sum += grade

#     last_exercise = exercise_name

#     exercise_counter += 1
#     average_grade = grades_sum / grade_counter
