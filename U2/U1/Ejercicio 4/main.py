import random

class Nodo:
    def __init__(self, elemento):
        self.__siguiente = None
        self.__elemento = elemento
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getElemento(self):
        return self.__elemento
    
    def setElemento(self, elemento):
        self.__elemento = elemento
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

class ColaEncadenada:
    def __init__(self):
        self.__ultimo = None
        self.__primero = None
        self.__cantidad = 0
        
    def Vacio(self):
        resultado = None
        if self.__cantidad == 0:
            resultado = True
        else: 
            resultado = False
        return resultado
        
    def Insertar(self, valor):  
        nuevo_nodo = Nodo(valor)
        if self.__ultimo == None:
            self.__primero = nuevo_nodo
        else:
            self.__ultimo.setSiguiente(nuevo_nodo)
            self.__cantidad += 1
        self.__ultimo = nuevo_nodo
        valor = nuevo_nodo.getElemento()
        return valor

    def Suprimir(self):
        valor = None
        if not self.Vacio():
            valor = self.__primero.getElemento()
            self.__primero = self.__primero.getSiguiente()
            self.__cantidad -= 1
            if self.__primero == None:
                self.__ultimo = None
        else: 
            print('Cola Vacia')
        return valor

class Cliente:
    def __init__(self, numero, tiempo_llegada):
        self.__numero = numero
        self.__tiempo_llegada = tiempo_llegada
        self.__tiempo_espera = 0
    
    def getNumero(self):
        return self.__numero
    
    def calculo_tiempo_espera(self, tiempo_Actual):
        valor = tiempo_Actual - self.__tiempo_llegada
        self.__tiempo_espera = valor
    
    def get_tiempo_espera(self):
        return self.__tiempo_espera 

if __name__ == '__main__':
    Cola1 = ColaEncadenada()
    Cola2 = ColaEncadenada()
    Cola3 = ColaEncadenada()
    tiempo_atencion1 = 5
    tiempo_atencion2 = 3
    tiempo_atencion3 = 4
    frecuencia_llegada1 = 2
    frecuencia_llegada2 = 2
    frecuencia_llegada3 = 2
    tiempo_simulacion = 120 # 2 horas en minutos
    
    clientes_atendidos = 0
    clientes_sin_atender = 0
    tiempo_espera_total = 0

    for tiempo_actual in range(tiempo_simulacion):
        # Generar llegada de clientes aleatoriamente
        llegada1 = random.random() < (1 / frecuencia_llegada1)
        llegada2 = random.random() < (1 / frecuencia_llegada2)
        llegada3 = random.random() < (1 / frecuencia_llegada3)
        
        if llegada1:
            cliente1 = Cliente(clientes_atendidos + 1, tiempo_actual)
            clientes_atendidos +=1
                    # Insertar el cliente en la cola 1
            Cola1.Insertar(cliente1)
        if llegada2:
            cliente2 = Cliente(clientes_atendidos + 1, tiempo_actual)
            clientes_atendidos += 1
            # Insertar el cliente en la cola 2
            Cola2.Insertar(cliente2)
        
        if llegada3:
            cliente3 = Cliente(clientes_atendidos + 1, tiempo_actual)
            clientes_atendidos += 1
            # Insertar el cliente en la cola 3
            Cola3.Insertar(cliente3)
        
        # Atender clientes en cada cola
        if not Cola1.Vacio():
            cliente1 = Cola1.Suprimir()
            cliente1.calculo_tiempo_espera(tiempo_actual)
            tiempo_espera_total += cliente1.get_tiempo_espera()
            if cliente1.get_tiempo_espera() <= tiempo_atencion1:
                    # Cliente atendido completamente, no se hace nada
                pass
            else:
                    # Cliente sigue en cola para la siguiente atención
                cliente1.calculo_tiempo_espera(tiempo_actual)
                Cola1.Insertar(cliente1)
            
        if not Cola2.Vacio():
            cliente2 = Cola2.Suprimir()
            
            cliente2.calculo_tiempo_espera(tiempo_actual)
            tiempo_espera_total += cliente2.get_tiempo_espera()
            if cliente2.get_tiempo_espera() <= tiempo_atencion2:
                # Cliente atendido completamente, no se hace nada
                pass
            else:
                # Cliente sigue en cola para la siguiente atención
                cliente2.calculo_tiempo_espera(tiempo_actual)
                Cola2.Insertar(cliente2)
                
        if not Cola3.Vacio():
            cliente3 = Cola3.Suprimir()
            cliente3.calculo_tiempo_espera(tiempo_actual)
            tiempo_espera_total += cliente3.get_tiempo_espera()
            if cliente3.get_tiempo_espera() <= tiempo_atencion3:
                # Cliente atendido completamente, no se hace nada
                pass
            else:
                # Cliente sigue en cola para la siguiente atención
                cliente3.calculo_tiempo_espera(tiempo_actual)
                Cola3.Insertar(cliente3)
        
# Calcular el promedio de tiempo de espera
promedio_tiempo_espera = tiempo_espera_total / clientes_atendidos

print("Clientes atendidos: ", clientes_atendidos)
print("Clientes sin atender: ", Cola1.Vacio() + Cola2.Vacio() + Cola3.Vacio())
print("Promedio de tiempo de espera: ", promedio_tiempo_espera)
        



        
    



