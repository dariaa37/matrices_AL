# Tipo M:   MATRIZ 3X3
# Program:  Matrix con funciones y fors para resolver por columnas
# Name:     Karla Díaz Aguilar

def lonelyCero(cero,f,coef,tam):
    for i in range(0,tam):
        cero[i] += f[i] * coef

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix
matrix = [[], [], []]

# Array for variables
variable = []

# Variable for matrix size
sizeM = len(matrix)

# Ingresa literales de la ecuación -----------------
print(" Ingresa las VARIABLES de la matriz ".center(50,"-"))
for i in range(sizeM):
    variable.append(input(f"\t\tVariable {i+1}:\t"))

# Ingresa ------------------------------------------
for i in range(sizeM):
    print(f"Ingresa datos de ecuación {1}".center(50,"-"))
    for j in range(sizeM +1):
        if j < sizeM:       # Solo imprime ecuaciones con literales
            matrix[i].append(float(input(f"\t\tValor {variable[j]}:\t")))
        else:
            matrix[i].append(float(input(f"\t\t\Resultado:\t")))


# Variable for equations size
sizeF = len(matrix[0])

# Define row (fila)
f1 = matrix[0];     f2 = matrix[1];     f3 = matrix[2]
coeficiente = 0

# From INT to FLOAT
for i in range(sizeM):
    for j in range (sizeF):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(50,"-") +"\n")
theMatrix(matrix)

# COLUMNA 0 (Resuelve CERO 1 y CERO 2)
for fila in range(1,sizeM):  # Se repite 3 veces a partir de 1
    coeficiente = matrix[fila][0]*(-1)/f1[0]
    print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[0]}")
    for columna in range(0,sizeF):       # Se repite 4 veces
        matrix[fila][columna] += f1[columna] * coeficiente

print(" · CERO 1 y 2: Fila 2/3 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# COLUMNA 1 (Resuelve el unico cero en la columna 1 = CERO 3)
coeficiente = f3[1]*(-1)/f2[1]          # Obtego coeficiente
lonelyCero(f3,f2,coeficiente,sizeF)     # único cero faltante de la columna
print(" CERO 3: Fila 3 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)   # Estado de la matrix


# COLUMNA 2
for fila in range(sizeM-1):  # Se repite 3 veces a partir de 1
    coeficiente = matrix[fila][2]*(-1)/f3[2]
    print(f"This is coeficiente: {coeficiente}   Fila: {fila}  f1o: {f1[2]}")
    for columna in range(0,sizeF):       # Se repite 4 veces
        matrix[fila][columna] += f3[columna] * coeficiente

print(" CERO 4 y 5: Fila 1 y 2 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# COLUMNA 1 (come back to end)
coeficiente = f1[1]*(-1)/f2[1]          # Obtego coeficiente
lonelyCero(f1,f2,coeficiente,sizeF)     # único cero faltante de la columna
print(" CERO 6: Fila 1 (nuevamente) - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)   # Estado de la matrix


# Guardar denominadores
deno1 = f1[0]
deno2 = f2[1]
deno3 = f3[2]

# Diagonal de 1
for colum in range(0, sizeF):
    f1[colum] /= deno1
    f2[colum] /= deno2
    f3[colum] /= deno3

print(" MATRIZ IDENTIDAD ".center(50,"=") +"\n")
theMatrix(matrix)

print(" RESULTADOS ".center(50,"="))
# Redondear (si se necesita)
for i in range(0,sizeM):
    value = matrix[i][3]
    print(f"\t\t| {variable[i]} =  {round(value)} |")