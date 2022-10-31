#class Naves:
lista = []
def lista_naves():
    
    lista.append(["Halcón Milenario", 800, 100, 300])
    lista.append(["Estrella de la muerte", 5000, 3000, 7000])
    lista.append(["Caza TIE", 20, 1, 2])
    lista.append(["Lanzadera imperial", 100, 5, 10])
    lista.append(["Ala-X / X-Wing", 50, 1,2])
    lista.append(["Supremacy" , 500 , 200, 350 ])

def mostrar_info():
    p= str(input("¿De que nave desea tener información (Halcón Milenario o Estrella de la muerte)?: "))
    if p== "Halcón Milenario":
        print("La infirmación del halcón milenario es: ")
        print("Largo de la nave: ", lista[0][1]) 
        print("Tripulación: ", lista[0][2])
        print("Cantidad de pasajeros: ", lista[0][3])
    if p=="Estrella de la muerte":
        print("La infirmación de la Estrella de la muerte es: ")
        print("Largo de la nave: ", lista[1][1]) 
        print("Tripulación: ", lista[1][2])
        print("Cantidad de pasajeros: ", lista[1][3])
    else:
        print("Valor introducido incorrecto.")

def mayor_cantidad_pasajeros( buscado):
    lista_pasajeros = []
    lista_pasajeros.append(lista[0][2])
    lista_pasajeros.append(lista[1][2])
    lista_pasajeros.append(lista[2][2])
    lista_pasajeros.append(lista[3][2])
    lista_pasajeros.append(lista[4][2])
    lista_pasajeros.append(lista[5][2])
    lista_pasajeros.sort()
   
    posicion = -1
    primero = 0
    ultimo = len(lista_pasajeros)-1
    lista_5 =[]
    while (primero <= ultimo) and ( posicion == -1):
        medio = (primero + ultimo) // 2
        if(lista_pasajeros[medio] == buscado):
            posicion = medio
            lista_5.append(lista_pasajeros[posicion])
        else:
            if(buscado<lista_pasajeros[medio]):
                ultimo = medio - 1
                lista_5.append(lista_pasajeros[ultimo])
            else:
                primero = medio + 1
                lista_5.append(lista_pasajeros[primero])
    return lista_5

lista_naves()
print(mayor_cantidad_pasajeros( buscado))