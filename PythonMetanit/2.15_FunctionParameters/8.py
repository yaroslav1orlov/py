# 8. Напишите программу, которая проверяет, содержит ли строка гласные буквы.

def isVowels(str1):
    if any(char in "aeiouAEIOU" for char in str1): 
        print("In string are some vowels letters")
        return True 
    print("In string aren't any vowels letters")  
    return False


str1 = "YEROX_RUST"

result = isVowels(str1) 
