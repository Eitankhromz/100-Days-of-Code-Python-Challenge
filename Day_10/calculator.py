import clear
from art import logo
#Calculator

#Add
def add(n1, n2):
    """adds two numbers together"""
    return n1 + n2
#Subtract
def subtract(n1, n2):
    """subtracts two numbers together"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """multiplies two numbers together"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """divides two numbers together"""
    return n1 / n2

#Square Root
def sqr_root(n1):
    """finds the square root of a number"""
    return n1 ** 0.5

def sqr(n1):
    """finds the square of a number"""
    return n1 ** 2

def sqr_root_2(n1, n2):
    """finds the n2 root of n1"""
    return n1 ** (1/n2)

def sqr_2(n1, n2):
    return n1 ** n2

sign_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "#": sqr_root,
    "**": sqr,
    "&": sqr_root_2,
    "^": sqr_2,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number? \n"))
    
    operations = ""
    for operation in sign_dictionary:
        operations += " " + operation
    print(operations)

    calculate = True
    while calculate:
    
        operation_symbol = input("Pick an operation: \n")
        if operation == "**/" or operation == "**":
            calculation_function = sign_dictionary[operation_symbol]
            answer = round(calculation_function(num1), 2)
            print(f"{num1} {operation_symbol} = {answer}")
        else:
            num2 = float(input("What is the next number? \n"))
            calculation_function = sign_dictionary[operation_symbol]
            answer = round(calculation_function(num1, num2), 2)
        
        # for symbol in sign_dictionary:
        #     if operation_symbol == symbol:
        #         calculation_function = sign_dictionary[symbol]
        #         first_answer = calculation_function(num1, num2)
        
            print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        play_again = input(f"Type 'yes' to continue with {answer}, type 'no' to start a new calculation, otherwise type 'exit' to exit\n").lower()
        if play_again == "no":
            calculator()
        elif play_again == "yes":
            num1 = answer
        elif play_again == "exit":
            break
        else:
            print ("That is an invalid input")

calculator()


####MODIFIED
#Calculator
from replit import clear
from art import logo

#Add
def add(n1, n2):
  """Adds two numbers together"""
  return n1 + n2

#Subtract
def subtract(n1, n2):
  """Subtracts two numbers together"""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """Multiplies two numbers together"""
  return n1 * n2

#Divide
def divide(n1, n2):
  """divides two numbers together"""
  return n1/n2

#Square
def square(n1, n2):
  """squares n1"""
  return n1**2

#Raise to power
def power(n1, n2):
  """raises n1 to the power of n2"""
  return n1**n2

#Square root
def sqrt(n1, n2):
  """finds the square root of n1"""
  return n1**0.5

#Create a dictionary with keys being the symbols and the functions being the values
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": square,
  "^": power,
  "%": sqrt,
}

print(logo)

def calculator():
  calculator_on = True
  
  num1 = float(input("What's the first number?: "))
  for operation in operations:
      print(operation)
  
  #Create while loop that continues to calculate until user chooses no to
  while calculator_on:
    operation_symbol = input("Pick an operation: ") #Ask user to pick operation
    
    num2 = float(input("What's the next number?: ")) #Pick the second number
    
    function = operations[operation_symbol] #store key (i.e "*") in var called function
    calculation = function(num1, num2) #perform function and store in calculation
  
    print(f"{num1} {operation_symbol} {num2} = {calculation}")
    
    calculate_again = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start new calculation, otherwise type 'exit; to stop': ").lower() #ask user 
    
    if calculate_again == "n":
      clear()
      calculator()
    elif calculate_again == "y":
      num1 = calculation 
    elif calculate_again == "exit":
      calculator_on = False
    else:
      print("invalid input")
      calculator_on = False

calculator()

