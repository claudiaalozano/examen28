class nodoPila(object):
    info, sig = None, None

class Pila(object): #Clase de la pila

    def __init__(self,name): 
       #Para crear una pila vacía

        self.cima = None
        self.tamanio = 0
        self.name = name

def apilar(pila,dato):
#función para apilar los datos

    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def pila_vacia(pila):
#imprime true si la pila está vacía para
    return pila.cima is None

def desapilar(pila):
#quita el útimo elemento de la pila(el último que hemos introducido) y nos lo devuelve.
    if not pila_vacia(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x



def en_cima(pila):
#imprime el valor que está encima de la pila, es decir, el último valor que hemos introducido.

    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

def tamanio(pila):
#devuelve el número de elementos de la pila

    return pila.tamanio


def barrido(pila):
#muestra el contenido de la pila sin perder ningún dato. 

    paux = Pila()
    while not pila.pila_vacia(pila):
        dato = pila.desapilar(pila)
        print(dato)
        pila.apilar(paux, dato)

    while not pila.pila_vacia(paux):
        dato = pila.desapilar(paux)
        pila.apilar(pila, dato)


torre_inc = Pila("Torre inicial")
torre_aux = Pila("Torre auxiliar")
torre_fin = Pila("Torre final")
d = int(input("Introduce en número de discos: "))
