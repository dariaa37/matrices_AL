# Tipo M:   MATRIZ 8x8
# Program:  Matrix con funciones y fors para resolver por columnas
# Name:     Karla Díaz Aguilar

def lonelyCero(cero,f,coef,tam):
    for i in range(0,tam):
        cero[i] += f[i] * coef

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:9}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix

matrix = [
    [-3, 2, -4, 1, -9],
    [4,  -2, -2, 3, -27],
    [2, 4, 1, -5, 18],
    [7, -3, 2, -9, -4],
]

# Variable for equations size
sizeM = len(matrix)
sizeF = len(matrix[0])

# Define row (fila)
f1 = matrix[0]; f2 = matrix[1]
f3 = matrix[2]; f4 = matrix[3]

# From INT to FLOAT
for i in range(sizeM):
    for j in range (sizeF):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(100,"-") +"\n")
theMatrix(matrix)