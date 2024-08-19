# Console Output
# To output information to the console, we use the built-in `print()` function.
# When calling this function, the value to be output is passed in parentheses:

print("Hello METANIT.COM")
# This code will output the string "Hello METANIT.COM" to the console.

# A distinctive feature of this function is that by default, it outputs the value on a new line. For example:

print("Hello World")
print("Hello METANIT.COM")
print("Hello Python")

# Here, three calls to the `print()` function output some messages. When output to the console, each message will be placed on a new line:

# Hello World
# Hello METANIT.COM
# Hello Python

# Such behavior is not always convenient. For example, we want all values to be displayed on one line.
# To do this, we need to adjust the behavior of the function using the `end` parameter.
# This parameter specifies the characters that are added at the end of the output string.
# When using the `end` parameter, the `print()` function call looks as follows:

print("Hello World", end=" ")
print("Hello METANIT.COM", end=" ")
print("Hello Python")
# Now the output values will be separated by a space:

# Hello World Hello METANIT.COM Hello Python

# Moreover, it can be not just one character but a set of characters:

print("Hello World", end=" and ")
print("Hello METANIT.COM", end=" and ")
print("Hello Python")

# In this case, the output messages will be separated by the characters " and ":

# Hello World and Hello METANIT.COM and Hello Python


# Console Input
# In addition to outputting to the console, we can get user input from the console.
# In Python, the `input()` function is defined for this purpose. This function takes an input prompt.
# We can save the input result in a variable. For example, let's define code for the user to enter their name:

name = input("Enter your name: ")
print(f"Your name: {name}")

# In this case, the `input()` function takes an input prompt in the form of the string "Enter your name:".
# The result of the function - the user input - is passed to the `name` variable.
# Then we can output the value of this variable to the console using the `print()` function. Example of code execution:

# Enter your name: Eugene
# Your name: Eugene

# Another example with multiple inputs:

name = input("Your name: ")
age = input("Your age: ")
print(f"Name: {name}  Age: {age}")

# Example of program execution:

# Your name: Tom
# Your age: 37
# Name: Tom  Age: 37

# It is important to note that all entered values are considered as values of type `str`, that is, strings.
# Even if we enter a number, as in the second case in the code above,
# Python will still treat the entered value as a string, not as a number.