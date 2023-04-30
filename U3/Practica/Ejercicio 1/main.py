import os
from ArbolBinario import ArbolBinario

if __name__ == '__main__':
    os.system()
    Arbol = ArbolBinario()                
    Arbol.insertar(60, Arbol.getRaiz())
    Arbol.insertar(21, Arbol.getRaiz())
    Arbol.insertar(70, Arbol.getRaiz())
    Arbol.insertar(90, Arbol.getRaiz())
    Arbol.insertar(112, Arbol.getRaiz())   
    Arbol.insertar(76, Arbol.getRaiz()) 
    print("Raíz del árbol:", Arbol.getRaiz().getClave()) 
    print("Árbol completo:")
    Arbol.inorden(Arbol.getRaiz())
        
    c=Arbol.nivel(70, Arbol.getRaiz())
    print("\nNivel:",c)
    Arbol.Hoja(112, Arbol.getRaiz())
    if Arbol.Hoja(76, Arbol.getRaiz()) is True:
        print('Es hoja')
    else:
        print('No es hoja')
    Arbol.inorden(Arbol.getRaiz())
    Arbol.Hijo(76, Arbol.getRaiz(), 90)
    Arbol.camino(76, Arbol.getRaiz(), 90)