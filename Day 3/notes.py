print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 #create a variable to track total 
#REMEMBER: one equal sign means you are assigning a variable

#REMEMBER: two equal signs means you are checking for equality (does the number on the left equal the right?)
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill+=5
  elif age <= 18:
    bill+=7
  elif age >= 45 and age <= 55:
    print("Everything will be ok. Have a ride on us!")
  else:
    bill+=12

  photo = input("Do you want a photo taken? Type Y for yes and N for no ")
#Add $3 to the bill
  if photo == "Y":
    bill+=3
  
  print(f"Your total bill is ${bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")

# if height >= 120:
#   print("You are tall enough to ride. ")
#   age = int(input("What is your age? "))
#   if age < 12:
#     print("Please pay $5. ")
#   elif age <= 18:
#     print("Please pay $7. ")
#   elif age > 18:
#     print("Please pay $10. ")
#   else:
#     print("Please pay $12. ")
# else:
#   print("Sorry you have to grow taller! ")
