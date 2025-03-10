from typing import Callable


# 1) to write a closure function that will store a list of cases, you need to implement two methods:
# - the first writes a new case to the list
# - the second returns all entries
def notebook() -> tuple[Callable[[str], None], Callable[[], None]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> None:
        nonlocal todo_list
        print(todo_list)

    return add_todo, get_all


add_todo, get_all = notebook()
add_todo('brush teeth')
add_todo('PT')
add_todo('do hw')

get_all()


# 2) counterpart the first task


# 3) create a function that will return the sum of the digits of a number as a string (we also use typing)

def sum_of_digits(value: int) -> str:
    new_str_value = str(value)
    res = []
    for idx, digit in enumerate(new_str_value):
        if digit != '0':
            res.append(digit + '0' * (len(new_str_value) - idx - 1))
    return ' + '.join(res)


print(sum_of_digits(10))


# Example:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
# 4) create a decorator that will count the number of times the function was run by this decorator, and will display this value after the function is executed
def decor(func):
    count = 0

    def inner_func(*arg, **kwargs):
        nonlocal count
        count += 1
        res = func(*arg, **kwargs)
        print(f'this func was called {count} times')
        return res

    return inner_func


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()

