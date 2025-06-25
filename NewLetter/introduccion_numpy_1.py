import numpy as np

# Crear un array unidimensional
a = np.array([1, 15, 13])
b = np.array([4, 5, 6])

#Suna de arrays
suma = a + b
print("Suma de arrays:", suma)
print("Suma de arrays con np.add:", np.add(a, b))

# Resta de arrays
resta = a - b
print("Resta de arrays:", resta)
print("Resta de arrays con np.subtract:", np.subtract(a, b))

# Multiplicación de arrays
multiplicacion = a * b
print("Multiplicación de arrays:", multiplicacion)
print("Multiplicación de arrays con np.multiply:", np.multiply(a, b))

# División de arrays
division = a / b
print("División de arrays:", division)
print("División de arrays con np.divide:", np.divide(a, b))

# Potencia de arrays
potencia = a ** b
print("Potencia de arrays:", potencia)  
print("Potencia de arrays con np.power:", np.power(a, b))
