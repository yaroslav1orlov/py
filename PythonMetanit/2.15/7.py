# 7. Используйте for для нахождения наибольшего числа в списке.

width = input("Enter width: ")
height = input("Enter height: ")

str = "╔"
for i in range(int(width)):
    str += "═"

str += "╗"

print(str)
print()


str = "╔"
for i in range(int(height)):
    str += "║"

str += "╗"

print(str)
print()