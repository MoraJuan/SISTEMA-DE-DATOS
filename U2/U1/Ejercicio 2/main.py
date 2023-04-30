import numpy as np

class Pila:
    __cant=0
    __tope=-1
    def __init__(self,cant):
        self.item = []
        self.__tope=-1
        self.__cant=cant

    def esta_vacia(self):
        return self.__tope == -1
    
    def llena(self):
        return self.__tope == self.__cant
    
    def Ultimo(self):
        return self.item[self.__tope]

    def agregar(self, dato):
        if(self.__tope <  self.__cant):
            self.__tope+=1
            self.item.append(dato)

    def sacar(self):
        if(self.esta_vacia()):
            print('Pila vacia')
            return (0)
        else:
            self.__tope-=1
            obj=self.item.pop(self.__tope)
            return obj

    def tamano(self):
        count = 0
        for _ in self.item:
            count += 1
        return count
    
    def Mostrar(self):
        if not self.vacia():
            i=self.__tope
            while(i>=0):
                print(self.item)
                i-=1

class JuegoHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.pila1 = Pila(4)
        self.pila2 = Pila(4)
        self.pila3 = Pila(4)
        self.movimientos = 0

        for i in range(num_discos, 0, -1):
            self.pila1.agregar(i)

    def imprimir_estado(self):
        print("Pila1:", self.pila1.item)
        print("Pila2:", self.pila2.item)
        print("Pila3:", self.pila3.item)

    def mover(self, pila_origen, pila_destino):
        if pila_origen == 1:
            origen = self.pila1
        elif pila_origen == 2:
            origen = self.pila2
        elif pila_origen == 3:
            origen = self.pila3
        else:
            print("Pila origen inválida")
            return False

        if pila_destino == 1:
            destino = self.pila1
        elif pila_destino == 2:
            destino = self.pila2
        elif pila_destino == 3:
            destino = self.pila3
        else:
            print("Pila destino inválida")
            return False

        if origen.esta_vacia():
            print("La pila origen está vacía")
            return False

        disco = origen.sacar()
        if not destino.esta_vacia() and disco > destino.item[-1]:
            print("No se puede colocar un disco encima de otro más pequeño")
            origen.agregar(disco)
            return False

        destino.agregar(disco)
        self.movimientos += 1
        return True

    def jugar(self):
        print("Estado inicial del juego:")
        self.imprimir_estado()

        while self.pila1.tamano() != 0 or self.pila2.tamano() != 0:
            pila_origen = int(input("Indique la pila origen: "))
            pila_destino = int(input("Indique la pila destino: "))

            if self.mover(pila_origen, pila_destino):
                self.imprimir_estado()

        print("Juego terminado en", self.movimientos, "movimientos.")
        print("Número mínimo de movimientos:", 2**self.num_discos-1)

# Ejemplo de ejecución
juego = JuegoHanoi(3)
juego.jugar() 
