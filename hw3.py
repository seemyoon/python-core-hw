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
# ###############################################################################
#
# create a class Human (name, age)
# create two classes Prince and Cinderella that inherit from Human:
# cinderella must have name, age, size of nong
# the prince must have the name, age, and size of the found shoe, as well as a method that will accept a list of cinderellas and look for the right one
#
# the cinderella class must have a count that will store the number of created instances of the class
# there must also be a class method that will display this value
#
#
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
#
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
# to check the cassets, use the isinstance method, example:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
