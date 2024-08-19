'''
Запросить у пользователя число и вивести чотное оно или нет
''' 
while True:
    num = int(input("ведите число: "))
    num1 = num / 2
    num2 = int(num1)
    if num1 == num2:
        print("чесло чётное")
    else:
        print("число не чётное")