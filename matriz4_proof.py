# Matrix 4x4
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
for i in range(len(matrix)):
    for j in range (len(matrix[0])):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(50,"-") +"\n")
theMatrix(matrix)

# CERO 1 - column 0
coeficiente = f2[0]*(-1)/f1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f2[colum] += f1[colum] * coeficiente

print(" CERO 1: Fila 2 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 2 - column 1
coeficiente = f3[0]*(-1)/f1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f3[colum] += f1[colum] * coeficiente

print(" CERO 2: Fila 3 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 3 - column 1
coeficiente = f4[0]*(-1)/f1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f4[colum] += f1[colum] * coeficiente

print(" CERO 3: Fila 4 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 4 - colum 2
coeficiente = f3[1]*(-1)/f2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,sizeF):
    f3[colum] += f2[colum] * coeficiente

print(" CERO 4: Fila 3 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 5 - colum 2
coeficiente = f4[1]*(-1)/f2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,sizeF):
    f4[colum] += f2[colum] * coeficiente

print(" CERO 5: Fila 4 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 6 - colum 3
coeficiente = f4[2]*(-1)/f3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,sizeF):
    f4[colum] += f3[colum] * coeficiente

print(" CERO 6: Fila 4 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 7 - colum 4
coeficiente = f1[3]*(-1)/f4[3]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,sizeF):
    f1[colum] += f4[colum] * coeficiente
    round(f1[colum])

print(" CERO 7: Fila 1 - Fila 4 * coeficiente ".center(50,"·")+"\n")
print(f1)

theMatrix(matrix)

# CERO 8 - colum 4
coeficiente = f2[3]*(-1)/f4[3]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f2[colum] += f4[colum] * coeficiente

print(" CERO 8: Fila 2 - Fila 4 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 9 - colum 4
coeficiente = f3[3]*(-1)/f4[3]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,sizeF):
    f3[colum] += f4[colum] * coeficiente

print(" CERO 9: Fila 3 - Fila 4 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 10
coeficiente = f1[2]*(-1)/f3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f1[colum] += f3[colum] * coeficiente

print(" CERO 10: Fila 1 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 11
coeficiente = f2[2]*(-1)/f3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f2[colum] += f3[colum] * coeficiente

print(" CERO 11: Fila 2 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 12
coeficiente = f1[1]*(-1)/f2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, sizeF):
    f1[colum] += f2[colum] * coeficiente

print(" CERO 12: Fila 1 - Fila 2 * coeficiente ".center(50,"·")+"\n")
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

print(" MATRIZ IDENTIDAD ".center(50,"=") +"\n")
theMatrix(matrix)

# Redondear (si se necesita)
x = f1[4];      y = f2[4];          z = f3[4];      w = f4[4]

print(f"Result:\t X = {round(x)}\t Y = {round(y)}\t Z = {round(z)}\t W = {round(w)}")