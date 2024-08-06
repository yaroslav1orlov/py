# + Создайте игру, где пользователь должен угадать число
# - от 1 до 10. Используйте цикл while

import random

randomNumber = random.randint(1, 10)
number = 0

while number != randomNumber:
    userInput1 = input("You have 3 attempts left. Guess the number from 1 to 10: ")
    userInput2 = input("You have 2 attempts left. Guess the number from 1 to 10: ")
    userInput3 = input("You have 1 attempts left. Guess the number from 1 to 10: ")
    number = int(userInput1)
    number = int(userInput2)
    number = int(userInput3)

    print("Opss, try again ]:, the number was", randomNumber)

print("Congratulations you guessed the number :]")