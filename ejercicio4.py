#restar, dividir, eliminar un término y determinar si un término existe en un polinomio

class datoPolinomio(object):
    def __init__(self,valor, termino):
        self.valor = valor 
        self.termino = termino


class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

