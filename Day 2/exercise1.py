# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
Write your code below this line 👇
sum = str( int(two_digit_number[0]) + int(two_digit_number[1]) )
print(sum)

#Or

int_sum = int(two_digit_number[0]) + int(two_digit_number[1])
str_sum = str(int_sum)
print(str_sum)

#Or

#print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)
