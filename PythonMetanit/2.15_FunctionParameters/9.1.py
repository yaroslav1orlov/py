'''
Запросить у пользователя число и вивести чётное оно или нет
'''
# создать функцию которая принимает число и возврощает bool
n = 1
def isPaired(n):
    n = True, False
    return n

result = isPaired(n)
print(n)

while True:
    num = int(input("ведите число: ")) #запрашивает число у пользователя
    num1 = num / 2                     #num1 = чесло которое задал пользователь и делим его на 2 
    num2 = int(num1)                   #num2 = делонное чесло которое задал пользователь
    if num1 == num2:                   #если делонное чесло которое задал пользователь = num2
        print("чесло чётное")          #виводим в консоль "чесло чётное"
    else:                              #если обратное виводим в консоль
        print("число не чётное")       #виводим число не чётное