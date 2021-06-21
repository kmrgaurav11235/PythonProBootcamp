# Review: 
# Create a function called greet(). 
# def greet():
    # Write 3 print statements inside the function.
    # print("Hi")
    # print("How are you?")
    # print("Isn't the weather nice today?")
# Call the greet() function and run your code.
# greet()

# Function that allows input
def greet_with_name(name): # name is parameter
    print(f"Hi {name}")
    print(f"How are you, {name}?")
    print(f"Isn't the weather nice today, {name}?")

greet_with_name("Gaurav") # "Gaurav" is agrument
greet_with_name("Fingolfin")
