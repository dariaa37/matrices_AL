# EXAMEN PARA OBTENER MATRIZ INVERSA
# All the funtions
import copy

# from Inversa.inversa_Par2 import determinante
def cerosLeft(matriz,fInicio,tamañoM,tamañoF,row,colum):        # Vuelve ceros columnas en diagonal izquierda
    print(f" Vuelta {colum} | Calculando determinate... ".center(80,"-"))
    for fila in range(fInicio,tamañoM):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente

### esta funawjdfhwjer
def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\t\n")

# INFORMACIÓN Y VARIABLES A USAR
matrix = [      
    [1, 3, 0, 1],
    [0, 2, 1, 4],
    [2, 1, 1, 0],
    [1, 0, 3, 1]
]

copyMatrix = copy.deepcopy(matrix)
size = len(matrix)  # Tamaño matriz
det = 1     # Determinante

# From INT to FLOAT
for i in range(size):
    for j in range (size):
        matrix[i][j] = float(matrix[i][j])

print(" Matriz a resolver: ".center(80,"="))       # Show Matrix
theMatrix(matrix)

# PARTE 1 | DETERMINANTE (Gauss Jordan)
c = 0       # Contador auxiliar para la función cerosLeft
while True:
    if c != size:
        f = matrix[c]   # Guarda filas y sus cambios
        cerosLeft(matrix,c+1,size, size,f,c)
        theMatrix(matrix)
        c += 1

    else:
        for i in range(size):
            det *= matrix[i][i]
        break

# DETERMINANTE
print(f" DETERMINATE: {det} ".center(50,"="))


# PARTE 2 | ADJUNTA 
# From INT to FLOAT
for i in range(size):
    for j in range (size):
        matrix[i][j] = float(matrix[i][j])

print(" Matriz a resolver: ".center(80,"="))       # Show Matrix
theMatrix(copyMatrix)

 # PARTE 2 | DETERMINANTE (pero Ley de Laplace)
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
    for i in range(4):
        filasAdjunta = []
        for j in range(4):
            print(f"Cofactor {i+1}, {j+1} ----")
            theMatrix(newMatrix3(copyMatrix, i,j))      # La matriz 3x3 se creá
            
            # Obtener determinante 3x3
            miniDet = sarrus(newMatrix3(copyMatrix, i,j))

            # Evalucaión de signos
            signo = ((i+1)+(j+1))% 2 
            print(f"signo | {signo}")
            if signo == 1:                          # Cofactores con signo (-)
                filasAdjunta.append(-1*miniDet)
            else: 
                filasAdjunta.append(miniDet)      # Cofactores con signo (+)
        matrixAdjunta.append(filasAdjunta)
        c += 1
    # c += 1

    if c == len(matrix):
        break

print(f"MATRIZ ADJUNTA".center(50,"="))
theMatrix(matrixAdjunta)

traspuesta = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
for i in range(size):
    for j in range(size):
        traspuesta[i][j] = matrixAdjunta[j][i]

print("MATRIZ TRANSPUESTA".center(50,"="))
theMatrix(traspuesta)

inversa = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

for i in range(size):
    for j in range(size):
        inversa[i][j] = traspuesta[i][j] / det

print(f"dter grande  {det}")
print("MATRIZ INVERSA".center(50,"="))
theMatrix(inversa)
