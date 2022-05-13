# #import random module
# import random
# import my_module
# #creating a variable that holds a random integer between 1 and 10
# random_integer = random.randint(1, 10)
# print(random_integer)
# # print(my_module.pi)

# #random float
# random_float = random.random()
# print(random_float)

# #random float between range
# random_float_multi = random.random() * 5 #prints random number between 0.00000 and 4.999999
# print(random_float_multi)

# random_float_uniform = random.uniform(1, 10)
# print(random_float_uniform)

# #What is a module?
# #splits large code up into individual modules
# # each module is responsible for a different bit of functionality

#Lists
states_of_america = ["New Jersey", "New York", "Florida"]
# print(states_of_america[0])
#if you put in a negative number, will start counting from the bottom of the list
# print(states_of_america[-1])

#can change speciifc items in list
states_of_america[0] = "New Joisey"
#print(states_of_america)

#can add items to list
states_of_america.append("Eitanland")
#or
states_of_america.insert(len(states_of_america), "Wyoming")
#print(states_of_america)

#can extend items in list
states_of_america.extend(["California", "Hawaii", "Utah"])
#print(states_of_america)

#count the amount of times a specific items appears in list
#print(states_of_america.count("Utah"))

#Nested Lists
# dirty_dozen = ["Strawberry", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][2])
