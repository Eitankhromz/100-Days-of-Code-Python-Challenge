
Exercise 4:
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#guard against any uppercase letters
lower_name1 = name1.lower()
lower_name2 = name2.lower()
#combine strings into one
combined = lower_name1 + lower_name2
#set up a counter
count = 0
#create variables to hold the amount of each letter
t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")
#add instances of each letter to true
true = t + r + u + e

l = combined.count("l")
v = combined.count("v")
o = combined.count("o")
#add instance of each letter to variable love
love = l + o + v + e
#store string versions of love and true in variable
str_lovescore = str(true) + str(love)
lovescore = int(str_lovescore) #change into int data type
#if/elif/else statements
if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore > 40 and lovescore < 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")

