m = []

def elementos_matriz(n):
    for i in range (n):
        m.append([])
        for j in range (n):
            v= int(input("Introduzca valor:"))
            m[i].append(v)
    return m


def sarrus(m):
    det = ((m[0][0] * m[1][1] * m[2][2]) + (m[0][1] * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])) - ((m[2][0] * m [1][1] * m[0][2]) + (m[2][1] * m [1][2] * m[0][0]) + (m[2][2] * m[1][0] * m [0][1]))
    print("El determinante de la matriz por la regla de Srrus es: ", det)



