class Zona:
    def __init__(self,nombre,zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
    
    def agregarAnimales(self,Animal):
        Animal.setZona(self)
        self._animales.append(Animal)
    
    def cantidadAnimales(self):
        len(self._animales)

    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    
    def getAnimales(self):
        return self._animales
    
    def setNombre(self,nuevo):
        self._nombre=nuevo
    
    def setZoo(self,nuevo):
        self._zoo=nuevo
    
    def setAnimales(self,nuevo):
        self._animales=nuevo

