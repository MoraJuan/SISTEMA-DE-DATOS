def factorial(n):
    stack = []
    result = 1
    stack.append(n)
    while len(stack) > 0:
        x = stack.pop()
        if x > 0:
            stack.append(x - 1)
            result = result * x
        else:
            return result
num = input("Ingrese numero: ")        
print(factorial(int(num))) # Output: 120

# En esta función se utiliza una pila (stack) para simular el comportamiento de la recursión. Primero, agregamos el número a la pila. Luego, mientras la pila contenga elementos, sacamos uno y seguimos las siguientes reglas:
# - Si el elemento sacado es mayor que cero, lo "descomponemos" en un número menor (x-1) y multiplicamos la actual "solución" (result) por el elemento sacado (x).
# - Si el elemento sacado es cero, se retorna el valor actual de la solución.