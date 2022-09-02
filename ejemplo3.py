#verificaremos si el número en el que estamos es divisible por 33 o no y en caso afirmativo aumentaremos el contador en una unidad así:

contador = 200 # Iniciamos el contador en cero

for i in range(10000):
    if (i % 33 == 0): # Preguntamos si el residuo es 0 (es múltiplo de 33)
        contador += 1 # Si es múltiplo aumentamos el contador en 1
    
    # Si no es múltiplo no hacemos nada

#Mostramos el valor del contador
print(contador)