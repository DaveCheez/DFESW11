# Iteration
"""
A list of exercises from W3Resource:
    https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
"""

# Exercise 1
"""
Write a Python program to find those numbers which are 
divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).
"""

# Steps....
# iterate through numbers between 1500 & 2700 (both included).
# check each number to be divisible by 7 and multiple of 5
# print out the numbers that are.
lst = []
for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
        lst.append(i)
print(lst)


# Exercise 2
"""
Write a program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 ] 
 where c = temperature in celsius and f = temperature in fahrenheit
Celsius times 9 divided by 5 plus 32.
Fahrenheit to Celsius, subtract 32 and multiply by 0.5556 (or 5/9).
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

# Steps..
# Take an input as an integer for fahrenheit *(f)
# Take an input as an integer for celsius    *(c)  
# Create a func to convert the values of each 
# do the calculation on the integer
# print the reasult with the given string

def convert_to_c(f):
   c = (f - 32) * 0.5556
   print(f'{f} F is {round(c)} in Celsius')

def convert_to_f(c):
   f = (c * 9)/5 + 32
   print(f'{c} C is {round(f)} in Fahrenhrit')

temp = input("Please enter the temperature to convert: c or f\n")

if temp == 'c':
    c = int(input("Please enter the temperature in celsius\n"))
    convert_to_f(c)
elif temp == 'f':
    f = int(input("Please enter the temperature in fahrenheit\n"))
    convert_to_c(f)
else:
    print("Incorrect value for temperature")



"""
4. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""