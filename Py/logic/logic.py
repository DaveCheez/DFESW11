# Logic Exercises

"""
Create a new Python file and write a program that does the following:
    Asks for an input from the user as a mark.
    If the mark is greater that 85 print "Distinction"
    If the mark is between 65 and 85 print "Pass"
    Anything else print "Fail"
"""
mark = int(input("Please enter your mark:\n"))

if mark > 85:
    print("Distinction")
elif mark >= 65 and mark <= 85:
    print("Pass")
else:
    print("Fail")


"""Try to do this both with and without elif statements."""

mark2 = int(input("Please enter your second mark:\n"))

if mark2 >= 65:
    if mark2 > 85:
        print("Distinction")
    else:
        print("Pass")
else:  
    print("Fail")
