
class Nodo:
    __clave = None
    __sigIzq = None
    __sigDer = None

    def __init__(self, clave):
        self.__clave = clave
        self.__sigIzq = None
        self.__sigDer = None
    
    def setCalve(self, clave):
        self.__clave = clave

    def setSigIzq(self, izq):
        self.__sigIzq = izq
        
    def setSigDer(self, der):
        self.__sigDer = der

    def getClave(self):
        return self.__clave
    
    def setClave(self, clave):
        self.__clave = clave

    def getSigIzq(self):
        return self.__sigIzq

    def getSigDer(self):
        return self.__sigDer