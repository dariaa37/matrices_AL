# Tipo M:   MATRIZ 4x4
# Program:  Matrix con funciones y fors para resolver por columnas
# Name:     Karla Díaz Aguilar

def cerosLeft(matriz,fInicio,tamañoM,tamañoF,row,colum):        # Vuelve ceros columnas en diagonal izquierda
    for fila in range(fInicio,tamañoM):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[0]}")
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente

def cerosRight(matriz,fFinal,tamañoM,tamañoF,row,colum):        # Vuelve 0 columnas diagonal derecha
    for fila in range(tamañoM-fFinal):  # Se repite 3 veces a partir de 1
        coeficiente = matriz[fila][colum]*(-1)/row[colum]
        print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[0]}")
        for columna in range(0,tamañoF):       # Se repite 4 veces
            matriz[fila][columna] += row[columna] * coeficiente

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
print(" > Vuelve el sistema una matriz < ".center(95,"-") +"\n")
theMatrix(matrix)

# # COLUMNA 0 - Ceros 1,2,3
# for fila in range(1,sizeM):  # Se repite 3 veces a partir de 1
#     coeficiente = matrix[fila][0]*(-1)/f1[0]
#     print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[0]}")
#     for columna in range(0,sizeF):       # Se repite 4 veces
#         matrix[fila][columna] += f1[columna] * coeficiente

cerosLeft(matrix,1,sizeM,sizeF,f1,0)
print(" CERO 1,2 y 3: Fila 2,4 y4 - Fila 1 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# # COLUMNA 1 - Ceros 4 y 5
# for fila in range(2,sizeM):  # Se repite 3 veces a partir de 1
#     coeficiente = matrix[fila][1]*(-1)/f2[1]
#     print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[0]}")
#     for columna in range(0,sizeF):       # Se repite 4 veces
#         matrix[fila][columna] += f2[columna] * coeficiente

cerosLeft(matrix,2,sizeM,sizeF,f2,1)
print(" CERO 4 y 5: Fila 3 y 4 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# COLUMNA 2 - Cero 6 (Único cero de la columna)
coeficiente = f4[2]*(-1)/f3[2]          # Obtego coeficiente
print(coeficiente)
lonelyCero(f4,f3,coeficiente,sizeF)     # único cero faltante de la columna
print(" CERO 6: Fila 4 - Fila 3 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix) 


# # COLUMNA 3 - Ceros 7,8,9
# for fila in range(sizeM-1):  # Se repite 3 veces a partir de 1
#     coeficiente = matrix[fila][3]*(-1)/f4[3]
#     print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[0]}")
#     for columna in range(0,sizeF):       # Se repite 4 veces
#         matrix[fila][columna] += f4[columna] * coeficiente

cerosRight(matrix,1,sizeM,sizeF,f4,3)
print(" CERO 7,8 y 9: Fila 1,2 y 3 - Fila 4 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# # COLUMNA 2 - Ceros 10 y 11
# for fila in range(sizeM-2):  # Se repite 3 veces a partir de 1
#     coeficiente = matrix[fila][2]*(-1)/f3[2]
#     print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[2]}")
#     for columna in range(0,sizeF):       # Se repite 4 veces
#         matrix[fila][columna] += f3[columna] * coeficiente

cerosRight(matrix,2,sizeM,sizeF,f3,2)
print(" CERO 10 y 11: Fila 1 y 2 - Fila 3 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix)


# COLUMNA 1 - Cero 12 (Único y último cero de la columna)
coeficiente = f1[1]*(-1)/f2[1]          # Obtego coeficiente
print(coeficiente)
lonelyCero(f1,f2,coeficiente,sizeF)     # único cero faltante de la columna
print(" CERO 12: Fila 1 - Fila 2 * coeficiente ".center(95,"·")+"\n")
theMatrix(matrix) 

# SALIDA PARA USUARIO
# Guardar denominadores
deno1 = f1[0];      deno2 = f2[1]
deno3 = f3[2];      deno4 = f4[3]

# Diagonal de 1
for colum in range(0, sizeF):
    # El valor de incognitas =     indice de 1/valores de columna 4
    f1[colum] /= deno1
    f2[colum] /= deno2
    f3[colum] /= deno3
    f4[colum] /= deno4

print(" MATRIZ IDENTIDAD ".center(95,"=") +"\n")
theMatrix(matrix)

# Redondear (si se necesita)
x = f1[4];      y = f2[4];          z = f3[4];      w = f4[4]

print(f"Result:\t X = {round(x)}\t Y = {round(y)}\t Z = {round(z)}\t W = {round(w)}".center(95))