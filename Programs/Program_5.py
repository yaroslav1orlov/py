def isEven(num):
    divided = num / 2
    rounded_num = round(divided)
    #print(type(divided), divided, rounded_num)
    number = rounded_num * 2
    return number == num

num = int(input("Enter any number: "))
result = isEven(num)

if result:
    print(f"This number is even ({num})")
else:
    print(f"This number is odd ({num})")
