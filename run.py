from EJERCICIO1.ejercicio1 import *
from EJERCICIO2.ejercicio2 import *
from EJERCICIO3.ejercicio3 import *
from EJERCICIO4.ejercicio4 import *
from EJERCICIO5.ejercicio5 import *

def menu():
    ej = int(input("Introduzca el número del ejercicio que desea ejecutar: "))
    if ej == 1:
        d = int(input("Introduce en número de discos: "))
        juego( d, torre_inc, torre_aux, torre_fin)
    
    elif ej == 2:
        n =3
        print(elementos_matriz(n), sarrus(m)) 

    elif ej == 3:
        lista_naves()
        print(mayor_cantidad_pasajeros())
        print(naves_at())
        print(mayor_tripulacion())
        print(seis_pasajeros())
        print(inf_peq_may())
    
    elif ej == 4:
        polinomio1 = Polinomio()
        agregar(polinomio1, 2, 2)
        agregar(polinomio1, 1, -1)
        agregar(polinomio1, 0, 2)
        polinomio2 = Polinomio()
        agregar(polinomio2, 3, -1)
        agregar(polinomio2, 2, 6)
        agregar(polinomio2, 1, 3)
        agregar(polinomio2, 0, 1)
        print("La resta de los polinomios es: " , mostrar(restar(polinomio1, polinomio2)))
        print("La división de los polinomios es: " ,mostrar(dividir(polinomio1, polinomio2)))
        print(mostrar(eliminar_un_termino(polinomio1)))
        print(buscar_termino(polinomio1))
    
    elif ej == 5:
        
        c = str(input("Introduce el mensaje para encriptar: ")).encode("utf-8")
        resolver = str(input("Hash a resolver: "))
        encriptacion(c, resolver)
        
            