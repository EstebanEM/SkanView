#Escriba un programa para mostrar los primeros 10 números naturales.
# WHILE
# Definimos una función para encontrar la suma de los primeros n números naturales con un ciclo while
def suma_naturales_while(n):
    suma = 0
    i = 1

    while i <= n:
        suma += i
        i += 1

    return suma

# Definimos el valor de n (en este caso, 20)
n = 20

# Llamamos a la función y almacenamos el resultado en una variable
resultado_while = suma_naturales_while(n)

# Imprimimos el resultado
print(f"La suma de los primeros {n} números naturales usando while es: {resultado_while}")

