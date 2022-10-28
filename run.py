from ejercicio1 import *
from ejercicio4 import *
from ejercicio5 import *

if __name__ == "__main__":
    ej = int(input("Introduzca el número del ejercicio que desea ejecutar: "))
    if ej == 1:
        juego(d, torre_inc, torre_aux, torre_fin)
    elif ej == 4:
        polinomio1 = int(input("Introduzca el valor de la incognita x: "))
        gradopolinomio1= int(input("Introduzca el grado del polinomio: "))
        for i in range(0,gradopolinomio1):
            coeficiente = int(input("\n introduzca el coeficiente: "))
            print("(", str(coeficiente) + ")" + str(polinomio1) + " ^ " + str(gradopolinomio1 -i))
        polinomio2 = int(input("Introduzca el valor de la incognita x: "))
        gradopolinomio2= int(input("Introduzca el grado del polinomio: "))
        for i in range(0,gradopolinomio2):
            coeficiente = int(input("\n introduzca el coeficiente: "))
            print("(", str(coeficiente) + ")" + str(polinomio2) + " ^ " + str(gradopolinomio2 -i))
        restar(polinomio1, polinomio2)

    elif ej == 5:
        encriptacion()
        desencriptacion ()
            