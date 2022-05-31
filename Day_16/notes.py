# import another_module
# print(another_module.another_variable)
#
# # import turtle
# # timmy = turtle.Turtle()
# #OR
# # from [module] import [class], [class]
# from turtle import Turtle, Screen
# # object = class(a.k.a blueprint)
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
#
# # [object] = [class or blueprint]
# my_screen = Screen()
# #     [object].[attribute]
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "c")
table.add_column("Type", ["Electric", "Water", "Fire"], "c")
table.align = 'l'

print(table.align)


print(table)

