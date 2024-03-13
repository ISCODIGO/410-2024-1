# un diccionario con la clave numeros enteros entre 0 y 100, y como valor
# el cuadrado

resultado = {}
for numero in range(101):
    resultado[numero] = numero**2
print(resultado)


resultado2 = {numero: numero**2 for numero in range(101)}
print(resultado2)
