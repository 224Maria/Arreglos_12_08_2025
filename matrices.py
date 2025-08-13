import numpy as np
matriz = np.random.randint(0,100(3,3))
print(matriz)
matriz2 = np.random.Generator(np.random.PCG64()).integers(1,100(3,3))
print("\033[34m", matriz2,"\033[0m")
matriz_identidad = np.eye(3)
print("\033[32m", matriz_identidad,"\033[0m")
print("\033[31m"," __________________"," \033[0m")
matriz_transpuesta = matriz.T
print("\033[33m", matriz_transpuesta,"\033[0m")
print("\033[31m"," __________________"," \033[0m")
matriz_zeros = np.zeros((2,2))
print("\033[35m", matriz_zeros,"\033[0m")
print("\033[31m"," __llenar la diagonal de 1__"," \033[0m")
for incrementador in range(2):  "incrementador ": Unknown word.
    matriz_zeros[incrementador][incrementador] = 1
print("\033[38m", matriz_zeros,"\033[0m")
print("\033[31m"," __________________"," \033[0m")

for fila in range(2):
    for columna in range(2):    "columna": Unknown word.
        matriz_zeros[fila][columna] = (np.random.randint(0,100))+1
print   Replace print statement by built-in function
print("\033[35m", matriz_zeros,"\033[0m")
print("\033[31m"," __________________"," \033[0m")
