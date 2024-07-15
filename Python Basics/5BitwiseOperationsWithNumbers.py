number = 5
print(f"number = {number:0b}")
number = 0b101
print(f"number = {number:0b}")
print(f"number = {number}")

number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6

x1 = 2
y1 = 5
z1 = x1 & y1
print(f"z1 = {z1}")

x2 = 4
y2 = 5
z2 = x2 & y2
print(f"z2 = {z2}")
print(f"z2 = {z2:0b}")

x1 = 2
y1 = 5
z1 = x1|y1

print(f"z1 = {z1}")
print(f"z1 = {z1:0b}")

x2 = 4
y2 = 5
z2 = x2 | y2
print(f"z2 = {z2}")
print(f"z2 = {z2:0b}")

x=9
y=5
z = x^y
print(f"z = {z}")
print(f"z = {z:0b}")

x = 45
key = 102

encrypt = x^key
print(f"Encrypted number: {encrypt}")

decrypt = encrypt ^ key
print(f"Decrypted number: {decrypt}")

x=9
y=5
x = x^y
y = x^y
x = x^y

print(f"x = {x}")
print(f"y = {y}")

x = 5
y = ~x;
print(f"y: {y}")

a = 16
b = 2
c = a << b
print(c)

d = a >> b
print(d)

a = 22
b = 2
c = a << b
print(c)
d = a >> b
print(d)