# Colocar en una tupla los numeros pares desde 0 hasta el 130

pares = []
for numero in range(131):
    if numero % 2 == 0:
        pares.append(numero)

tupla = tuple(pares)
print(tupla)



'''
Lista de comprehension tiene las siguientes partes:
[ {elemento a ingresar en la lista} {bucle} {filtro} ]

'''
pares2 = tuple(numero for numero in range(131) if numero % 2 == 0)
print(pares2)
