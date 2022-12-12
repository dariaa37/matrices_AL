# Tipo M:   MATRIZ 4x4
# Program:  Matrix con funciones y fors para resolver por columnas
# Name:     Karla Díaz Aguilar

import copy

def cerosLeft(matriz,fInicio,tamañoM,tamañoF,row,colum):        # Vuelve ceros columnas en diagonal izquierda
    for fila in range(fInicio,tamañoM):  # Se repite 3 veces a partir de 1
        print(f"{matriz[fila][colum]} | {row} | {colum} ")
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        print(f"coeficiente = {coeficiente}")
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente

def cerosRight(matriz,fFinal,tamañoM,tamañoF,row,colum):        # Vuelve 0 columnas diagonal derecha
    for fila in range(tamañoM-fFinal):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente



def lonelyCero(cero,f,tam,columna):
    coef = cero[columna]*(-1)/f[columna]
    for i in range(0,tam):
        cero[i] += f[i] * coef

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:9}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix

matrixOriginal = [
    [-3, 2, -4, 1, -9],
    [4,  -2, -2, 3, -27],
    [2, 4, 1, -5, 18],
    [7, -3, 2, -9, -4],
]

matrix = copy.deepcopy(matrixOriginal)
variable = []

# Variable for equations size
sizeM = len(matrix)
sizeF = len(matrix[0])

# Define row (fila)
f1 = matrix[0]; f2 = matrix[1]; f3 = matrix[2]; f4 = matrix[3]

# From INT to FLOAT
for i in range(sizeM):
    for j in range (sizeF):
        matrix[i][j] = float(matrix[i][j])

# Ingresar variables
print(" Ingresa las VARIABLES de la matriz ".center(50,"-"))
for i in range(sizeM):
    variable.append(input(f"\t\tVariable {i+1}:\t"))

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(95,"-") +"\n")
theMatrix(matrix)

# # COLUMNA 0 - Ceros 1,2,3
cerosLeft(matrix,1,sizeM,sizeF,f1,0)
print(" CERO 1,2 y 3: Fila 2,4 y4 - Fila 1 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# # COLUMNA 1 - Ceros 4 y 5
cerosLeft(matrix,2,sizeM,sizeF,f2,1)
print(" CERO 4 y 5: Fila 3 y 4 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

#### SOLO PRUEBA -----------------------------
# # COLUMNA 2 - Cero 6
cerosLeft(matrix,3,sizeM,sizeF,f3,2)
print(" CERO 4 y 5: Fila 3 y 4 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)

# # COLUMNA 2 - Cero 6 (Único cero de la columna)
# lonelyCero(f4,f3,sizeF,2)     # único cero faltante de la columna
# print(" CERO 6: Fila 4 - Fila 3 * coeficiente ".center(95,"·")+"\n")
# theMatrix(matrix) 


# # COLUMNA 3 - Ceros 7,8,9
cerosRight(matrix,1,sizeM,sizeF,f4,3)
print(" CERO 7,8 y 9: Fila 1,2 y 3 - Fila 4 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# # COLUMNA 2 - Ceros 10 y 11
cerosRight(matrix,2,sizeM,sizeF,f3,2)
print(" CERO 10 y 11: Fila 1 y 2 - Fila 3 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# COLUMNA 1 - Cero 12 (Único y último cero de la columna)
lonelyCero(f1,f2,sizeF,1)     # único cero faltante de la columna
print(" CERO 12: Fila 1 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix) 

# SALIDA PARA USUARIO
# Guardar denominadores
deno1 = f1[0];      deno2 = f2[1];      deno3 = f3[2];      deno4 = f4[3]

# Diagonal de 1
for colum in range(0, sizeF):
    # El valor de incognitas =     indice de 1/valores de columna 4
    f1[colum] /= deno1
    f2[colum] /= deno2
    f3[colum] /= deno3
    f4[colum] /= deno4

print(" MATRIZ IDENTIDAD ".center(95,"=") +"\n")
theMatrix(matrix)

print(" RESULTADOS ".center(50,"="))
for i in range(0,sizeM):        # Redondear (si se necesita)
    value = matrix[i][4]
    print(f"\t\t   | {variable[i]} =  {round(value)} |")

# Sustituir en ecuaciones (comprobación)
print("\n" + " COMPROBACIÓN POR SUSTITUCIÓN ".center(50,"="))
for i in range(0,sizeM):        # Accedo a cant de filas de matriz
    result = 0
    for j in range(0,sizeM):    # Accedo a elementos por fila
        result += matrixOriginal[i][j] * matrix[j][4]
    print(f"\t\tEcuación {i+1}:\t{round(result)}")