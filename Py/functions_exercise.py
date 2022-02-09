
"""
Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, 
and output their name and final ICT grade as a percentage.
Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.
Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)
"""

# Exercise 1

"""
Steps...
define a function (grades) # done
create variables: name, homework_score (/25), assessment score (/50) and final exam score (/100) as inputs # done
calculate the ICT grade. (sum(scores)/175) * 100
output their name and final ICT grade as a percentage
"""
name = input("Please enter your name\n").capitalize()
homework_score = int(input("Please enter your homework score (/25)\n"))
assessment_score = int(input("Please enter your assessment score (/50)\n"))
final_exam_score = int(input("Please enter your final exam score (/100)\n"))

def grades(final_exam_score, assessment_score, homework_score):
    scores = (final_exam_score, assessment_score, homework_score)
    percentage_score = round((sum(scores)/175) * 100)
    return percentage_score

ICT = grades(final_exam_score, assessment_score, homework_score)


# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

"""
Steps...
Create a list of grades A,B,C,D etc with corresponding scores.
Assign a grade for scores out of 100
Output grade letter for the percentage score
"""

def grade_letters(ICT): 
    if ICT > 80:
        letter = 'A'
    elif ICT < 80 and ICT > 60:
        letter = 'B'
    elif ICT < 60 and ICT > 40:
        letter = 'C'
    elif ICT < 40 and ICT > 20:
        letter = 'D'
    else: 
        letter = 'Fail'

    return letter

print(f"{name} your percentage score is {ICT}% which is grade {grade_letters(ICT)}")