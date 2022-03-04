from math import prod


# 1. Write a Python function to find the Max of three numbers.

def max_of_3(a,b,c):
    return max(a,b,c)

# 2. Write a Python function to sum all the numbers in a list.

def sum_of_all(list):
    return sum(list)

# 3. Write a Python function to multiply all the numbers in a list.

def find_product(list1):
    return prod(list1)

# 4. Write a Python program to reverse a string.

def reverse_string(str):
    return str[::-1]

# 5. Write a Python function to calculate the factorial of a number
# (a non-negative integer). 
# The function accepts the number as an argument.

'''
Steps...
define a function
take a positive integer as an argument
create a list of numbers from 1 to the given argument
find the product of all the numbers in the list
'''

def find_factorial(i):
    j = [ i for i in range(1, i+1) ]
    return prod(j)


# 6. Write a Python function to check whether 
# a number falls in a given range. 

def check_in_range(a,b,c):
    if [c for c in range(a,b)]:
        return True
    return False
    
# 7. Write a Python function that accepts a string 
# and calculate the number of upper case letters 
# and lower case letters.

'''
Steps...
define a function
take a string as an argument
create 2 lists (upper) & (lower) case 
append each letter to the corresponding list

'''

def upper_lower_count(str):
    upper = []
    lower = []
    for x in str:
        if x.islower():
            lower.append(x)
        elif x.isupper(): 
            upper.append(x)

    return len(upper), len(lower)
