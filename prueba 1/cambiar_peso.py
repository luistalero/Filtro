import os 
dolar = 3944
euro = 4279
yen =26.30

title = """
********************
*    BIENVENIDO    *
********************
"""
os.system('cls')
print(title)
pesos = float(input("Ingrese la cantidad de Pesos que quiere convertir a dolares : "))
print(f'los pesos equivalen a {pesos/dolar} dolares')
pesos = float(input("Ingrese la cantidad de Pesos que quiere convertir a Euros : "))
print(f'los pesos equivalen a {pesos/euro} Euros')
pesos = float(input("Ingrese la cantidad de Pesos que quiere convertir a Yenes : "))
print(f'los pesos equivalen a {pesos/yen} Yenes')
Euros = float(input("Ingrese la cantidad de Euros que quiere convertir a Pesos : "))
print(f'los pesos equivalen a {Euros*euro} Pesos')