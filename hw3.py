from typing import Self
from abc import ABC, abstractmethod


# Create a Rectangle class:
# -it must take two sides x,y
# -describe the behavior for arithmetic methods:
# + the sum of the planes of two instances of the class
# - the difference of the planes of two instances of the class
# == planes for equality
# != planes for inequality
# >, < less than more than
# when calling the len() method, calculate the sum of the sides
#

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__dict__)

    def area(self):
        return self.x * self.y

    def __add__(self, other: Self):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __len__(self):
        return self.x + self.y


first_rectangle = Rectangle(5, 3)
second_rectangle = Rectangle(4, 6)
print('first rectangle: ', first_rectangle)
print('common sum of shapes: ', first_rectangle + second_rectangle)
print('subtract of shapes: ', first_rectangle - second_rectangle)
print('eq of shapes: ', first_rectangle == second_rectangle)
print('not eq of shapes: ', first_rectangle != second_rectangle)
print('sum of sides: ', len(first_rectangle))
print('> : ', first_rectangle > second_rectangle)
print('< : ', first_rectangle < second_rectangle)


# ###############################################################################
#
# create a class Human (name, age)
# create two classes Prince and Cinderella that inherit from Human:
# cinderella must have name, age, size of foot
# the prince must have the name, age, and size of the found shoe, as well as a method that will accept a list of cinderellas and look for the right one
#
# the cinderella class must have a count that will store the number of created instances of the class
# there must also be a class method that will display this value
#
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Cinderella(Human):
    counter: int = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.counter += 1

    def get_counter(self):
        return self.counter


class Prince(Human):
    def __init__(self, name: str, age: int, found_size_of_foot: int):
        super().__init__(name, age)
        self.found_size_of_foot = found_size_of_foot

    def to_find_cinderella(self, *args: Cinderella) -> str:
        found_cinderella = None
        for cinderella in [*args]:
            if cinderella.foot_size == self.found_size_of_foot:
                found_cinderella = cinderella.name
                break

        if found_cinderella: return f'Congratulation dear {cinderella.name}, i have found you ❤'

        return f'Unfortunately, but i could\'t find my love 😔'


prince = Prince('Christopher', 20, 30)
cinderella1 = Cinderella('Alla', 21, 36)
cinderella2 = Cinderella('Ella', 18, 30)
cinderella3 = Cinderella('Fauna', 25, 33)
cinderella4 = Cinderella('Liza', 24, 40)

print(cinderella4.get_counter())

to_find_cinderella = prince.to_find_cinderella(
    cinderella1,
    cinderella2,
    cinderella3,
    cinderella4,
)

print(to_find_cinderella)


# ###############################################################################
#
# 1) Create an abstract class Printable that will describe the abstract print() method
# 2) Create the Book and Magazine classes, each with a name variable in the constructor, and which inherit from the Printable class
# 3) Create the Main class in which there will be:
# - a variable of the printable_list class that will store books and magazines
# - the add method with which you can add class instances to the list and check whether what is being passed is a Book or Magazine class, otherwise ignore the addition
# - method show_all_magazines which will display all magazines by calling the print method of an abstract class
# - the show_all_books method that will display all books by calling the print method of an abstract class
#
# Example:
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
#
# to check class, use the isinstance method, example:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

class UserTest:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Printable(ABC):

    @abstractmethod
    def print(self):
        print(self)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book name: {self.name}")


class Magazine(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine name: {self.name}")


class Main:
    printable_list = []

    def __init__(self):
        pass

    def add(self, instance: object):
        if isinstance(instance, (Magazine, Book)): return self.printable_list.append(instance)
        raise TypeError('Wrong class!')

    def show_all_magazines(self):
        for item in self.printable_list:
            if isinstance(item, Magazine):
                item.print()

    def show_all_books(self):
        for item in self.printable_list:
            if isinstance(item, Book):
                item.print()


book1 = Book('1984')
book2 = Book('Buratino')

magazine1 = Magazine('Deadpool')
magazine2 = Magazine('Spider-man')
magazine3 = Magazine('Iron-man')

test_user = UserTest('vanya', 20)

main_instance = Main()
main_instance.add(book1)
main_instance.add(book2)

main_instance.add(magazine1)
main_instance.add(magazine2)
main_instance.add(magazine3)
main_instance.add(magazine3)

# main_instance.add(test_user)

main_instance.show_all_books()
main_instance.show_all_magazines()
