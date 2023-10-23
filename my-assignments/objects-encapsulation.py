# Classes are a blueprint
class CoffeeOrder:
  def __init__(self, name, coffee_type, has_milk):
    self.name = name
    self.type = coffee_type
    self.has_milk = has_milk
    
  def to_string(self):
      print(f"name: {self.name}")
      print(f"type: {self.type}")
      print(f"has-milk: {self.has_milk}\n")
      
# Each are their own unique instances of the CoffeeOrder class:

adriana_order = CoffeeOrder("adriana", "latte", True)
mariana_order = CoffeeOrder("mariana", "mocha", True)

# When we print them, we can see that they are both CoffeeOrder objects and saved into memory at different locations.

print(adriana_order.name)
print(mariana_order.name)

# TODO: Order yourself a coffee by making a new instance of the CoffeeOrder class. 
# - Define a new variable and initialize an instance of CoffeeOrder
# - when initializing your instance include your name and coffee type
mikey_order = CoffeeOrder("mikey", "gibraltar", True)


# TODO: Some people like to have milk with their coffee. Add a new attribute to 
# the CoffeeOrder class: has_milk. This should store a bool. 
# Add a parameter that will allow you to initialize has_milk in the __init__
# Include the new third argument with each of the three coffee orders. 


# TODO: Let's test that. Print a messsage for each order that has the order's
# name, coffee_type, and has_milk. Make it read something like: 
# Name: <name> type: <coffee_type> Has Milk: <has_milk>
print(f'''name: {adriana_order.name}
type: {adriana_order.type}
has milk: {adriana_order.has_milk}\n''')

print(f'''name: {mariana_order.name}
type: {mariana_order.type}
has milk: {mariana_order.has_milk}\n''')

print(f'''name: {mikey_order.name}
type: {mikey_order.type}
has milk: {mikey_order.has_milk}\n''')

# If you though about making a function to solve that last TODO you are 
# doing this right! With classes we can go a step further by making the function
# part of the class itself! 

# TODO: Add a new method to the CoffeeOrder class. This method will return a 
# string describing the order. Often class will implement a "to_string" method
# that returns a human readable string describing the class instance. 
# - add a new function inside the class but NOT in the __init__ watch the indentation!
# - this new method should return a string: "Name: <name> type: <coffee_type> Has Milk: <has_milk>"
# - To access attributes of your class use the keyword self! For example: self.name
adriana_order.to_string()
mariana_order.to_string()
mikey_order.to_string()
