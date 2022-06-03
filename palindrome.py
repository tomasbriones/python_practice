# from mypy import *

def is_palindrome(string: str)-> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    var = input("Ingrese un nombre:")
    print(is_palindrome(var))

if __name__ == '__main__':
    print("Ejecutando codigo")
    run()