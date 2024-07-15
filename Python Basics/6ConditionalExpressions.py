a = 5
b = 6
result = 5 == 6
print(result)
print(a != b)
print(a > b)
print(a < b)

bool1 = True
bool2 = False
print(bool1 == bool2)

age = 22
weight = 58
result = age > 21 and weight == 58
print(result)

result = 4 and "w"
print(result)

result = 0 and "w"
print(result)

age = 22
isMarried = False
result = age > 21 or isMarried
print(result)

result = 4 or "w"
print(result)

result = 0 or "w"
print(result)

age = 22
isMarried = False
print(not age > 21)
print(not isMarried)
print(not 4)
print(not 0)

message = "hello world!"
hello = "hello"
print(hello in message)
gold = "gold"
print(gold in message)

message = "hello world!"
hello = "hello"
print(hello not in message)

gold = "gold"
print(gold not in message)