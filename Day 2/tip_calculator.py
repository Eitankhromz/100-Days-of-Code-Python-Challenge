#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Welcome
print("Welcome to the tip calculator!") 

#assign variable to input of user & change data type from str to int or bool
bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
peoples = int(input("How many people to split the bill? "))

#prepare for multiplying tip
int_tip_amount = (tip_amount /100) + 1

#calculate total with tip & divide by group amount
total_bill = bill * int_tip_amount
perPerson = total_bill/ peoples

#format perPerson with correct amount of decimal places 
final_amt = "{:.2f}".format(perPerson)

#print result using f-string
print(f"Each person should pay: ${final_amt}")
