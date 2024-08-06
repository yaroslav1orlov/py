name = "Tom"
 
 
def say_hi():
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
say_hi()
say_bye()

def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
 
 
def say_bye():
    name = "Tom"
    print("Good bye", name)
 
say_hi()
say_bye()

name = "Tom"
 
 
def say_hi():
    name = "Bob"
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
 
say_hi()
say_bye()

name = "Tom"
 
 
def say_hi():
    global  name
    name = "Bob"
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
 
say_hi()
say_bye()

def outer():
    n = 5
 
    def inner():
        print(n)
 
    inner()
    print(n)
 
 
outer()

def outer():
    n = 5
 
    def inner():
        n = 25
        print(n)
 
    inner()
    print(n)
 
 
outer()

def outer():
    n = 5
 
    def inner():
        nonlocal n
        n = 25
        print(n)
 
    inner()
    print(n)
 
 
outer()