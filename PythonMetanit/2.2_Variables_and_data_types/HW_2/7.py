# + Создайте игру, где пользователь должен угадать число
# - от 1 до 10. Используйте цикл while

import random

randomNumber = random.randint(1, 10)
number = 0

while number != randomNumber:
    userInput = input("Guess the number from 1 to 10: ")
    number = int(userInput)
    print("Opss, try again ):")

print("Congratulations you guessed the number (:")