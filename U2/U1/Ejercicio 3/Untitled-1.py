Here is the requested code, without the prints that display the results:

```python
import random

class Simulacion():
    def simular(self, duracion_simulacion):
        xcola = [] 
        
        tiempo_maximo_impresion = 5
        t_actual = 0
        tiempo_espera = 0
        cantidad_atendidos = 0
        cantidad_no_atendidos = 0
        espera_total = 0    
        
        while t_actual < duracion_simulacion:
            if random.randint(1, 5) == 1:
                tiempo_impresion = random.randint(1,10)
                xcola.append(tiempo_impresion)
                
            if tiempo_espera == 0 and len(xcola) > 0:
                tarea_actual = xcola.pop(0)
                
                if tarea_actual > tiempo_maximo_impresion:
                    tarea_actual -= tiempo_maximo_impresion
                    xcola.append(tarea_actual)  
                    cantidad_no_atendidos += 1
                else:
                    cantidad_atendidos += 1
                    espera_total += t_actual
                    tiempo_espera = tarea_actual             

            if tiempo_espera > 0:
                tiempo_espera -= 1
                
            t_actual += 1
        
        return cantidad_atendidos, cantidad_no_atendidos, espera_total          

if __name__ == '__main__':
    Cola = Simulacion()
    cantidad_atendidos, cantidad_no_atendidos, espera_total = Cola.simular(int(60))
```