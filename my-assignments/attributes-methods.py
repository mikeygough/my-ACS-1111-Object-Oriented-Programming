# -----------------------------------------------------------------------
# CHALLENGE 1

# Created the Dog class
class Dog:
    pass

# Instatiation
jess_dog = Dog()

# TODO: Create an instance of Dog and assign it to a variable
ralph = Dog()

# Create attributes for jess_dog object, using dot notation.
# Like variables, if attribute did not exist, it is created when you first assign it a value.

jess_dog.name = "Tara"
jess_dog.age = 1
jess_dog.color = "brown"
jess_dog.cuteness_level = 10

# TODO: Add four attrbutes to your dog instance. Give each a value that describes your dog.

ralph.name = "Ralph"
ralph.age = 42
ralph.color = "silver"
ralph.cuteness_level = 8

# Update attributes similar to how you would update a variable.

jess_dog.age += 1
print(f"My age is {jess_dog.age}")

# TODO: Update the some of the attributes of your dog instance. Assign a new value 
# to one of the existing attributes of your dog. 

ralph.age += 1

# The name attribute 
print(f"My name is {jess_dog.name}")

# TODO: Print one or more of your dog's attributes:
print(f"My name is {ralph.name}. I am {ralph.age} years old with {ralph.color} fur.")

# Delete a property from an object with del

del jess_dog.name
print(f"My age is {jess_dog.age}")

# TODO: Delete one of the attributes of your dog. 
del ralph.cuteness_level

# Rather than having to print all of the attributes one by one, we can use __dict__
print(jess_dog.__dict__)

# TODO: Check the attrbutes of your dog by printing yourdog.__dict__. This should 
# show you all of the attribues that exist on your dog. 
print(ralph.__dict__)


# -----------------------------------------------------------------------
# CHALLENGE 2

# TODO: We need to define a Dog class. All dogs will have the following 
# attributes. Define these on the class Dog below. 

# name
# breed 
# fave_snack

# By defining these attributes on the class all dog instances will have them. 
# Remember! attributes are initialized in the __init__ method! 

# Dog class
class Dog:
    def __init__(self, name: str, breed: str, fave_snack: str):
        self.name = name
        self.breed = breed
        self.fave_snack = fave_snack

# TODO: Instantiate 3 objects of type Dog
dog_1 = Dog(name='Bandi', breed='Corgi', fave_snack='Socks')
dog_2 = Dog(name='Goose', breed='German Shephard', fave_snack='Chickens')
dog_3 = Dog(name='Bowser', breed='Sharpe', fave_snack='Toy Stuffing')

# TODO: Using the object variable names, create a list of Dog objects called dogs.
dogs = [dog_1, dog_2, dog_3]

# TODO: Using the loop print the names of the dogs
[print(dog.name) for dog in dogs]

# TODO: Using a loop, delete breed attribute for all the dogs in the list dogs
for dog in dogs:
    del dog.breed

# TODO: Using a loop, add an attribute 'species' and assign it the value 'canine'
for dog in dogs:
    dog.species='canine'

# TODO: Use the __dict__ attribute to print each dog and check it's attributes and values 
# use a loop to print __dict__ for each dog in your list. 
[print(dog.__dict__) for dog in dogs]