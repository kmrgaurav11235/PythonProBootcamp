# Unlimited keyword arguments for a function / method
# *args : Single '*' means unlimited positional arguments
# **kwargs: Double '**' means unlimited positional arguments

def display(**kwargs):
    # kwargs is a dictionary
    print(type(kwargs))
    print(kwargs)

    # We can use kwargs like a dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)

    # Or we can just use the names of the key
    print(f"value1 = {kwargs['value1']}")
    print(f"value2 = {kwargs['value2']}")


display(value1=3, value2=5)


# We can use normal and args/kwargs together
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(n=4, multiply=4, add=3))


# Class with kwargs
class Car:
    def __init__(self, **kw):
        # The benefit of using get() over [] is that it doesn't throw the KeyError. It just returns 'None'.
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

my_car = Car(make="BMW")
print(my_car.model)  # prints 'None'
