import os
class Nodo:
    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig
    
    def getValor(self):
        return self.__valor

class Lista: #Lista Enlazada, por posicion
    __comienzo: Nodo = None
    def __init__(self):
        self.__comienzo = None
        self.__tamaño = 1

    def estaVacia(self):
        return self.__comienzo == None

    def siguiente(self,valor):
        if self.estaVacia():
            print('Lista Vacia')
        else:
            siguiente = None
            nodo = self.__comienzo
            pos = 1
            while nodo != None:
                if pos == valor:
                    siguiente = nodo.getSiguiente()
                nodo = nodo.getSiguiente()
                pos+=1
        return siguiente

    def anterior(self,posicion)->Nodo:

        if self.estaVacia():
            print('Esta Vacia')
        else:
            pos = 1
            anterior = None
            nodo = self.__comienzo
            while nodo != None:
                pos+=1
                if pos == posicion:
                    anterior = nodo
                nodo = nodo.getSiguiente()
        return anterior

    def insertar(self,valor,posicion):
        if posicion > self.__tamaño:
            raise 'Fuero de Rango'
        nodo = Nodo(valor)
        if posicion == 1:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            print('Se inserto correctamente en la cabeza')
        else:
            previo = self.anterior(posicion)
            nodo.setSiguiente(previo.getSiguiente())
            previo.setSiguiente(nodo)

            print('Se inserto correctamente')
        self.__tamaño +=1

    def suprimir(self,valor):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            if self.__comienzo.getValor()== valor:
                self.__comienzo = self.__comienzo.getSiguiente
            else:
                previo = self.anterior(valor)
                sig = self.siguiente(valor)
                previo.setSiguiente(sig)

    def buscar(self,valor):
        bandera = False
        pos = 0
        nodo = self.__comienzo
        while nodo != None and bandera != True:
            if nodo.getValor() == valor:
                print('Encontre el elemento')
                bandera = True
            pos+=1
            nodo = nodo.getSiguiente()
        if bandera ==  False:
            pos = -1
        else:
            pos = pos -1
        return pos
    def recorrer(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            while nodo.getSiguiente() != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()
        print(nodo.getValor())

if __name__ == '__main__':
    os.system('cls')
    lista = Lista()
    lista.insertar(1,1)
    lista.insertar(2,2)
    lista.insertar(3,2)
    lista.insertar(4,2)
    lista.insertar(5,3)
    lista.insertar(6,4)
    lista.recorrer()
    print('\n')
    lista.suprimir(2)
    lista.suprimir(5)
    lista.recorrer()