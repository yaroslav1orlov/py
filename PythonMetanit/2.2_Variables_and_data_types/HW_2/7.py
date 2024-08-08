# + Создайте игру, где пользователь должен угадать число
# - от 1 до 10. Используйте цикл while

import random
randomNumber = random.randint(1, 10)
number = 0
attempts = 3

while number != randomNumber:
    userInput = input(f"Guess the number from 1 to 10 (Attempts left: {attempts}): ")
    number = int(userInput)
    attempts -= 1 # attempts = attempts - 1
    print("Oops, try again ):" * (number != randomNumber) + "Congratulations, you guessed the number (:" * (number == randomNumber)) # == Mean True, False
    if attempts == 0:
        break
    
print("Sorry, you've used all your attempts. The number was", randomNumber * (number != randomNumber))