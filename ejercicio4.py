#restar, dividir, eliminar un término y determinar si un término existe en un polinomio

class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    def __init__(self,valor, termino):
        self.valor = valor 
        self.termino = termino


class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

def agregar(polinomio, termino, valor):
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if(termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino 
    else:
        actual = polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig 
        aux.sig = actual.sig
        actual.sig = aux


def modificar(polinomio, termino, valor):
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino != termino):
        aux = aux.sig 
    aux.info.valor = valor

def obtener_valor(polinomio, termino):
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino > termino):
        aux = aux.sig 
    if(aux is not None and aux.info.termino == termino):
        return aux.info.valor  
        