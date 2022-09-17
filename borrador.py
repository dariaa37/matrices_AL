# Matrix
def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix

matrix = [
    [1, 2, 3, 6],
    [2, -3, 2, 14],
    [3, 1, -1, -2],
]

# Variable for equations size
sizeM = len(matrix)
sizeF = len(matrix[0])

# Define row (fila)
f1 = matrix[0];     f2 = matrix[1];     f3 = matrix[2]
coeficiente = 0

# From INT to FLOAT
for i in range(len(matrix)):
    for j in range (len(matrix[0])):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(50,"-") +"\n")
theMatrix(matrix)

# COLUMNA 0
for fila in range(1,sizeM):  # Se repite 3 veces a partir de 1
    coeficiente = matrix[fila][0]*(-1)/f1[0]
    for columna in range(0,sizeF):       # Se repite 4 veces
        print(coeficiente)
        matrix[fila][columna] += f1[columna] * coeficiente

print(" CERO 1: Fila 2 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)
