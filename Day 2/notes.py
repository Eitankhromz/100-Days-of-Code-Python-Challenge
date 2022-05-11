#Data Types

#String
print("Hello"[0]) #adding the number is called subscripting
print("Hello"[4]) #the last character "o" is printed here

#"123" #this is not treated as a number but a STRING
print("123" + "345")

#Integer (numbers without decimal places)
print(123 + 456)

#Float (Decimal point "floats" around number)

#Boolean
True
False



num_char = len(input("What is your name? \n"))
#print("Your name has " + num_char + " characters. ")

#print(type(num_char)) #type function to know what type the variable is
new_num_char = str(num_char) # converting int into str

print("Your name has " + new_num_char + " characters")



# print( 2**3)

# PEMDASLR
# ()
# **
# * / #multiplication and division equal
# + - #addition and subtraction equal

# print(3 * 3 + 3 / 3 - 3) #will equal 7
# print(3 * 3 / 3 + 3 - 3) will equal 3
print(3 * (3 + 3) / 3 - 3)



# print(round(8 / 3, 2)) #round function rounds numbers to specific decimal places
# print(8//3) #flaw division cuts the number into an int

# result = 4 / 2
# result/= 2
# print(result)
# score+=1 is the same as score = score + 1

score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score {score}, your height is {height}, you are winning is {isWinning}")




