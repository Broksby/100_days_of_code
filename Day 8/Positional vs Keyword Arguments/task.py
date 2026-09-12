# Functions with input

#def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")

def greet_with_name(name, location, time):
    print(f"Hello, {name}! You have successfully logged in from {location}. It is {time}")

greet_with_name(time="Now", location="The Moon", name="Neil")