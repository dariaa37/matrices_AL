# MATRIZ 3X3
# Matrix con operaciones una por una sin funciones

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix

matrix = [
    [-4, 1, 0, -18],
    [1, -3, 1, 0],
    [0, 1, -2, 0],
]

# Variable for equations size
size = len(matrix[0])

# Define row (fila)
f1 = matrix[0]
f2 = matrix[1]
f3 = matrix[2]

# From INT to FLOAT
for i in range(len(matrix)):
    for j in range (len(matrix[0])):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(50,"-") +"\n")
theMatrix(matrix)

# CERO 1
coeficiente = f2[0]*(-1)/f1[0]       # Divide 2/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    f2[colum] += f1[colum] * coeficiente

print(" CERO 1: Fila 2 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 2
coeficiente = f3[0]*(-1)/f1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    f3[colum] += f1[colum] * coeficiente

print(" CERO 2: Fila 3 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 3
coeficiente = f3[1]*(-1)/f2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    f3[colum] += f2[colum] * coeficiente

print(" CERO 3: Fila 3 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 4
coeficiente = f1[2]*(-1)/f3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    f1[colum] += f3[colum] * coeficiente

print(" CERO 4: Fila 1 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 5
coeficiente = f2[2]*(-1)/f3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    f2[colum] += f3[colum] * coeficiente

print(" CERO 5: Fila 2 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 6
coeficiente = f1[1]*(-1)/f2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    f1[colum] += f2[colum] * coeficiente

print(" CERO 6: Fila 1 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# Guardar denominadores
deno1 = f1[0]
deno2 = f2[1]
deno3 = f3[2]

# Diagonal de 1
for colum in range(0, size):
    f1[colum] /= deno1
    f2[colum] /= deno2
    f3[colum] /= deno3

print(" MATRIZ IDENTIDAD ".center(50,"=") +"\n")
theMatrix(matrix)

# Redondear
x = f1[3];      y = f2[3];          z = f3[3]

print(f"Result ->\t X = {round(x)}\t Y = {round(y)}\t Z = {round(z)}")