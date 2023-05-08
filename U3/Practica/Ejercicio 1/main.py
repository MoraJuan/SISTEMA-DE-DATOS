import os
from ArbolBinario import ArbolBinario

if __name__ == '__main__':
    
    Arbol = ArbolBinario()                
    Arbol.insertar(60, Arbol.getRaiz())
    Arbol.insertar(21, Arbol.getRaiz())
    Arbol.insertar(11, Arbol.getRaiz())
    Arbol.insertar(7, Arbol.getRaiz())
    Arbol.insertar(25, Arbol.getRaiz())
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
    #Arbol.inorden(Arbol.getRaiz())
    #Arbol.Preorden(Arbol.getRaiz())
    Arbol.Postorden(Arbol.getRaiz())
    
    Arbol.Hijo(76, Arbol.getRaiz(), 90)
    c=Arbol.camino(60, Arbol.getRaiz() ,76)
    print(c)