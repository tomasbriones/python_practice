import random

def run():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_upper = []
    for letter in alphabet:
        alphabet_upper.append(letter.upper())
    numbers = ['1','2','3','4','5','6','7','8','9']
    symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','<',',','>','.','?','/']
    all_data = alphabet+numbers+symbols
    random.shuffle(all_data)

    password_list = []
    for i in range(0,12):
        password_list.append(random.choice(all_data))
    password = "".join(password_list)
    print(f"Tu password de {len(password_list)} digitos es: {password}")

if __name__== "__main__":
    run()