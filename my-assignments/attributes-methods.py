# -----------------------------------------------------------------------
# SAMPLE
print('\nSAMPLE')

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
# CHALLENGE 1
print('\nCHALLENGE 1')

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


# -----------------------------------------------------------------------
# CHALLENGE 2
print('\nCHALLENGE 2')

# TODO: Each object should have the following attributes:
# name - name of the city you picked
# country - the country the city is located in
# temperature - the city's temperature in F. 
# latitude - city's latitude coordinate 
# longitude - city's longitude coordinate 

# Location class
class Location:
    def __init__(self, name: str, country: str, 
                 temperature: float, latitude: float, longitude: float):
        self.name = name
        self.country = country
        self.temperature = temperature
        self.latitude = latitude
        self.longitude = longitude

# TODO: Instantiate three locations. Instaniate each location with the correct values for 
# name, country, temperature, latitude, longitude. For the last three look up the correct 
# values! Use the current teperature and the actual latitude and longitude. 

chicago = Location(name='Chicago', country='United States of America',
                   temperature=65, latitude=41.881832, longitude=-87.623177)

osaka = Location(name='Osaka', country='Japan',
                   temperature=57, latitude=34.672314, longitude=135.484802)

porto = Location(name='Porto', country='Portugal',
                   temperature=67, latitude=41.150223, longitude=-8.629932)

# TODO: Using the object variable names, create a list of Location objects called bucketlist.
bucket_list = [chicago, osaka, porto]

# TODO: Using the loop print the name of the city of each location in bucketlist. 
[print(city.name) for city in bucket_list]

# TODO: Loop over your locations and print only locations above the equator. 
# Latitude represents how far above or below the equator a location is. Positive numbers 
# are above the equator negative numbers are below. 
for city in bucket_list:
    if city.latitude > 0:
        print(f"{city.name} is above the equator")

# TODO: Using the loop, loop through the objects to find which location has the warmest weather
max_attr = max(bucket_list, key=lambda x: x.temperature)
print(f"The city with the highest temperature is: {max_attr.name}")


# -----------------------------------------------------------------------
# CHALLENGE 2.5
print('\nCHALLENGE 2.5')

# Students Class
class Student:
    # class attributes are shared by all instances
    school = "Make School"
    location = "San Francisco"
    major = "Computer Science"


# TODO: Instantiate 2 object of type Student
jhene = Student()
kehlani = Student()

# TODO: Access class attributes using dot notation. Run this code and check the output

print(f"Jhene studies {jhene.major} at {jhene.school} in {jhene.location}.")
print(f"Kehlani studies {kehlani.major} at {kehlani.school} in {kehlani.location}.")

# TODO: Print the  __dict__ attribute to for each object to see a dictionary of all the attributes defined for the object itself.

print(jhene.__dict__)
print(kehlani.__dict__)

# TODO: Answer the question: Why is it blank? 
# I think because school, location and major are all class attributes instead of instance attributes.

# TODO: Remove the comment on the line below: 
print(Student.__dict__)

# TODO: Answer the questions: 
# What attributes do I see in the Student class object? 
# Is Student an instance of Student or is it something else?

# I see the 'school', 'location' and 'major' attributes.
# Student is not an instance of Student, it is the class.

# Imagine that Make School moves to San Rafael!
# We can update the class variable for all instances by:

# TODO: Uncomment the line below
Student.location = "San Rafael"

# TODO: Uncomment the lines below and run your code.
# Here you are printing the location for each student again.

print(f"Jhene studies in {jhene.location}.")
print(f"Kehlani studies in {kehlani.location}.")

# TODO: Kehlani transfered , update her school to UCLA.
# Uncomment these lines:

kehlani.school = "UCLA"
print(kehlani.school)

# Do you think that the name of the school will change for Jhene too? Test it.
# TODO: Predict what you think will happen. Is jhene going to UCLA or are they
# still in San Rafael?

print(jhene.school) 

# What happened?
# Looks like kehlani.school = 'UCLA' overode the class attribute and updated it to UCLA.
# this effectively changed the instance attribute

# Print the __dict__ for kehlani
print(kehlani.__dict__)
# Now kehlani has instance attributes!