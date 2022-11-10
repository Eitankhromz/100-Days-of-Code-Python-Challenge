# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Change age data type to int or float
int_age = int(age)

#subtract current age from 90 
howLong = 90 - int_age

#calculate days, weeks, and months
daysLeft = round(howLong * 365)
weeksLeft = round(howLong * 52)
monthsLeft = round(howLong * 12)

#print using f-string
print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")

OR

years_left = 90 -int(age)

days = int(years_left) * 365
weeks = int(years_left) * 52
months = int(years_left) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


