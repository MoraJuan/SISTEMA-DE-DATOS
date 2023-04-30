from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz
       
    def insertar(self, clave, subArbol):
        if subArbol is None:
            subArbol = self.__raiz
        
        if subArbol is None:
            nodo = Nodo(clave)
            self.__raiz = nodo
        else:
            if clave > subArbol.getClave():
                if subArbol.getSigDer() ==  None:
                    nodo = Nodo(clave)
                    subArbol.setSigDer(nodo)
                else:
                    self.insertar(clave, subArbol.getSigDer())
            elif clave < subArbol.getClave():
                if subArbol.getSigIzq() == None:
                    nodo = Nodo(clave)
                    subArbol.setSigIzq(nodo)
                else:
                    self.insertar(clave, subArbol.getSigIzq())
            else:
                print('ERROR: Elemento ya existente!')


    def eliminar(self, clave, subArbol):
        if subArbol is None:
            print("El elemento a eliminar no existe en el árbol")
        elif clave < subArbol.getClave():
            subArbol.setSigIzq(self.eliminar(clave, subArbol.getSigIzq()))
        elif clave > subArbol.getClave():
            subArbol.setSigDer(self.eliminar(clave, subArbol.getSigDer()))
        else:
            if subArbol.getSigIzq() is None and subArbol.getSigDer() is None:
                subArbol = None
            elif subArbol.getSigIzq() is None:
                subArbol = subArbol.getSigDer()
            elif subArbol.getSigDer() is None:
                subArbol = subArbol.getSigIzq()
            else:
                padre_sucesor = subArbol
                sucesor = subArbol.getSigDer()
                while sucesor.getSigIzq() is not None:
                    padre_sucesor = sucesor
                    sucesor = sucesor.getSigIzq()
                subArbol.setClave(sucesor.getClave())
                if padre_sucesor == subArbol:
                    padre_sucesor.setSigDer(sucesor.getSigDer())
                else:
                    padre_sucesor.setSigIzq(sucesor.getSigDer())
        return subArbol



    def buscar(self, clave, subArbol):
        if subArbol is None:
            return None
        
        if clave == subArbol.getClave():
            return subArbol
        
        if clave < subArbol.getClave():
            return self.buscar(clave, subArbol.getSigIzq())
        
        if clave > subArbol.getClave():
            return self.buscar(clave, subArbol.getSigDer())
        
        # Si llegamos aquí es porque no se encontró el nodo
        return None

    def nivel(self, clave, subArbol): #Aumenta el 1 cada vez que pasa de nivel
        if subArbol is None:
            return 0

        if clave == subArbol.getClave():
            return 1

        if clave < subArbol.getClave():
            return 1 + self.nivel(clave, subArbol.getSigIzq())

        if clave > subArbol.getClave():
            return 1 + self.nivel(clave, subArbol.getSigDer()) #Retornando asi la cantidad de veces que se hizo el bucle


    def Hoja(self, clave, subArbol):
        if clave < subArbol.getClave():
            return self.Hoja(clave, subArbol.getSigIzq())
            
        elif clave > subArbol.getClave():
            return self.Hoja(clave, subArbol.getSigDer())
            
        else:
            if subArbol.getSigIzq() is None and subArbol.getSigDer() is None:
                return True
            else:
                return False
    
    def Hijo(self, clave, subArbol, padre):
        if subArbol is None:
            return False

        if clave < subArbol.getClave():
            return self.Hijo(clave, subArbol.getSigIzq(), subArbol)

        if clave > subArbol.getClave():
            return self.Hijo(clave, subArbol.getSigDer(), subArbol)

        # si llegamos aquí, es porque encontramos el nodo con clave == subArbol.getClave()
        if subArbol != self.__raiz and clave < padre.getClave():
            print('Es hijo')
            return True
        else:
            print('No es hijo')
            return False

    def camino(self, clave, subArbol, camino):
        # Si el subárbol es None, no se encontró la clave y se retorna un camino vacío
        if subArbol is None:
            return False

        # Si se encontró la clave, se agrega al camino y se retorna el camino
        if clave == subArbol.getClave():
            camino.append(subArbol.getClave())
            return camino

        # Si la clave es menor que la clave del nodo actual, se busca en el subárbol izquierdo
        if clave < subArbol.getClave():
            camino.append(subArbol.getClave())
            return self.camino(clave, subArbol.getSigIzq(), camino)

        # Si la clave es mayor que la clave del nodo actual, se busca en el subárbol derecho
        if clave > subArbol.getClave():
            camino.append(subArbol.getClave())
            return self.camino(clave, subArbol.getSigDer(), camino)


         
    
    
                
    def inorden(self, subArbol): #Muestra todos los resueltados en orden
        if subArbol != None:
            self.inorden(subArbol.getSigIzq())
            print(subArbol.getClave(), end=" ")
            self.inorden(subArbol.getSigDer())       
            
