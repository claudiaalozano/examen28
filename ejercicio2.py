matriz = []

def elementos_matriz(n):
    for i in range (n):
        matriz.append([])
        for j in range (n):
            v= int(input("Introduzca valor:"))
            matriz[i].append()
    return matriz

n = int(input('Dimensiones de la matriz: '))
print(elementos_matriz(n))