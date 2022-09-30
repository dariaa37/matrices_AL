#   Gilberto Gutiérrez Vázquez
#   Eliminación gausiana

from fractions import Fraction

largo = int(input('Ingrese el número máximo de coeficientes: '))
numfila = largo-1

tabla = []
mul = []

for i in range(numfila):
   f = (input(f'\nDigite los coeficientes de la {i+1} ecuación separados por comas (si no hay, ponga 0): '))
   f = f.split(sep=',')
   tabla.append([])
   for j in f:
       tabla[i].append(int(j))

print(tabla)

fila = 0
tamlargo = 0
inverso = 0

while fila < numfila:
   inverso = 1/(tabla[0][tamlargo])

   for columna in range(0, len(tabla[fila])):
       tabla[0][columna] = tabla[0][columna] * inverso

   for i in range(1, numfila):
      mul.append(tabla[i][tamlargo]*-1)

   for i in range(1,numfila):
       for j in range(0,largo):
           tabla[i][j] = (tabla[0][j]*mul[i-1]) + tabla[i][j]


   tabla.append(tabla[0])
   del tabla[0]

   mul = []
   fila += 1
   tamlargo += 1

print('')
print('Los resultados son: ')
for fila4 in range(0,len(tabla)):
   v = Fraction(str(tabla[fila4][numfila])).limit_denominator()
   print(f'La {fila4+1} variable es igual a: {v}')

