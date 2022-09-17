# Matrix

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix

matrix = [
    [1, 1, 1, -6],
    [2, 1, -1, -1],
    [1, -2, 3, -6],
]

# Variable for equations size
size = len(matrix[0])

# Define row (fila)
r1 = matrix[0]
r2 = matrix[1]
r3 = matrix[2]

# From INT to FLOAT
for i in range(len(matrix)):
    for j in range (len(matrix[0])):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(50,"-") +"\n")
theMatrix(matrix)

# CERO 1
coeficiente = r2[0]*(-1)/r1[0]       # Divide 2/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r2[colum] += r1[colum] * coeficiente

print(" CERO 1: Fila 2 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 2
coeficiente = r3[0]*(-1)/r1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r3[colum] += r1[colum] * coeficiente

print(" CERO 2: Fila 3 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 3
coeficiente = r3[1]*(-1)/r2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r3[colum] += r2[colum] * coeficiente

print(" CERO 3: Fila 3 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 4
coeficiente = r1[2]*(-1)/r3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r1[colum] += r3[colum] * coeficiente

print(" CERO 4: Fila 1 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 5
coeficiente = r2[2]*(-1)/r3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r2[colum] += r3[colum] * coeficiente

print(" CERO 5: Fila 2 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 6
coeficiente = r1[1]*(-1)/r2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r1[colum] += r2[colum] * coeficiente

print(" CERO 6: Fila 1 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# Guardar denominadores
deno1 = r1[0]
deno2 = r2[1]
deno3 = r3[2]

# Diagonal de 1
for colum in range(0, size):
    r1[colum] /= deno1
    r2[colum] /= deno2
    r3[colum] /= deno3

print(" MATRIZ COMPLETADA ".center(50,"=") +"\n")
theMatrix(matrix)

print(f"Result ->\t X = {r1[3]}\t Y = {r2[3]}\t Z = {r3[3]}")