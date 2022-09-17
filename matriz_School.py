# Matrix 4x4

def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:7}'.format(item) for item in row])for row in keanu]) + "\n")

# Define matrix

matrix = [
    [1, -2, 2, -3, 15],
    [3,  4, -1, 1, -6],
    [2, -3, 2, -1, 17],
    [1, 1, -3, -2, -7],
]

# Variable for equations size
size = len(matrix[0])

# Define row (fila)
r1 = matrix[0]; r2 = matrix[1]
r3 = matrix[2]; r4 = matrix[3]

# From INT to FLOAT
for i in range(len(matrix)):
    for j in range (len(matrix[0])):
        matrix[i][j] = float(matrix[i][j])

# Part 1: Show the matrix
print(" > Vuelve el sistema una matriz < ".center(50,"-") +"\n")
theMatrix(matrix)

# CERO 1 - column 1
coeficiente = r2[0]*(-1)/r1[0]       # Divide 3/1 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r2[colum] += r1[colum] * coeficiente

print(" CERO 1: Fila 2 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 2 - column 1
coeficiente = r3[0]*(-1)/r1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r3[colum] += r1[colum] * coeficiente

print(" CERO 2: Fila 3 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 3 - column 1
coeficiente = r4[0]*(-1)/r1[0]       # Divide -1/4 to got coef. and modify file 2
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r4[colum] += r1[colum] * coeficiente

print(" CERO 3: Fila 4 - Fila 1 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 4 - colum 2
coeficiente = r3[1]*(-1)/r2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r3[colum] += r2[colum] * coeficiente

print(" CERO 4: Fila 3 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 5 - colum 2
coeficiente = r4[1]*(-1)/r2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r4[colum] += r2[colum] * coeficiente

print(" CERO 5: Fila 4 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 6 - colum 3
coeficiente = r4[2]*(-1)/r3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r4[colum] += r3[colum] * coeficiente

print(" CERO 6: Fila 4 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 7 - colum 4
coeficiente = r1[3]*(-1)/r4[3]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r1[colum] += r4[colum] * coeficiente

print(" CERO 7: Fila 1 - Fila 4 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 8 - colum 4
coeficiente = r2[3]*(-1)/r4[3]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r2[colum] += r4[colum] * coeficiente

print(" CERO 8: Fila 2 - Fila 4 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 9 - colum 4
coeficiente = r3[3]*(-1)/r4[3]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0,size):
    r3[colum] += r4[colum] * coeficiente

print(" CERO 9: Fila 3 - Fila 4 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 10
coeficiente = r1[2]*(-1)/r3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r1[colum] += r3[colum] * coeficiente

print(" CERO 10: Fila 1 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# CERO 11
coeficiente = r2[2]*(-1)/r3[2]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r2[colum] += r3[colum] * coeficiente

print(" CERO 11: Fila 2 - Fila 3 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)


# CERO 12
coeficiente = r1[1]*(-1)/r2[1]
print(f"· Coeficiente: {coeficiente}") # PROFF

for colum in range(0, size):
    r1[colum] += r2[colum] * coeficiente

print(" CERO 12: Fila 1 - Fila 2 * coeficiente ".center(50,"·")+"\n")
theMatrix(matrix)

# Guardar denominadores
deno1 = r1[0]
deno2 = r2[1]
deno3 = r3[2]
deno4 = r1[3]

# Diagonal de 1
for colum in range(0, size):
    r1[colum] /= deno1
    r2[colum] /= deno2
    r3[colum] /= deno3
    r4[colum] /= deno4

print(" MATRIZ IDENTIDAD ".center(50,"=") +"\n")
theMatrix(matrix)

print(f"Result ->\t W = {r1[4]}\t X = {r2[4]}\t Y = {r3[4]}\t Z = {r4[4]}")