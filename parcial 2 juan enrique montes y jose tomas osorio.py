import random
vector = []

for _ in range(50):
    numero_entero = random.randint(1, 20)
    vector.append(numero_entero)

print(f"Primer vector:\n {vector}")

segundo_vector = []

for numero in vector:
    if numero not in segundo_vector:
        segundo_vector.append(numero)

print(f"Segundo vector:\n {segundo_vector}")

tercer_vector = []

for numero in segundo_vector:
    cantidad_repeticiones = vector.count(numero)
    tercer_vector.append(cantidad_repeticiones)

print(f"Tercer vector:\n {tercer_vector}")

num_contar = int(input("Ingrese un numero para contarlo en el primer vector (de 1 al 20)"))

cantidad_repetido = 0

for numero in vector:
    if numero == num_contar:
        cantidad = vector.count(numero)
        cantidad_repetido = cantidad
        break;

print(f"El numero {num_contar} se repite: {cantidad_repetido}")

tamaño_vector1 = 0
tamaño_vector2 = 0
tamaño_vector3 = 0

for _ in vector:
    tamaño_vector1 = tamaño_vector1 + 1

for _ in segundo_vector:
    tamaño_vector2 = tamaño_vector2 + 1

for _ in tercer_vector:
    tamaño_vector3 = tamaño_vector3 + 1

print(f"El tamaño de los vectores es: 1={tamaño_vector1} 2={tamaño_vector2} 3={tamaño_vector3}")

#PUNTO 2 A

matriz = []

for i in range(5):
    fila = []
    for j in range(5):
        valor = random.randint(100, 200)
        fila.append(valor)
    matriz.append(fila)

print("Primer Matriz:\n")   
for fila in matriz:
    print(fila)

print("")

#PUNTO B    
segunda_matriz = [[],[],[],[],[]]

for elemento in matriz: 
    for indice, valor in enumerate(elemento):
    
        if indice == 0:
            resultado = pow(valor, 2)
            segunda_matriz[0].append(resultado)
        elif indice == 1:
            resultado = pow(valor, 4)
            segunda_matriz[1].append(resultado)
        elif indice == 2:
            resultado = pow(valor, 2)
            segunda_matriz[2].append(resultado)
        elif indice == 3:
            resultado = pow(valor, 4)
            segunda_matriz[3].append(resultado)
        else:
            resultado = pow(valor, 2)
            segunda_matriz[4].append(resultado)

print("Segunda Matriz:\n")            
for fila in segunda_matriz:
    print(fila)
    
print("")

#PUNTO C    
suma_filas = []

for elemento in matriz:
    suma = 0
    for valor in elemento:
        suma += valor
    
    suma_filas.append(suma)

print(f"Vector suma filas: {suma_filas}")

#PUNTO D
suma_columnas = []

suma1 = 0
suma2 = 0
suma3 = 0
suma4 = 0
suma5 = 0

for elemento in segunda_matriz:
    for indice,valor in enumerate(elemento):
        if indice == 0:
            suma1+=valor
        elif indice == 1:
            suma2+=valor
        elif indice == 2:
            suma3+=valor
        elif indice == 3:
            suma4+=valor
        else:
            suma5+=valor
            
suma_columnas.append(suma1)
suma_columnas.append(suma2)
suma_columnas.append(suma3)
suma_columnas.append(suma4)
suma_columnas.append(suma5)
    
print(f"Vector suma columnas: {suma_columnas}")

print("")

#PUNTO E
matriz_diferencia = []
    
for i in range(5):
    fila = []
    for j in range(5):
        diferencia = segunda_matriz[i][j] - matriz[i][j]
        fila.append(diferencia)
    matriz_diferencia.append(fila)
    
print("Matriz Diferencia:")
for fila in matriz_diferencia:
    print(fila)

print("")

#PUNTO F
numero = int(input("Ingrese el numero a multiplicar por la matriz: "))

matriz_producto = []
    
for i in range(5):
    fila = []
    for j in range(5):
        producto = matriz[i][j] * numero
        fila.append(producto)
    matriz_producto.append(fila)
    
print("Matriz producto:")
for fila in matriz_producto:
    print(fila)

print("")

#PUNTO G
producto_matrices = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        for k in range(len(segunda_matriz)):
            producto_matrices[i][j] += matriz[i][k] * segunda_matriz[k][j]

print("Producto matriz uno por matriz dos:")
for fila in producto_matrices:
    print(fila)

print("")

#PUNTO H
suma_diagonal = 0

for i in range(len(matriz)):
    suma_diagonal += matriz[i][i]

print(f"Suma de la diagonal principal en la matriz uno es: {suma_diagonal}")

print("")

#PUNTO I
suma_diagonal_inversa = 0

for i in range(len(segunda_matriz)):
    suma_diagonal_inversa += segunda_matriz[i][len(segunda_matriz) - 1 - i]
    
print(f"Suma de la diagonal inversa en la matriz dos es: {suma_diagonal_inversa}" )
print("")

#PUNTO J
suma_elementos = 0

for elemento in producto_matrices:
    for valor in elemento:
        suma_elementos += valor

media = suma_elementos / len(producto_matrices)

print(f"La media de la matriz producto de dos matrices es: {media}")