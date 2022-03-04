"""
Create a function
put a print statement in it
call it a few times.
run the program
"""


def print_something(something):
    for x in range(5):
        print(something)

something = "pies"
print_something(something)


"""
Temp Convertor
"""
f = int(input("Please enter the temperature in fahrenheit\n"))
def convert_to_c(f):
   c = (f - 32) * 0.5556
   return c 

print(f'{f} F is {round(convert_to_c(f))} in Celsius')

