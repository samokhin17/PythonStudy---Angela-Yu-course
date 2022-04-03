# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('black', 'red')
# timmy.speed(1)
# timmy.circle(50)
# timmy.forward(100)
# timmy.circle(50)
# timmy.right(90)
# timmy.forward(200)
# timmy.circle(-50)
# timmy.circle(-50, 180)
# timmy.forward(200)
#
# # for i in range(4):
# #     timmy.forward(100)
# #     timmy.left(90)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table.align)
table.align = 'l'
print(table.align)

print(table)
