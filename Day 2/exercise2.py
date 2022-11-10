# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#BMI = weight/(height ** 2)

# Change weight and height data type from str to float
int_height = float(height)
int_weight = float(weight)

#Complete BMI Calculation
bmi = int_weight / int_height ** 2

#		OR

bmi = float(weight) / float(height) ** 2 
print(int(bmi))

# print bmi result
print(int(bmi))

