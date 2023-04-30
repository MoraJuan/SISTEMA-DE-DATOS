class Nodo:
  def __init__(self, valor, esperando = 0): #Cargamos valores a la cola
    self.__item = valor
    self.__esperando = esperando
    self.__sig = None


  def obteneritem(self):
    return self.__item


  def cargaritem(self, valor):
    self.__item = valor


  def cargarsig(self, siguiente):
    self.__sig = siguiente


  def obtenersig(self):
    return self.__sig
  
  def cargarEsperando(self, Xesperando):
    self.__esperando = Xesperando
    
  def ObtenerEsperando(self):
      return self.__esperando      

    
class cola:
  

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__tamaño = 0

    
    def insertar(self, valor):
        nodo = Nodo(valor)
        if self.__primero == None:
            self.__primero = nodo
            self.__cola = nodo
            
        else:
            self.__cola.cargarsig(nodo)
            self.__cola = nodo
            
        
        
        self.__tamaño +=1

    def suprimir(self):
        if self.vacia():
            return 'Ya no quedan elementos'
        else:
            nodo = self.__primero
            self.__primero = nodo.obtenersig()
            self.__tamaño -=1
            return nodo

    def vacia(self):
        return self.__primero == None and self.__ultimo == None

    def recuperapr(self):
        primero = self.__primero
        return primero.obteneritem() 

    def recorrer(self, aux):
        if aux is not None:
            print(aux.obteneritem())
            self.recorrer(aux.obtenersig())



    