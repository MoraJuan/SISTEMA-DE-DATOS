class Nodo:
    def __init__(self, valor, fila, columna, siguiente=None):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.siguiente = siguiente

class Fila:
    def __init__(self, numero):
        self.numero = numero
        self.cabeza = Nodo(None, self.numero, -1)
        self.siguiente = None

    def insertar(self, valor, columna):
        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.columna < columna:
            actual = actual.siguiente
        if actual.siguiente is not None and actual.siguiente.columna == columna:
            actual.siguiente.valor = valor
        else:
            nuevo = Nodo(valor, self.numero, columna, actual.siguiente)
            actual.siguiente = nuevo

    def sumar(self, otra_fila):
        resultado = Fila(self.numero)
        actual1 = self.cabeza.siguiente
        actual2 = otra_fila.cabeza.siguiente
        while actual1 is not None and actual2 is not None:
            if actual1.columna == actual2.columna:
                suma = actual1.valor + actual2.valor
                resultado.insertar(suma, actual1.columna)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
            elif actual1.columna < actual2.columna:
                resultado.insertar(actual1.valor, actual1.columna)
                actual1 = actual1.siguiente
            else:
                resultado.insertar(actual2.valor, actual2.columna)
                actual2 = actual2.siguiente
        while actual1 is not None:
            resultado.insertar(actual1.valor, actual1.columna)
            actual1 = actual1.siguiente
        while actual2 is not None:
            resultado.insertar(actual2.valor, actual2.columna)
            actual2 = actual2.siguiente
        return resultado

class MatrizRala:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.cabeza = Fila(-1)

    def insertar(self, valor, fila, columna):
        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.numero < fila:
            actual = actual.siguiente
        if actual.siguiente is not None and actual.siguiente.numero == fila:
            actual.siguiente.insertar(valor, columna)
        else:
            nueva_fila = Fila(fila)
            nueva_fila.insertar(valor, columna)
            nueva_fila.siguiente = actual.siguiente
            actual.siguiente = nueva_fila

    def sumar(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            raise ValueError("Las matrices deben tener la misma dimensión para sumarse")
        resultado = MatrizRala(self.filas, self.columnas)
        actual1 = self.cabeza.siguiente
        actual2 = otra_matriz.cabeza.siguiente
        while actual1 is not None and actual2 is not None:
            if actual1.numero == actual2.numero:
                nueva_fila = actual1.sumar(actual2)
                resultado.cabeza.insertar(nueva_fila, actual1.numero)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
            elif actual1.numero < actual2.numero:
                resultado.cabeza.insertar(actual1, actual1.numero)
                actual1 = actual1.siguiente
            else:
                resultado.cabeza.insertar(actual2, actual2.numero)
                actual2 = actual2.siguiente
        while actual1 is not None:
            resultado.cabeza.insertar(actual1, actual1.numero)
            actual1 = actual1.siguiente
        while actual2 is not None:
            resultado.cabeza.insertar(actual2, actual2.numero)
            actual2 = actual2.siguiente
        return resultado

if __name__ == '__main__':
    matriz = MatrizRala(4, 5)

    # Agregamos valores
    matriz.insertar(3, 0, 1)
    matriz.insertar(4, 0, 3)
    matriz.insertar(2, 1, 2)
    matriz.insertar(1, 1, 4)
    matriz.insertar(5, 2, 0)
    matriz.insertar(6, 2, 1)
    matriz.insertar(7, 2, 2)
    matriz.insertar(8, 3, 3)

    otra_matriz = MatrizRala(4, 5)

    # Agregamos valores
    otra_matriz.insertar(1, 0, 1)
    otra_matriz.insertar(2, 1, 2)
    otra_matriz.insertar(4, 1, 4)
    otra_matriz.insertar(5, 2, 0)
    otra_matriz.insertar(3, 2, 1)
    otra_matriz.insertar(1, 3, 3)

    # Sumamos las dos matrices
    resultado = matriz.sumar(otra_matriz)

    # Imprimimos la matriz resultante
    for i in range(resultado.filas):
        print(f"Fila {actual.cabeza.siguiente.valor}: ", end="")
        actual = resultado.cabeza.siguiente
        while actual is not None and actual.numero <= i:
            if actual.numero == i:
                for j in range(resultado.columnas):
                    if actual.cabeza.siguiente is not None and actual.cabeza.siguiente.columna == j:
                        print(actual.cabeza.siguiente.valor, end="\t")
                        actual.cabeza = actual.cabeza.siguiente
                    else:
                        print(0, end="\t")
                actual = actual.siguiente  # Actualizamos el valor de actual.numero
            else:
                for j in range(resultado.columnas):
                    print(0, end="\t")
            actual = actual.siguiente
        print()