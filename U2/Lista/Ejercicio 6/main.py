class Nodo:
    def __init__(self, pos, tamano, siguiente=None):
        self.pos = pos
        self.tamano = tamano
        self.siguiente = siguiente
    
    def __str__(self):
        return f"[Inicio: {self.pos}, Tamaño: {self.tamano}]"


class Lista:
    def __init__(self):
        self.comienzo = None
    
    def estaVacia(self):
        return self.comienzo == None
    
    def insertar(self, pos, tamano):
        nuevoNodo = Nodo(pos, tamano)
        if self.estaVacia():
            self.comienzo = nuevoNodo
        else:
            aux = self.comienzo
            anterior = None
            while aux != None and aux.pos < pos:
                anterior = aux
                aux = aux.siguiente
            if anterior == None:
                nuevoNodo.siguiente = self.comienzo
                self.comienzo = nuevoNodo
            elif aux == None:
                anterior.siguiente = nuevoNodo
            else:
                nuevoNodo.siguiente = aux
                anterior.siguiente = nuevoNodo

    def mejorAjuste(self, tamano):
        aux = self.comienzo
        anterior = None
        seleccionado = None
        while aux != None:
            if aux.tamano >= tamano and (seleccionado == None or aux.tamano < seleccionado.tamano):
                seleccionado = aux
                anterior = anterior
            anterior = aux
            aux = aux.siguiente
        if seleccionado != None:
            if seleccionado.tamano == tamano:
                if anterior == None:
                    self.comienzo = seleccionado.siguiente
                else:
                    anterior.siguiente = seleccionado.siguiente
            else:
                seleccionado.pos += tamano
                seleccionado.tamano -= tamano
        return seleccionado

if __name__ == '__main__':
    xLista = Lista()
    xLista.insertar(13, 9)
    xLista.insertar(10, 2)
    xLista.insertar(8, 9)
    mejor_ajuste = xLista.mejorAjuste(6)
    print(mejor_ajuste)