# Matriz INVERSA

# Forma de matriz
def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\t\n")

# OPERACIONES

# Define Principal Matrix 
originalMatrix = []

# Array para guardar el valor de 1 antes de ser 1
diagonalFutureOne = []

# Ingresa filas de matriz
sizeM = int(input("<<< ¿Cuantas columnas tiene la matriz?\t"))
noEcuacion = 0

while True:
    noEcuacion += 1     # Guarda ciclo while
    ecuacion = []       # Guarda valores de la ecuación (solo durante un ciclo)

    print(f"Ingrega datos de:\nECUACIÓN {noEcuacion}")      # Ingresa los valores de la fila
    for i in range(sizeM):
        ecuacion.append(float(input(f"Valor {i+1}:\t")))
    originalMatrix.append(ecuacion)         # Ingresa la fila (array) a matriz

    if noEcuacion == sizeM:
        break

print("\nMatriz a resolver:")       # Show Matrix
theMatrix(originalMatrix)