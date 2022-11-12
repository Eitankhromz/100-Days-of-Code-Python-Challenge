import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rand_name = random.randint(0, (len(names)-1))

print(f"{names[rand_name]} is going to buy the meal today!")

OR

lucky_index = random.randint(0, len(names)-1)

lucky_individual = names[lucky_index]

print(f"{lucky_individual} is going to buy the meal today! ")
