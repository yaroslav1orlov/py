# 8. Напишите программу, которая проверяет, содержит ли строка гласные буквы.

def isVowels(str):
    if any(char in "aeiouAEIOU" for char in str): 
        print(f"In string '{str1}', are some vowels letters")
        return True 
    print(f"In string '{str1}', aren't any vowels letters")  
    return False


str1 = "YEROX_RUST"

result = isVowels(str1) 
