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

    def setValor(self, valor):
        self.__valor = valor

class Lista: 
    def __init__(self):
        self.__comienzo = None
        self.__tamaño = 1

    def estaVacia(self):
        return self.__comienzo == None

    def siguiente(self,valor):
        if self.estaVacia:
            print('Lista Vacia')
        else:
            siguiente = None
            nodo = self.__comienzo
            while nodo != None:
                if nodo.getValor() == valor:
                    siguiente = nodo.getSiguiente()
                nodo = nodo.getSiguiente()
        return siguiente

    def anterior(self,posicion):
        if self.estaVacia:
            print('Esta Vacia')
        else:
            pos = 1
            anterior = None
            nodo = self.__comienzo
            while nodo != None:
                if pos == posicion:
                    anterior = nodo
                nodo = nodo.getSiguiente()
                pos+=1
        return anterior
        
    def insertar(self, valor):
        
        anterior:Nodo = None 
        siguiente = None
        nuevo = Nodo(int(valor))
        if(self.__comienzo == None):
            self.__comienzo = nuevo
            nuevo.setSiguiente(None)
        elif (self.__comienzo.getValor() == valor):
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        else:
            p = self.__comienzo
            anterior = None

            while((p != None) and (valor > p.getValor())):
                anterior = p 
                p = p.getSiguiente()
            if anterior == None:
                self.__comienzo = nuevo
            else:
                anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(p)
        print("Listo :)")

    
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
        nodo = self.__comienzo
        while(nodo.getSiguiente() != None):
            print(nodo.getValor())
            nodo = nodo.getSiguiente()
        print(nodo.getValor())
        
            
if __name__ == '__main__':
    xLista = Lista()
    for i in range(5):
        num = input('Ingrese valor')
        xLista.insertar(int(num))
    xLista.recorrer()