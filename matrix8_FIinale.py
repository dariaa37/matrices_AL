# Tipo M:   MATRIZ 8x8
# Program:  Matrix con funciones y fors para resolver por columnas
# Name:     Karla Díaz Aguilar

def cerosLeft(matriz,fInicio,tamañoM,tamañoF,row,colum):        # Vuelve ceros columnas en diagonal izquierda
    for fila in range(fInicio,tamañoM):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente

def cerosRight(matriz,fFinal,tamañoM,tamañoF,row,colum):        # Vuelve 0 columnas diagonal derecha
    for fila in range(tamañoM-fFinal):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente

def lonelyCero(cero,f,coef,tam):
    for i in range(0,tam):
        cero[i] += f[i] * coef

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\t\n")

# Define matrix

matrix = [
     [-2, 3, -8, -7, 6,	3, 5, 3, -98],
     [7, -3, -4, 3, -3, -3, 4, 3, 89],
     [3, -5, 3, 2, -3, -5, -4, 5, 71],
     [3, 5, 4, 7, 3, -2, -6, -3, 73],
     [6, 2, -2, 5, 2, -3, 1, -5, 62],
     [-3, 2, 4, 8, 3, -5, 5, 6, 163],
     [-6, 8, -6, -3, 4, -8, -2, 2, -63],
     [-3, 4, 7, 7, -7, -6, 4, -8, 117]
]

# Variable for equations size
sizeM = len(matrix)
sizeF = len(matrix[0])

# Define row (fila)
f1 = matrix[0]; f2 = matrix[1]; f3 = matrix[2]; f4 = matrix[3]
f5 = matrix[4]; f6 = matrix[5]; f7 = matrix[6]; f8 = matrix[7]

# From INT to FLOAT
for i in range(sizeM):
    for j in range (sizeF):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(100,"-") +"\n")
theMatrix(matrix)

# INICIO PROCESOS ------------------------------------------

# CEROS IZQUIERDA <<<<<<<
# COLUMNA 0 - Ceros 1-7
cerosLeft(matrix,1,sizeM,sizeF,f1,0)
print(" CERO 1 a 7: Fila 2 a 8 - Fila 1 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 1 - Ceros 8-13
cerosLeft(matrix,2,sizeM,sizeF,f2,1)
print(" CERO 8 a 13: Fila 3 a 8 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 2 - Ceros 14-18
cerosLeft(matrix,3,sizeM,sizeF,f3,2)
print(" CERO 14 a 18: Fila 4 a 8 - Fila 3 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 3 - Ceros 19-22
cerosLeft(matrix,4,sizeM,sizeF,f4,3)
print(" CERO 19 a 22: Fila 5 a 8 - Fila 4 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 4 - Ceros 23-25
cerosLeft(matrix,5,sizeM,sizeF,f5,4)
print(" CERO 23 a 25: Fila 6 a 8 - Fila 5 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 5 - Ceros 26-27
cerosLeft(matrix,6,sizeM,sizeF,f6,5)
print(" CERO 26 y 27: Fila 6 a 8 - Fila 6 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 6 - Cero 28 (Único cero de la columna)
coeficiente = f8[6]*(-1)/f7[6]          # Obtego coeficiente
lonelyCero(f8,f7,coeficiente,sizeF)     # único cero faltante de la columna
print(" CERO 28: Fila 8 - Fila 7 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix) 

# CEROS DERECHA >>>>>>>
# COLUMNA 7 - Ceros 29-35
cerosRight(matrix,1,sizeM,sizeF,f8,7)
print(" CERO 29-35: Fila 1 a 7 - Fila 8 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 6 - Ceros 36-41
cerosRight(matrix,2,sizeM,sizeF,f7,6)
print(" CERO 36-41: Fila 1 a 6 - Fila 7 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 5 - Ceros 42-46
cerosRight(matrix,3,sizeM,sizeF,f6,5)
print(" CERO 42-46: Fila 1 a 5 - Fila 6 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 4 - Ceros 47-50
cerosRight(matrix,4,sizeM,sizeF,f5,4)
print(" CERO 47-50: Fila 1 a 4 - Fila 5 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 3 - Ceros 51-53
cerosRight(matrix,5,sizeM,sizeF,f4,3)
print(" CERO 51-53: Fila 1 a 3 - Fila 4 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 2 - Ceros 54 y 55
cerosRight(matrix,6,sizeM,sizeF,f3,2)
print(" CERO 54 y 55: Fila 1 y 2 - Fila 3 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# COLUMNA 1 - Cero 56 (Único y último cero de la columna)
coeficiente = f1[1]*(-1)/f2[1]          # Obtego coeficiente
lonelyCero(f1,f2,coeficiente,sizeF)     # único cero faltante de la columna
print(" CERO 56: Fila 1 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix) 

# SALIDA PARA USUARIO
# Guardar denominadores
deno1 = f1[0];      deno2 = f2[1];      deno3 = f3[2];      deno4 = f4[3]
deno5 = f5[4];      deno6 = f6[5];      deno7 = f7[6];      deno8 = f8[7]

# Diagonal de 1
for colum in range(0, sizeF):
    # El valor de incognitas =     indice de 1/valores de columna 4
    f1[colum] /= deno1;    f2[colum] /= deno2;
    f3[colum] /= deno3;    f4[colum] /= deno4;
    f5[colum] /= deno5;    f6[colum] /= deno6;
    f7[colum] /= deno7;    f8[colum] /= deno8

print(" MATRIZ IDENTIDAD ".center(95,"=") +"\n")
theMatrix(matrix)

variables = ["a","b","c","d","e","f","g","h"]
resultado = []

print(" RESULTADOS ".center(95,"="))
# Redondear (si se necesita)
for i in range(0,sizeM):
    literal = matrix[i][8]
    print(f"| {variables[i]} =  {round(literal)} |".rjust(55))
