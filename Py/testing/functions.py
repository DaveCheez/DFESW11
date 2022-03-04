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