################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()
# print(player_health)

#There is no block scope
# game_level = 3
# def create_new_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

#Modifying Global Scope
# enemies = 1

# def increase_enemies():
#     global enemies #ADVISED AGAINST CHANGING GLOBAL VARIABLE
#     enemies += 1
#     print(f"enemies inside function: {enemies}") # will print zombies because inside local variable

# increase_enemies()
# print(f"enemies outside function: {enemies}") #will print skeletons cuz inside global variable

# instead
# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}") 
#     return enemies + 1

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Constants
PI = 3.1415

def calc():
    return PI

print(calc())

