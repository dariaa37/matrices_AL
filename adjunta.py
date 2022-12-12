# Adjunta

import copy


def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\t\n")

# INFORMACIÓN Y VARIABLES A USAR
matrix = [      
    [1, 3, 0, 1],
    [0, 2, 1, 4],
    [2, 1, 1, 0],
    [1, 0, 3, 1]
]

size = len(matrix)  # Tamaño matriz
det = 1     # Determinante
copyMatrix = copy.deepcopy(matrix)

# From INT to FLOAT
for i in range(size):
    for j in range (size):
        matrix[i][j] = float(matrix[i][j])

print(" Matriz a resolver: ".center(80,"="))       # Show Matrix
theMatrix(matrix)

 # PARTE 1 | DETERMINANTE (Ley de Laplace)
def sarrus(d):      # Da un valor ADJUNTO solo para matrices 3x3
    diagonalA = d[0][0] * d[1][1] * d[2][2] + (d[0][1] * d[1][2] * d[2][0]) +(d[0][2] * d[1][0] * d[2][1])
    diagonalB = d[0][2] * d[1][1] * d[2][0] + (d[0][1] * d[1][0] * d[2][2]) +(d[0][0] * d[1][2] * d[2][1])
    detSarrus = float(diagonalA - diagonalB)
    return detSarrus

# # Guarda los datos de matriz 3x3
def newMatrix3(matriz,thisNoFila, thisNoColumna):
    tresMat = []                                    # Guarda matriz 3x3
    for i in range(size):
        if i != thisNoFila:                         # Avoid fila del coeficiente
            miniFila = []   
            for j in range(size):
                if j != thisNoColumna:              # Avoid columna del coeficiente
                    miniFila.append(matriz[i][j])   # Guarda Filas
            tresMat.append(miniFila)
    return tresMat

# PARTE 2 | MATRIZ ADJUNTA
# Crea matrices de 3 para resolver con Sarrus
c = 0
matrixAdjunta = []
while True:
    for i in range(size):
        filasAdjunta = []
        for j in range(size):
            print(f"Cofactor {i+1}, {j+1} ----")
            theMatrix(newMatrix3(matrix, i,j))      # La matriz 3x3 se creá
            
            # Obtener determinante 3x3
            miniDet = sarrus(newMatrix3(matrix, i,j))

            # Evalucaión de signos
            signo = ((i+1)+(j+1))% 2 
            if signo == 1:                          # Cofactores con signo (-)
                print("inpar")
                filasAdjunta.append(-1*miniDet)
                print(filasAdjunta)
            else: 
                filasAdjunta.append(miniDet)      # Cofactores con signo (+)
                print("inpar")
                print(filasAdjunta)
        matrixAdjunta.append(filasAdjunta)
    c += 1

    if c == len(matrix):
        break

print(f"MATRIZ ADJUNTA")
theMatrix(matrixAdjunta)
