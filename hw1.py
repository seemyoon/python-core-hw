import re

# strings
#
# 1) write a program that selects numbers (1, 2, but not like 465) from an input string and outputs them separated by commas,
# for example:
# st = 'as 23 fdfdg544' input string
# 2,3,5,4,4 #output to the console.
print('task 1:\n')
st = 'as 23 fdfdg544'
for elem in st:
    if elem.isdigit(): print(elem)

# #################################################################################
# 2) write a program that selects numbers (564, not only 5) from the input string and outputs them
# as they are written
# for example:
# st = 'as 23 fdfdg544 34' #input string
# 23, 544, 34 #output to the console

print('task 2:\n')
st2 = 'as 23 fdfdg544'
list_of_nums = [int(num) for num in re.findall('\d+', st2)]
for num in list_of_nums:
    print(num)

print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st2).split()))

# #################################################################################
# list comprehension
#
# 1) there is a string:
# greeting = 'Hello, world'
# write each character as a separate list element and make it uppercase:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello, world'
res = [letter.capitalize() for letter in greeting]
print(res)
#
# 2) from the range 0-50 write down only odd numbers and square them
# example:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
list_of_all_nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484,
                    529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600,
                    1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
new_list_of_all_nums = []
for num in list_of_all_nums:
    if num % 2 == 0:
        pass
    else:
        new_list_of_all_nums.append(num ** 2)
print(new_list_of_all_nums)


# function
#
# - create a function that prints a list
def create_list():
    print([12, 88, 77])


create_list()


# - create a function that takes three numbers and prints and returns the largest.
def output_the_largest_number(first_num, second_num, third_num):
    return max(first_num, second_num, third_num)


print(output_the_largest_number(1, 10, 6))


# - create a function that takes any number of numbers, returns the smallest, and outputs the largest
def output_the_number(*args):
    print(max(args))
    return min(args)


output_the_number(6, 45, 84, 355)


# - create a function that returns the largest number from a list
def output_the_largest_number_from_the_list(*args):
    return max(args)


list_of_any_quantity_in_the_list = [3, 5, 774, 32055, 88989, 1000]
print(output_the_largest_number_from_the_list(*list_of_any_quantity_in_the_list))


# - create a function that returns the smallest number from the list
def output_the_smallest_number(*args):
    return min(args)


print(output_the_smallest_number(*list_of_any_quantity_in_the_list))


# - create a function that takes a list of numbers and adds up the values ​​of the elements of the list and returns it.
def take_list_of_nums(passed_list):
    return sum(passed_list)


print(take_list_of_nums(list_of_any_quantity_in_the_list))


# - create a function that takes a list of numbers and returns the arithmetic mean of its values.
def take_list_of_nums(passed_list):
    return sum(passed_list) / len(passed_list)


print(take_list_of_nums(list_of_any_quantity_in_the_list))

# ################################################################################################
# 1) Given a list:
# list = [22, 3,5,2,8,2,-23, 8,23,5]
# - find the min number
new_list_of_all_nums2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(min(new_list_of_all_nums2))
# - remove all duplicates
print(list(dict.fromkeys(new_list_of_all_nums2)))
# - replace every 4th value with 'X'
new_list_of_all_nums3 = [2, 8, 2, -2, 59, 802, 3, 5]
for index in range(3, (len(new_list_of_all_nums3)), 4):
    new_list_of_all_nums3[index] = 'X'

print(new_list_of_all_nums3)


# 2) print an empty square with "*" the side of which is specified as an argument to the function
def output_square(side: int):
    i = 0
    while i < side:
        if i == 0 or i == side - 1:
            print('*' * side)
        else:
            print(f'*{' ' * (side - 2)}*')
        i += 1


output_square(5)
# 3) print the multiplication table using a while loop
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(list_of_nums):
    print(f'multiplication by {i + 1}')
    for num in list_of_nums:
        print(f'{i} x {num} = {i * num}')
    i += 1

# 4) rework this task under the menu
selected_option = 0

while selected_option not in range(1, 5):
    print('hello, choose the number, that you want to launch:')
    print('press 1 to work with list')
    print('press 2 to represent empty square')
    print('press 3 to show the multiplication table')
    print('press 4 to quit')
    try:
        selected_option = int(input('please enter your choice (1-4): '))
    except ValueError as e:
        print('Invalid input. Please enter a number between 1 and 4.')
        continue

if selected_option == 1:
    print('enter list of numbers, like [1, 2, 3...]')
    selected_option = input('your list: ')
    try:
        user_list = list(map(int, selected_option.replace(' ', '').split(',')))
        print('your list:', user_list)

        selected_option_with_list = 0
        while user_list and selected_option_with_list not in range(1, 5):
            print('choose the number, that you want to do with list:')
            print('press 1 to find the min number')
            print('press 2 to delete duplicates')
            print('press 3 to replace every 4th value with "X"')
            print('press 4 to quit')
            try:
                selected_option_with_list = int(input('please enter your choice (1-4): '))
            except ValueError as e:
                print('Invalid input. Please enter a number between 1 and 4.')
                continue

        if selected_option_with_list == 1:
            print('min number:', min(user_list))

        elif selected_option_with_list == 2:
            print(list(dict.fromkeys(user_list)))

        elif selected_option_with_list == 3:
            for index in range(3, (len(user_list)), 4):
                user_list[index] = 'X'
            print(user_list)

        elif selected_option_with_list == 4:
            print('goodbye!')

        else:
            print('invalid choice, please select a number between 1 and 4.')

    except ValueError as e:
        print('faulty input')

elif selected_option == 2:
    print('enter size of side, like 5')
    selected_option_side = int(input('your input: '))
    try:
        i = 0
        while i < selected_option_side:
            if i == 0 or i == selected_option_side - 1:
                print('*' * selected_option_side)
            else:
                print(f'*{' ' * (selected_option_side - 2)}*')
            i += 1

    except ValueError as e:
        print('faulty input')

elif selected_option == 3:
    list_of_possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('you chose to show the multiplication table.')
    i = 0
    while i < len(list_of_nums):
        print(f'multiplication by {i + 1}')
        for num in list_of_nums:
            print(f'{i} x {num} = {i * num}')
        i += 1

elif selected_option == 4:
    print('goodbye!')

else:
    print('invalid choice, please select a number between 1 and 4.')
