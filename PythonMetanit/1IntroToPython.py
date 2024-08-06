# A Python program consists of a set of instructions, each placed on a new line. For example:

print(2 + 3)
print("Hello")

# Indentation plays a big role in Python. Incorrect indentation is effectively an error. For example, in the following case, we will get an error even though the code is almost identical to the one above:
#
# print(2 + 3)
#     print("Hello")
#
# Therefore, new instructions should be placed at the beginning of the line. This is one of the important differences between Python and other programming languages like C# or Java.

# However, keep in mind that some language constructs can consist of multiple lines. For example, the if conditional construct:

if 1 < 2:
    print("Hello")

# In this case, if 1 is less than 2, the string "Hello" is printed. Here, indentation is required because the print("Hello") instruction is not used on its own but as part of the if conditional construct. According to the code formatting guide, the indentation should preferably be a multiple of 4 spaces (i.e., 4, 8, 16, etc.). Although if the indentation is not 4 but 5 spaces, the program will still work.

# There are not many such constructs, so there should be no significant confusion about where to place spaces.

# Case Sensitivity
# Python is a case-sensitive language, so expressions print, Print, or PRINT represent different expressions. If we try to use the Print method instead of the print method to output to the console:
#
#Print("Hello World")
#
# It won't work.

# Comments
# Comments are used to note what a particular section of code does. When translating and executing the program, the interpreter ignores comments, so they have no effect on the program's operation. Comments in Python can be block or line comments.

# Line comments start with the hash sign - #. They can be placed on a separate line:

# # Output to the console
# # the message Hello World
# print("Hello World")

# Any set of characters after the # sign is a comment. In the example above, the first two lines of code are comments.

# They can also be placed on the same line as the language instructions, after the executing instructions:

print("Hello World")  # Output the message to the console

# In block comments, three single quotes are placed before and after the comment text: '''comment text'''. For example:

'''
    Output to the console
    the message Hello World
'''
print("Hello World")

# Main Functions
# Python provides a number of built-in functions. Some of them are used very often, especially at the initial stages of learning the language, so let's consider them.

# The main function for outputting information to the console is the print() function. The string we want to print is passed as an argument to this function:

print("Hello Python")

# If we need to print multiple values to the console, we can pass them to the print function separated by commas:

print("Full name:", "Jake", "Smith")

# As a result, all the passed values will be joined with spaces into one string:

# Full name: Jake Smith

# While the print function is responsible for output, the input function is responsible for inputting information. This function takes an optional prompt argument and returns the entered string, which we can store in a variable:

name = input("Enter your name: ")
print("Hello", name)

# Console output:

# Enter your name: Ethan
# Hello Ethan