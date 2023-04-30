import numpy as np

class Nodo:
    __elemento = None
    __siguiente = None

    def setSiguiente(self, sig):
        self.__siguiente = sig
    
    def getDato(self):
        return self.__elemento
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__elemento = dato


class ListaCursores:
    __cab = None
    __arreglo = None
    __maximo = None
    __cantidad = None
    __disponible = None


    def __init__(self, maximo = 10):
        self.__arreglo = np.empty(maximo, dtype = Nodo)
        self.__maximo = maximo
        self.__cantidad = 0
        self.__cab = -1
        self.__disponible = 0
        for i in range(self.__maximo):
            nodo = Nodo()
            self.__arreglo[i] = nodo
        for  j in range(self.__maximo-1):
            self.__arreglo[j].setSiguiente(i+1)
        self.__arreglo[self.__maximo-1].setSiguiente(-1)

    
    
    def vacio(self):
        return (self.__cantidad == 0)
    
    def lleno(self):
        return (self.__cantidad == self.__maximo)

    


    def insertar_posicion(self, p, elemento):
        if p>=1 and p<=self.__cantidad+1:
            self.__arreglo[self.__disponible].setDato(elemento)
            if self.vacio():
                self.__arreglo[self.__disponible].setSiguiente(self.__cab)
                self.__cab = self.__disponible
                self.__disponible+=1
                self.__cantidad+=1
            else:
                if not self.lleno():
                    aux = self.__cab
                    ant = aux
                    band = False
                    i = 0
                    while aux != -1 and not band:
                        if i == p-1:
                            band = True
                        else:
                            i+=1
                            ant = aux
                            aux = self.__arreglo[aux].getSiguiente()
                    if i == 0:#Insertar en la primer posicion de la lista
                        self.__arreglo[self.__disponible].setSiguiente(self.__cab)
                        self.__cab = self.__disponible
                        self.__cantidad+=1
                        self.__disponible+=1
                    else:
                        self.__arreglo[self.__disponible].setSiguiente(aux)
                        self.__arreglo[ant].setSiguiente(self.__disponible)
                        self.__cantidad+=1
                        self.__disponible+=1
                else:
                    print('ERROR: Lista llena!')
        else:
            print('ERROR: Posicion ingresada no valida!')

    def suprimir_posicion(self, p):
        if p >= 1 and p<=self.__cantidad:
            if not self.vacio():
                encontro = False
                i = 0
                aux = self.__cab
                ant = aux
                while aux != -1 and not encontro:
                    if i == p-1:
                        encontro = True
                    else:
                        i+=1
                        ant = aux
                        print(ant)
                        aux = self.__arreglo[aux].getSiguiente()
                self.__arreglo[ant].setSiguiente(self.__arreglo[aux].getSiguiente())
                self.__cantidad-=1
                self.__disponible = aux#la nueva celda disponible será la posicion en donde se elimino le nodo
            else:
                print('ERROR: Lista vacia')
        else:
            print('ERROR: Posicion no valida!')
    
    def insertar_contenido(self, elemento):
        if not self.lleno():
            self.__arreglo[self.__disponible].setDato(elemento)
            if self.vacio():
                self.__arreglo[self.__disponible].setSiguiente(self.__cab)
                self.__cab = self.__disponible
                self.__disponible+=1
                self.__cantidad+=1
                
            else:
                aux = self.__cab
                ant = aux
                encontro = False
                while not encontro and aux != -1:
                    if elemento > self.__arreglo[aux].getDato():
                        encontro = True
                    else:
                        ant = aux
                        aux = self.__arreglo[aux].getSiguiente()
                if aux == self.__cab:
                    self.__arreglo[self.__disponible].setSiguiente(self.__cab)
                    self.__cab = self.__disponible
                    self.__disponible+=1
                    self.__cantidad+=1
                else:
                    self.__arreglo[ant].setSiguiente(self.__disponible)
                    self.__arreglo[self.__disponible].setSiguiente(aux)
                    self.__disponible+=1
                    self.__cantidad+=1       
        else:
            print('ERROR: Lista llena!')
    
    def buscar(self, elemento):
        p = None
        if not self.vacio():
            i = 0
            aux = self.__cab
            encontro = False
            while aux != -1 and not encontro:
                if elemento == self.__arreglo[aux].getDato():
                    encontro = True
                else:
                    aux = self.__arreglo[aux].getSiguiente()
                    i+=1
            p = i
        else:
            print('ERROR: Lista vacia!')
        return p
    
    def recuperar(self, p):
        elem = None
        if p>=0 and p <= self.__cantidad-1:
            if not self.vacio():
                i = 0
                encontro = False
                aux = self.__cab
                while not encontro:
                    if i == p:
                        encontro = True
                    else:
                        i+=1
                        aux = self.__arreglo[aux].getSiguiente()
                elem = self.__arreglo[aux].getDato()
        return elem
                
    def supimir_contenido(self, elemento):
        if not self.vacio():
            encontro = False
            aux = self.__cab
            ant = aux
            i = 0
            while not encontro and aux != -1:
                if elemento == self.recuperar(i):
                    encontro = True
                else:
                    i+=1
                    ant =aux
                    aux = self.__arreglo[aux].getSiguiente()
            if not encontro:
                print('ERROR: Elemento no encontrado!')
            else:
                self.__arreglo[ant].setSiguiente(self.__arreglo[aux].getSiguiente())
                self.__disponible = aux
        else:
            print('ERROR: Lista vacia!')
    
    def primer_elemento(self):
        return self.__arreglo[self.__cab].getDato()
    
    def ultimo_elemento(self):
        aux = self.__cab
        ant = aux
        elemento = None
        while aux != -1:
            ant =aux
            aux = self.__arreglo[aux].getSiguiente()
        elemento = self.__arreglo[ant].getDato()
        return elemento
        
    def recorrer(self):
        aux = self.__cab
        while aux != -1:
            print(self.__arreglo[aux].getDato())
            aux = self.__arreglo[aux].getSiguiente()
    
    def anterior(self, p):
        val =None
        if p > 1 and p <= self.__cantidad:
            i = 0
            encontro = None
            aux = self.__cab
            ant = aux
            while aux != -1 and not encontro:
                if i == p-1:
                    
                    encontro = True
                else:
                    i+=1
                    ant = aux
                    aux = self.__arreglo[aux].getSiguiente()
            val = self.__arreglo[ant].getDato()
            
        else:
            print('ERROR: Posicion no valida!')
        return val
            

if __name__ == '__main__':
    obj = ListaCursores()
    for i in range(3):
        num = input("ingresa num")
        obj.insertar_contenido(num)
    nums = input("num a sumprimir")
    obj.supimir_contenido(nums)
    obj.recorrer()