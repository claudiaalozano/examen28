#class Naves:
lista = []
def lista_naves():
    
    lista.append(["Halcón Milenario", 2000, 100, 300])
    lista.append(["Estrella de la muerte", 5000, 1000, 4000])
    lista.append(["Caza TIE", 20, 1, 2])
    lista.append(["Lanzadera imperial", 100, 5, 10])
    lista.append(["Ala-X / X-Wing", 50, 1,2])

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


lista_naves()
print(mostrar_info())