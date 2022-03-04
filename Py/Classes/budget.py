"""
Goal: Create a Budget class that can instantiate objects based on 
different budget categories like food, clothing, and entertainment. 
These objects should allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance amounts between categories

Considerations: this is a very interesting project as it allows not only to comprehend how a 
class is initialized and used, but also represented and used as input to other functions. 
You will learn how to add methods to your classes and print them in a way that allows complex representation 
of your class object at different points in the program. As a bonus, you will define a function that computes 
how much money you are spending across class categories as a % of your total expenses, something that can be very 
useful for the money-savvy programmers among you.

Approach: define the purpose and flexibility of a class object; build its class methods using a modular 
approach and develop an understanding for how different instances of the same class can interact.

Key concepts: Class initialization, instance methods and instance representation.
Defining and using functions that take class instances as input parameters

"""
# Steps
# Create a Budget class
# instantiate objects based on different
# budget categories like food, clothing, and entertainment. 
# When objects are created, they are passed in the name of the category. 
# The class should have an instance variable called ledger that is a list. 

class Category:
    balance = 0
    ledger = list()

    def __init__(self, name):
        self.name = name

    def deposit(self, amount, description):
        self.amount = amount
        self.description = description
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        return self.ledger


    def withdraw(self, amount, description):
        self.amount = amount
        self.description = description
        self.balance -= amount
        return {"amount": -abs(amount), "description": description}

    def get_balance(self):
        return self.balance


food = Category("Food")
print(food.name)
print(food.deposit(1000, "initial deposit"))
print(food.withdraw(100.15, "groceries"))
print(food.withdraw(86.89, "restaurant and more food for dessert"))

print(food.get_balance())

clothing = Category("Clothing")
print(clothing.deposit(1000, "initial deposit"))
print(clothing.withdraw(10.15, "Jeans"))
print(clothing.withdraw(15.89, "Socks"))
print(clothing.get_balance())

print(food)
print(clothing)