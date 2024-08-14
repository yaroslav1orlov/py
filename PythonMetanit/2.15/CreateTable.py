width = input("Enter width: ")
height = input("Enter height: ")

str = "╔"
for i in range(int(width)):
    str += "═"
str += "╗\n"

str += "╚"
for i in range(int(width)):
    str += "═"
str += "╝"

print(str)