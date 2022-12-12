def prettyMatrix(A):
    print('\n'+'\n'.join([''.join(['{:9.4}'.format(float(elemento)) for elemento in fila]) for fila in A])+'\n')

sistema = [
    # [2, 0, 1],
    # [3, 0, 0],
    # [5, 1, 1]

    # [-3, 2, 0],
    # [1, -1, 2],
    # [-2, 1, 3]

    [5, -2, 4],
    [6, 7, -3],
    [3, 0, 2]
]

#prettyMatrix(sistema)

def determinante(a):
    if (len(a) == 2):
        print("if 2-------")
        prettyMatrix(a)
        detA = a[0][0] * a[1][1] - a[0][1] * a[1][0]

    if (len(a) == 3):
        print("if 3------")
        prettyMatrix(a)
        a1 = a[0][0] * determinante( [ [ a[1][1], a[1][2] ], [  a[2][1], a[2][2] ] ] )
        a2 = a[0][1] * determinante( [ [ a[1][0], a[1][2] ], [  a[2][0], a[2][2] ] ] )
        a3 = a[0][2] * determinante( [ [ a[1][0], a[1][1] ], [  a[2][0], a[2][1] ] ] )
        detA = a1 - a2 + a3

    return detA

detA = determinante(sistema)
print("Determinante: "+str(detA))

adjunta = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
#for i in range(3):
    #for j in range(3):
        
        #adjunta[i][j] = (-1)^((i+1)+(j+1)) * determinante

print("Llenando andjunta")
adjunta[0][0] = determinante([[sistema[1][1], sistema[1][2]],[sistema[2][1], sistema[2][2]]])
adjunta[0][1] = -determinante([[sistema[1][0], sistema[1][2]],[sistema[2][0], sistema[2][2]]])
adjunta[0][2] = determinante([[sistema[1][0], sistema[1][1]],[sistema[2][0], sistema[2][1]]])
adjunta[1][0] = -determinante([[sistema[0][1], sistema[0][2]],[sistema[2][1], sistema[2][2]]])
adjunta[1][1] = determinante([[sistema[0][0], sistema[0][2]],[sistema[2][0], sistema[2][2]]])
adjunta[1][2] = -determinante([[sistema[0][0], sistema[0][1]],[sistema[2][0], sistema[2][1]]])
adjunta[2][0] = determinante([[sistema[0][1], sistema[0][2]],[sistema[1][1], sistema[1][2]]])
adjunta[2][1] = -determinante([[sistema[0][0], sistema[0][2]],[sistema[1][0], sistema[1][2]]])
adjunta[2][2] = determinante([[sistema[0][0], sistema[0][1]],[sistema[1][0], sistema[1][1]]])

print("MATRIZ ADJUNTA")
prettyMatrix(adjunta)

traspuesta = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(3):
    for j in range(3):
        traspuesta[i][j] = adjunta[j][i]

print("MATRIZ TRANSPUESTA")
prettyMatrix(traspuesta)


inversa = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(3):
    for j in range(3):
        inversa[i][j] = traspuesta[i][j] / detA

print("MATRIZ INVERSA")
prettyMatrix(inversa)
