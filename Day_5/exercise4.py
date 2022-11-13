#Write your code below this row 👇

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        number = "FizzBuzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    print(number)

    OR
    
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            number+= 1
            number = "FizzBuzz"
        elif number % 3 == 0:
            number+= 1
            number = "Fizz"
        elif number % 5 == 0:
            number+= 1
            number = "Buzz"
        print(number)
