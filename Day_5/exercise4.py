#Write your code below this row 👇

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        number = "FizzBuzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    print(number)
