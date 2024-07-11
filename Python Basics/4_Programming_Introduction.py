# Python supports all common arithmetic operations:

# Addition of two numbers:
print(6 + 2)  # 8

# Subtraction of two numbers:
print(6 - 2)  # 4

# Multiplication of two numbers:
print(6 * 2)  # 12

# Division of two numbers:
print(6 / 2)  # 3.0

# Integer division of two numbers:
print(7 / 2)  # 3.5
print(7 // 2)  # 3

# This operation returns the integer result of division, discarding the fractional part

# Exponentiation:
print(6 ** 2)  # Raising 6 to the power of 2. Result - 36

# Modulus operation:
print(7 % 2)  # Getting the remainder of the division of 7 by 2. Result - 1

# In this case, the closest number to 7 that is divisible by 2 without a remainder is 6. So the remainder is 7 - 6 = 1

'''
    When using several arithmetic operations sequentially, they are performed according to their precedence. 
    Higher precedence operations are performed first. 
    The precedence of operations in descending order is given in the following table:
'''

'''
    Operations      Direction
    **              Right to left
    * / // %        Left to right
    + -             Left to right
'''

# Let's consider the following expression:
number = 3 + 4 * 5 ** 2 + 7
print(number)  # 110

'''
    Here, exponentiation (5 ** 2) is performed first, then the result is multiplied by 4 (25 * 4), 
    then addition occurs (3 + 100), and finally another addition (103 + 7).
'''

'''
    To override the order of operations, parentheses can be used:

'''
number = (3 + 4) * (5 ** 2 + 7)
print(number)  # 224

'''
    It should be noted that both integers and floating-point numbers can participate in arithmetic operations. 
    If an operation involves both an integer (int) and a floating-point number (float), 
    the integer is converted to the float type.
'''

'''
    Arithmetic operations with assignment
    A number of special operations allow assigning the result of an operation to the first operand:
'''

'''
    +=  Assignment of the result of addition
    -=  Assignment of the result of subtraction
    *=  Assignment of the result of multiplication
    /=  Assignment of the result of division
    //= Assignment of the result of integer division
    **= Assignment of the power of a number
    %=  Assignment of the remainder of the division
'''

# Examples of operations:
number = 10
number += 5
print(number)  # 15

number -= 3
print(number)  # 12

number *= 4
print(number)  # 48

'''
    
    Rounding and the round function
    When performing operations with float type numbers, it should be considered that the result may not be exactly accurate. 
    For example:
'''
first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(third_number)  # 0.40002000000000004

'''
    In this case, we expect to get 0.40002, but a four appears at the end after a series of zeros. 
    Another example:
'''
print(2.0001 + 0.1)  # 2.1001000000000003

# To round the result, we can use the built-in round() function:
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number))  # 2

'''

    The round() function takes the number to be rounded. 
    If a single number is passed, it is rounded to the nearest integer.
    The round() function can also take a second number specifying how many decimal places the result should have:
'''
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4))  # 2.1001

'''
    In this case, third_number is rounded to 4 decimal places.
    If the function takes only one value - the number to be rounded - it is rounded to the nearest integer.
'''

'''
    Examples of rounding:
'''
print(round(2.49))  # 2 - rounding to the nearest integer 2
print(round(2.51))  # 3

'''
    However, if the rounding part is equally distant from two integers, the rounding goes to the nearest even number:
'''
print(round(2.5))  # 2 - nearest even number
print(round(3.5))  # 4 - nearest even number

'''
    Rounding is performed to the nearest multiple of 10 to the power of minus the rounding part:
'''
print(round(2.554, 2))      # 2.55
print(round(2.5551, 2))     # 2.56
print(round(2.554999, 2))   # 2.55
print(round(2.499, 2))      # 2.5

'''
    However, it should be considered that the round() function is not a perfect tool. 
    For example, above when rounding to integers, the rule is applied that if the rounding part is equally distant from two values, 
    the rounding is done to the nearest even value. In Python, because the decimal part of a number cannot be exactly represented as a float number, 
    this may lead to some unexpected results. For example:
'''
print(round(2.545, 2))  # 2.54
print(round(2.555, 2))  # 2.56 - rounding to even
print(round(2.565, 2))  # 2.56
print(round(2.575, 2))  # 2.58

print(round(2.655, 2))  # 2.65 - not rounding to even
print(round(2.665, 2))  # 2.67
print(round(2.675, 2))  # 2.6