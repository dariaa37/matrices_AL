def theMatrix(keanu):
    print('\n'.join([''.join(['\t{:9}'.format(item) for item in row])for row in keanu]) + "\n")


# Matrices
mA = [
    [-2,3],
    [-5,1],
    [0,-6]
]

mB = [
    [1,-5,0],
    [-8,9,2]
]

mC = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# PROCESO
for row in range(3):
    for colum in range(3):
        cons = 0
        for coef in range(2):
            cons += mA[row][coef] * mB[coef][colum]
        mC[row][colum] = cons

print("RESULTADO DE AxB = C".center(60,"="))
theMatrix(mC)