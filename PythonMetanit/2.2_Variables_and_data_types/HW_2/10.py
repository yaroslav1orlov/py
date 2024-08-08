# Реализуйте простой счетчик с возможностью увеличения и сброса значения, используя цикл while и ввод пользователя

counter = 0

while True:
    print(f"Current counter value: {counter}")
    print("Enter 'p', to increase the value by 1.")
    print("Enter 'r', to reset the value.")
    print("Enter 'q', to quit.")
    
    user_input = input("Your choice: ")

    if user_input == 'p':
        counter += 1
    elif user_input == 'r':
        counter = 0
    elif user_input == 'q':
        break
    else:
        print("Invalid input, try again.")

print("Program terminated.")