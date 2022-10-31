matriz = []

def elementos_matriz(n):
    for i in range (n):
        matriz.append([])
        for j in range (n):
            v= int(input("Introduzca valor:"))
            matriz[i].append(v)
    return matriz
n =3
print(elementos_matriz(n))