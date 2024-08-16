def CreateHeder(width):
    str = "╔"
    for i in range(int(width)):
        str += "═"
    str += "╗\n"
    return str

def CreateFooter(width):
    str = "╚"
    for i in range(int(width)):
        str += "═"
    str += "╝"
    return str

width = input("Enter width: ")
height = input("Enter height: ")

header = CreateHeder(width)
footer = CreateFooter(width)

print(header + footer)