# 5. Напишите цикл for, который выводит таблицу умножения на 5.



for i in range(2, 10):
    print("")
    print("   ", i)
    print("")
    for x in range(2, 10):
        print(f"{i} * {x} =", i * x)    