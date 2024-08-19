# Создайте программу, которая находит наименьший общий делитель двух чисел, используя цикл while

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b

print("Least common divisor: " + a)