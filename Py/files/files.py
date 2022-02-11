"""
Create a text file with text in your repo, save, add and commit it
use open() to open the file into a var
use read() to create a string object
print the string object
post a code screenshot
"""

f = open("file_1.txt")

ctx = f.read()
print(ctx)

f.close()