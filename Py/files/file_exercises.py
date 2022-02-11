"""
Exercises
1. Create a Python file which does the following:
    Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
    Reads and displays the names of the 1st and 4th team in the file.

2. Create a new Python file which does the following:
    Edits your "teams.txt" file so that the top line is replaced with 
    "This is a new line".
    Print out the edited file line by line.
"""

# 1
team_list = ['lfc\n', 'mufc\n', 'brfc\n', 'bwfc\n', 'mcfc']
try:
    with open('teams.txt', 'x') as f:
        for s in team_list:
            f.write(s)
except FileExistsError:
    with open('teams.txt', 'w') as f:
        for s in team_list:
            f.write(s)
with open('teams.txt', 'r', newline='') as teams:
    lines = teams.readlines()
    print(f"{lines[0]}{lines[3]}")


