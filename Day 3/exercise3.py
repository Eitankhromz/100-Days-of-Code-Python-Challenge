# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

 # 11/11 Solution

#Write your code below this line 👇
# if year % 4 != 0:
#     print("Not a leap year.")
# else:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
    
    
