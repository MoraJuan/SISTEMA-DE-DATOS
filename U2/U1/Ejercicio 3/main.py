#   El Laboratorio de Computación tiene una única impresora, a la cual llegan trabajos para imprimir de cualquiera
#   de las máquinas. Considerando que los trabajos llegan cada 5 minutos a la cola de impresión. Se requiere simular
#   el comportamiento de dicha cola, teniendo en cuenta que cada trabajo tiene asociado el tiempo que se demorará
#   el mismo en ser impreso; y que la impresora tiene un tiempo máximo para procesar cada trabajo de 5 minutos.
#   Tener en cuenta que el trabajo que no se terminó de imprimir porque excedía su tiempo de proceso ingresa
#   nuevamente a la cola con el tiempo restante de impresión.
#   Se pide: a) Informar cantidad de trabajos que quedaron sin atender.
# b) Indicar el promedio de espera de los trabajos impresos.


import random
from ColaEncadena import cola


class Simulacion():
    def simular(self, duracion_simulacion):
        xcola = cola()
        tiempo_maximo_impresion = 5
        t_actual = 0
        tiempo_espera = 0
        cantidad_atendidos = 0
        cantidad_no_atendidos = 0
        espera_total = 0
        #Simulacion de cola
        while t_actual < duracion_simulacion:
            #Chequeamos si llego un nuevo trabajo
            xrandom = random.randint(1, 5)
            if xrandom == 1:
                tiempo_impresion = random.randint(1, 8)
                xcola.insertar(tiempo_impresion)
            #Chequemos si un trabjo ha sido impreso
            if tiempo_espera == 0 and not xcola.vacia():
                tarea_actual = tiempo_impresion
                if tarea_actual > tiempo_maximo_impresion:
                    tarea_actual -= tiempo_maximo_impresion
                    xcola.suprimir()
                    cantidad_no_atendidos += 1
                else:
                    cantidad_atendidos += 1
                    espera_total += t_actual
                    tiempo_espera = tarea_actual
            #Actualizamos tiempos

            if tiempo_espera > 0:
                tiempo_espera -= 1
            t_actual += 1
        print(f'Cantidad de trabajos atendidos: {cantidad_atendidos}')
        print(f'Cantidad de trabajos no atendidos: {cantidad_no_atendidos}')
        print(f'Promedio de espera: {espera_total/(cantidad_atendidos+cantidad_no_atendidos):.2f} minutos')   
            



if __name__ == '__main__':
    Cola = Simulacion()
    Cola.simular(int(60))
