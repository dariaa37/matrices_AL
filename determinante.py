# Program:  Determinantes
# Name:     Karla Díaz Aguilar

# [2,0,1] [3,0,0] [5,1,1]

def cerosLeft(matriz,indice,aryBeforeOne,aryForInverse):        # Vuelve ceros columnas en diagonal izquierda
    tamañoM = len(matriz)       # Tamaño matriz (Cant filas matriz)
    tamañoF = len(matriz[0])    # Tamaño fila (Cant elementos en fila)
    theOne = matriz[indice][indice] 
    for fila in range(indice+1,tamañoM):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][indice]*(-1)/ theOne
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += matriz[indice][columna] * coeficiente

    aryBeforeOne.append(theOne)    # Guarda el valor de la diagonal antes de ser 0
    aryForInverse.append(1/theOne)

def determinante(matriz,inverso):
    tamañoM = len(matriz)       # Tamaño matriz (Cant filas matriz)
    tamañoF = len(matriz[0])    # Tamaño fila (Cant elementos en fila)
    det = 0
    for fila in range(tamañoM): # Crea la diagonal de 1 y cambia los demas valores
        for elemento in range(tamañoF):
            det += matriz[fila][elemento] * inverso[fila]
    theMatrix(matriz)
    return det

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\t\n")


# Define Principal Matrix 
originalMatrix = []

# Array para guardar el valor de 1 antes de ser 1
diagonalFutureOne = []


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

# Determinants process -----------------------
fila = 0
while True:
    # Resuelve 0 por columnas
    cerosLeft(originalMatrix,fila)
    print(f"Ceros columna {fila+1}")
    theMatrix(originalMatrix)
    # Contador de no Fila
    fila += 1

    if fila == sizeM:
        break    

determinante(originalMatrix,)

    ## Optimizar función ceros leff