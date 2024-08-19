factorial = int(input("Enter factorial: "))
result = 1
i = 1
while i < factorial:
    result = i * result
    print(f"factorial - {i} result = ", result)

    i += 1 # i = i + 1
    print(f"{i} < {factorial} - {i < factorial}")
    
print(f"{factorial}! = {result}")

# Используйте цикл while для вычисления факториала числа