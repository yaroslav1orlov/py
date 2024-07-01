import pwinput
user_name = input("Username: ")
password_1 = pwinput.pwinput(prompt="Password: ", mask="#")
welcome_message = f"Welcome, {user_name}. Now I know your password, your password is {password_1}! Ahahahaha"
print(welcome_message)