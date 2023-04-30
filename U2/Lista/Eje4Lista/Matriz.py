import os
class Nodo:
    def __init__(self,valor,fila,columna):
        self.__valor = valor
        self.__fila = fila
        self.__columna = columna
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig
    def setValor(self, valor):
        self.__valor = valor
    
    def getValor(self):
        return self.__valor

    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__columna

class Lista: #Lista Enlazada
    __comienzo: Nodo = None
    def __init__(self):
        self.__comienzo = None
        self.__tamaño = 0
    def getTamaño(self):
        return self.__tamaño
    def getComienzo(self):
        return self.__comienzo
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

    def anterior(self,fila,columna):

        if self.estaVacia():
            print('Esta Vacia')
        else:
            anterior = None
            nodo = self.__comienzo
            bandera = False
            while nodo != None and bandera == False:
                if fila < nodo.getFila():
                    anterior=nodo
                    bandera = True
                elif fila == nodo.getFila():
                    if columna < nodo.getColumna():
                        anterior=nodo
                        bandera = True
                else:
                    aux = nodo
                nodo = nodo.getSiguiente()

            if nodo == None:
                anterior = aux
            return anterior

    def insertar(self, valor, fila, columna):
    # Verifica si ya existe un nodo con la misma fila y columna que el nuevo nodo.
        nodoe = self.buscar(fila, columna)
        if nodoe is not None:
            self.__comienzo.setValor(valor)

    #Aca hace el resto de la implementacion
        else:
            nodo = Nodo(valor, fila, columna)
            if self.__comienzo is None:
                self.__comienzo = nodo
            else:
                if self.__comienzo.getFila() > fila:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo = nodo
                elif self.__comienzo.getFila() == fila:
                    if self.__comienzo.getColumna() > columna:
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo = nodo
                    elif self.__comienzo.getColumna() == columna:
                        self.__comienzo.setValor(valor)
                    else:
                        previo = self.anterior(fila, columna)
                        nodo.setSiguiente(previo.getSiguiente())
                        previo.setSiguiente(nodo)
                else:
                    previo = self.anterior(fila, columna)
                    nodo.setSiguiente(previo.getSiguiente())
                    previo.setSiguiente(nodo)
            self.__tamaño += 1

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

                
    def buscar(self, fila, columna):
        nodo = self.__comienzo
        while nodo is not None:
            if nodo.getFila() == fila and nodo.getColumna() == columna:
                return nodo
            nodo = nodo.getSiguiente()
        return None
    
    '''def buscar(self,valor):
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
        return pos'''
    
    def recorrer(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            while nodo.getSiguiente() != None:
                    print('Fila {} Columna {} Valor {}'.format(nodo.getFila(),nodo.getColumna(),nodo.getValor()))
                    nodo = nodo.getSiguiente()
        print('Fila {} Columna {} Valor {}'.format(nodo.getFila(),nodo.getColumna(),nodo.getValor()))
        print('\n')

def sumar_matrices(matriz1, matriz2):
    matriz_suma = Lista() # Crear una nueva matriz para almacenar los resultados

    nodo1 = matriz1.getComienzo()
    nodo2 = matriz2.getComienzo()

    while nodo1 is not None or nodo2 is not None:
        fila1 = columna1 = fila2 = columna2 = valor1 = valor2 = 0

        # Obtener los datos del primer nodo de la matriz 1
        if nodo1 is not None:
            fila1 = nodo1.getFila()
            columna1 = nodo1.getColumna()
            valor1 = nodo1.getValor()

        # Obtener los datos del primer nodo de la matriz 2
        if nodo2 is not None:
            fila2 = nodo2.getFila()
            columna2 = nodo2.getColumna()
            valor2 = nodo2.getValor()

        # Comparar las filas y columnas de los nodos para determinar la suma
        if fila1 < fila2 or (fila1 == fila2 and columna1 < columna2):
            # Si el nodo de la matriz 1 es menor, se agrega a la matriz de suma
            matriz_suma.insertar(valor1, fila1, columna1)
            nodo1 = nodo1.getSiguiente()

        elif fila1 > fila2 or (fila1 == fila2 and columna1 > columna2):
            # Si el nodo de la matriz 2 es menor, se agrega a la matriz de suma
            matriz_suma.insertar(valor2, fila2, columna2)
            nodo2 = nodo2.getSiguiente()

        else:
            # Si las filas y columnas son iguales, se suman los valores y se agrega a la matriz de suma
            valor_suma = valor1 + valor2
            matriz_suma.insertar(valor_suma, fila1, columna1)
            nodo1 = nodo1.getSiguiente()
            nodo2 = nodo2.getSiguiente()

    return matriz_suma
def mult_matrices(matriz1, matriz2):
    matriz_suma = Lista() # Crear una nueva matriz para almacenar los resultados

    nodo1 = matriz1.getComienzo()
    nodo2 = matriz2.getComienzo()

    while nodo1 is not None or nodo2 is not None:
        fila1 = columna1 = fila2 = columna2 = valor1 = valor2 = 0

        # Obtener los datos del primer nodo de la matriz 1
        if nodo1 is not None:
            fila1 = nodo1.getFila()
            columna1 = nodo1.getColumna()
            valor1 = nodo1.getValor()

        # Obtener los datos del primer nodo de la matriz 2
        if nodo2 is not None:
            fila2 = nodo2.getFila()
            columna2 = nodo2.getColumna()
            valor2 = nodo2.getValor()

        # Comparar las filas y columnas de los nodos para determinar la suma
        if fila1 < fila2 or (fila1 == fila2 and columna1 < columna2):
            # Si el nodo de la matriz 1 es menor, se agrega a la matriz de suma
            matriz_suma.insertar(valor1, fila1, columna1)
            nodo1 = nodo1.getSiguiente()

        elif fila1 > fila2 or (fila1 == fila2 and columna1 > columna2):
            # Si el nodo de la matriz 2 es menor, se agrega a la matriz de suma
            matriz_suma.insertar(valor2, fila2, columna2)
            nodo2 = nodo2.getSiguiente()

        else:
            # Si las filas y columnas son iguales, se suman los valores y se agrega a la matriz de suma
            valor_suma = valor1 * valor2
            matriz_suma.insertar(valor_suma, fila1, columna1)
            nodo1 = nodo1.getSiguiente()
            nodo2 = nodo2.getSiguiente()

    return matriz_suma
"""def sumar(matrizMayor,matrizMenor):
    matrizR = Lista()
    nodo1 = matrizMayor.getComienzo()
    nodo2 = matrizMenor.getComienzo()
    valor = 0
    fila = 0
    columna = 0
    bandera = False
    while nodo1 !=None:
        while nodo2 != None:
            if nodo1.getFila() == nodo2.getFila() and nodo1.getColumna() == nodo2.getColumna():
                valor = nodo1.getValor() + nodo2.getValor()
                fila = nodo1.getFila()
                columna = nodo1.getColumna()
                bandera = True
            nodo2 = nodo2.getSiguiente()
        nodo2 = matrizMenor.getComienzo()
        if bandera == True:
            matrizR.insertar(valor,fila,columna)
        else:
            matrizR.insertar(nodo1.getValor(),nodo1.getFila(),nodo1.getColumna())
        nodo1 = nodo1.getSiguiente()
    
    return matrizR"""

if __name__ == '__main__':

    os.system('cls')
    matriz1 = Lista()
    matriz1.insertar(2,4,5)
    matriz1.insertar(10,4,2)
    matriz1.insertar(5,3,2)
    matriz1.insertar(4,2,2)
    matriz1.insertar(6,2,2)
    matriz1.insertar(8,2,2)
    matriz1.insertar(9,1,4)
    matriz1.insertar(20,10,4)
    
    matriz2 = Lista()
    matriz2.insertar(2,4,5)
    matriz2.insertar(10,6,8)
    matriz2.insertar(5,10,4)
    
    matriz2.insertar(9,8,7)

    matriz1.recorrer()
    matriz2.recorrer()

    matriz_suma = sumar_matrices(matriz1, matriz2)
    matriz_suma.recorrer()

    matriz_mult = mult_matrices(matriz1, matriz2)
    matriz_mult.recorrer()

    """if matriz1.getTamaño() > matriz2.getTamaño():
        matrizR = sumar(matriz1,matriz2)
        matrizR.recorrer()
    else:
        matrizR = sumar(matriz2,matriz1)
        matrizR.recorrer()"""
