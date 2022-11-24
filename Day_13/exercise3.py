for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #Must be 'and' statement otherwise all 'FizzBuzz'
    print("FizzBuzz")
  elif number % 3 == 0: #change to elif statement (not mutually exclusive)
    print("Fizz")
  elif number % 5 == 0: #change to elif statement (not mutually exclusive)
    print("Buzz")
  else:
    print(number) #do not need brackets (printing lists w/ only one number)
