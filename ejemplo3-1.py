#Otra solucion para el ejercicio N° 3

cadena = 'Hola mundo'

for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end='')
print()
print(cadena[::-1])
