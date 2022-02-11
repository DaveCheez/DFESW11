# Print Function
print("Hello")

# Variable Assignment
x = 101             # integer
y = 10.5            # float
name = 'David'      # string
l_name = 'Barrow'   # string
f = False           # Boolean
t = True            # Boolean

print(x + y)               # Calculation
print(name + ' ' + l_name) # Concatenation

# Type Casting booleans to integers
print(int(f))
print(int(t))

# Booleans
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)


# Numbers & Floats
number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# Using .items() method generate a list of tuples consisted of each key value pair.
dict = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
ans_1 = dict.items()

print(ans_1)

# Using .get() method print the value of "son's eyes".
dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
ans_1 = dict.get("son's eye color")

print(ans_1)

# Assign the first element of the list to answer_1 on line 2
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]

print(answer_1)

# Print the last element of the list through variable answer_1.
lst=[11, 100, 101, 999, 1001]
answer_1 = lst[-1]

print(answer_1)

# Assign the first element of the list to answer_1 
lst=[11, 100, 99, 1000, 999]
answer_1 = lst[0]

print(answer_1)