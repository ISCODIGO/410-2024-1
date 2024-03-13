# Colocar en una lista los numeros pares elevados al cuadrado desde 0 hasta el 130

pares = []
for numero in range(131):
    if numero % 2 == 0:
        pares.append(numero**2)

print(pares)

'''
Lista de comprehension tiene las siguientes partes:
[ {elemento a ingresar en la lista} {bucle} {filtro} ]

'''
pares2 = [numero**2 for numero in range(131) if numero % 2 == 0]
print(pares2)
