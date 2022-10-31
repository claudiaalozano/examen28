from ejercicio1 import *
from ejercicio2 import *
from ejercicio4 import *
from ejercicio5 import *

if __name__ == "__main__":
    ej = int(input("Introduzca el número del ejercicio que desea ejecutar: "))
    if ej == 1:
        d = int(input("Introduce en número de discos: "))
        juego( d, torre_inc, torre_aux, torre_fin)
    
    elif ej == 2:
        n =3
        print(elementos_matriz(n), sarrus(m)) 
    
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
        encriptacion()
        desencriptacion ()
            