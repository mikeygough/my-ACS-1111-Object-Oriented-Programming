# pi is a global variable
# it can be used inside of functions, but not modified unless
# it is introduced with the 'global' keyword
pi = 3.14

def calculate_circle_circumference(radius):
    """ returns the stringified circumference of a circle with radius and pi=3.14 """
    # radius is a local variable
    return "{:.2f}".format(2 * pi * radius)

def calculate_circle_area(radius):
    """ returns the stringified area of a circle with radius and pi=3.14 """
    # radius is a local variable
    return "{:.2f}".format(pi * radius ** 2)


print("Circumference:", calculate_circle_circumference(5)) # -> 31.40
print("Area:", calculate_circle_area(5)) # -> 78.50

print("Pi:", pi) # -> 3.14
print(radius) # -> NameError: name 'radius' is not defined