def add(*args):
    # print(args[0]) #unlimited positional argument

    sum = 0
    for num in args:
        sum+= num
    return sum


# print(add(1, 2, 3, 4))

def calculate(n, **kwargs):
    print(kwargs) #creates a dictionary of the keyword arguments
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)

