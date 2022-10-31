#class Naves:
lista = []
def lista_naves():
    
    lista.append(["Halcón Milenario", 800, 100, 300])
    lista.append(["Estrella de la muerte", 5000, 3000, 7000])
    lista.append(["Caza TIE", 20, 1, 2])
    lista.append(["Lanzadera imperial", 100, 5, 10])
    lista.append(["Ala-X / X-Wing", 50, 1, 4])
    lista.append(["Supremacy" , 500 , 200, 350 ])
    lista.append(["AT-AT", 200, 300, 400])

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

def mayor_cantidad_pasajeros():
    lista_pasajeros = []
    lista_pasajeros.append(lista[0][3])
    lista_pasajeros.append(lista[1][3])
    lista_pasajeros.append(lista[2][3])
    lista_pasajeros.append(lista[3][3])
    lista_pasajeros.append(lista[4][3])
    lista_pasajeros.append(lista[5][3])
    lista_pasajeros.append(lista[6][3])
    lista_pasajeros.sort()
    print("Los valores más altos de pasajeros son: ",lista_pasajeros[-5:], ", que corresponden a Ala-X / X-Wing, Lanzadera imperial, Halcón Milenario, Supremacy y Estrella de la muerte. ")
    
def naves_at():
    nombres = []
    nombres.append(lista[0][0])
    nombres.append(lista[1][0])
    nombres.append(lista[2][0])
    nombres.append(lista[3][0])
    nombres.append(lista[4][0])
    nombres.append(lista[5][0])
    nombres.append(lista[6][0])
    s = []
    for n in nombres:
        if n.startswith('AT') == True:
            s.append(n)
            print(s)
            
def mayor_tripulacion():
    mt = []
    mt.append(lista[0][2])
    mt.append(lista[1][2])
    mt.append(lista[2][2])
    mt.append(lista[3][2])
    mt.append(lista[4][2])
    mt.append(lista[5][2])
    mt.append(lista[6][2])
    print("Las tripulaciones son: ", mt, "y la mayor tripulación es: " , max(mt))

def seis_pasajeros():
    lista_pasajeros = []
    lista_pasajeros.append(lista[0][3])
    lista_pasajeros.append(lista[1][3])
    lista_pasajeros.append(lista[2][3])
    lista_pasajeros.append(lista[3][3])
    lista_pasajeros.append(lista[4][3])
    lista_pasajeros.append(lista[5][3])
    lista_pasajeros.append(lista[6][3])
    lista_pasajeros.sort()
    s = []


lista_naves()
print(mayor_cantidad_pasajeros())
print(naves_at())
print(mayor_tripulacion())