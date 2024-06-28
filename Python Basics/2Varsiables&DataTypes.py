# Variables
# Variables are used to store data. In Python, a variable name must start with an alphabetic character or an underscore
# and can contain alphanumeric characters and underscores. Additionally, the variable name should not match any of
# Python's reserved keywords. The reserved keywords are few and easy to remember.

# For example, let's create a variable:
name = "Tom"
# Here, the variable `name` is defined, which stores the string "Tom".

# In Python, two types of variable naming conventions are used: camel case and underscore notation.
# Camel case means that each new word in the variable name starts with a capital letter. For example:
userName = "Tom"

# Underscore notation means that words in the variable name are separated by an underscore. For example:
user_name = "Tom"

# It's also important to consider case sensitivity, so the variables `name` and `Name` will represent different objects.
name = "Tom"
Name = "Tom"

# Once we define a variable, we can use it in the program. For example, we can try to print its content to the console
# using the built-in `print` function:
name = "Tom"  # defining the variable name
print(name)   # printing the value of the variable name to the console

# Variables in Python
# An important feature of a variable is that we can change its value during the execution of the program:
name = "Tom"  # the variable name equals "Tom"
print(name)   # prints: Tom
name = "Bob"  # changing the value to "Bob"
print(name)   # prints: Bob

# Data Types
# A variable holds data of a certain data type. Python has many different data types. Here, we will only consider
# the most basic types: bool, int, float, complex, and str.

# Boolean values
# The bool type represents two logical values: True (correct, truth) or False (incorrect, false). The value True is used
# to show that something is true, while the value False shows that something is false. Example of variables of this type:
isMarried = False
print(isMarried)  # False

isAlive = True
print(isAlive)    # True

# Integers
# The int type represents an integer, such as 1, 4, 8, 50. Example:
age = 21
print("Age:", age)  # Age: 21

count = 15
print("Count:", count)  # Count: 15

# By default, standard numbers are considered as numbers in the decimal system. But Python also supports numbers in
# binary, octal, and hexadecimal systems.

# To indicate that a number is in the binary system, prefix the number with 0b:
a = 0b11
b = 0b1011
c = 0b100001
print(a)  # 3 in decimal system
print(b)  # 11 in decimal system
print(c)  # 33 in decimal system

# To indicate that a number is in the octal system, prefix the number with 0o:
a = 0o7
b = 0o11
c = 0o17
print(a)  # 7 in decimal system
print(b)  # 9 in decimal system
print(c)  # 15 in decimal system

# To indicate that a number is in the hexadecimal system, prefix the number with 0x:
a = 0x0A
b = 0xFF
c = 0xA1
print(a)  # 10 in decimal system
print(b)  # 255 in decimal system
print(c)  # 161 in decimal system

# It is worth noting that no matter which system we pass the number to the print function for output to the console,
# it will by default be displayed in the decimal system.

# Floating-point numbers
# The float type represents a floating-point number, such as 1.2 or 34.76. A dot is used as a separator between the
# integer and fractional parts.
height = 1.68
pi = 3.14
weight = 68.0
print(height)  # 1.68
print(pi)      # 3.14
print(weight)  # 68.0

# A floating-point number can be defined in exponential notation:
x = 3.9e3
print(x)  # 3900.0

x = 3.9e-3
print(x)  # 0.0039

# A float number can have only 18 significant digits. So, in this case, only two digits are used - 3.9. And if the number
# is too large or too small, we can write the number in this notation using an exponent. The number after the exponent
# indicates the power of 10 by which the main number - 3.9 should be multiplied.

# Complex numbers
# The complex type represents complex numbers in the format real_part + imaginary_part j - the imaginary part is followed
# by the suffix j
complexNumber = 1 + 2j
print(complexNumber)  # (1+2j)

# Strings
# The str type represents strings. A string represents a sequence of characters enclosed in single or double quotes,
# for example "hello" and 'hello'. In Python 3.x, strings represent a set of characters in Unicode encoding.
message = "Hello World!"
print(message)  # Hello World!

name = 'Tom'
print(name)  # Tom

# If the string has many characters, it can be broken into parts, and these parts can be placed on different lines of code.
# In this case, the entire string is enclosed in parentheses, and its individual parts are enclosed in quotes:
text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)

# If we want to define a multiline text, such text is enclosed in triple double or single quotes:
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula
'''
print(text)

# When using triple single quotes, do not confuse them with comments: if the text in triple single quotes is assigned
# to a variable, it is a string, not a comment.

# Escape sequences in a string
# A string can contain a number of special characters - escape sequences. Some of them:
# \\: allows you to add a backslash inside the string
# \': allows you to add a single quote inside the string
# \": allows you to add a double quote inside the string
# \n: performs a line break
# \t: adds a tab (4 spaces)
# Let's apply some sequences:
text = "Message:\n\"Hello World\""
print(text)
# Console output of the program:
# Message:
# "Hello World"

# Although such sequences can help us in some tasks, for example, put a quote in a string, make a tab, or move to another
# line, they can also interfere. For example:
path = "C:\\python\\name.txt"
print(path)
# Here the variable path contains a path to a file. However, inside the string, there are characters "\n", which will be
# interpreted as an escape sequence. So, we will get the following console output:
# C:\python
# ame.txt

# To avoid such a situation, prefix the string with the character r
path = r"C:\python\name.txt"
print(path)

# Inserting values into a string
# Python allows you to insert the values of other variables into a string. To do this, place the variables inside the
# string in curly braces {}, and put the character f before the entire string:
userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)  # name: Tom  age: 37

# In this case, the value of the userName variable will be inserted in place of {userName}. Similarly, the value of the
# userAge variable will be inserted in place of {userAge}.

# Dynamic Typing
# Python is a dynamically typed language.