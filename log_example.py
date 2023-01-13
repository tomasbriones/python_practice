import logging

def suma(x,y):
    return x+y

def saluda(nombre):
    return f"Hola {nombre}, ¿como esta tu dia?"


num_1 = 10
num_2 = 4

nombre = "Tomas"

resultado_suma = suma(num_1,num_2)
logging.warning(f"suma:{num_1}+{num_2}={resultado_suma}")
saludo = saluda(nombre)
logging.warning(saludo)