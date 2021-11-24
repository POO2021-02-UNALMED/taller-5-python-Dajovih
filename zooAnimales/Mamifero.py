from Animal import Animal

class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0
    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos+=1
        return Mamifero(nombre,edad,"pradera",genero,True,4)
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones+=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    @classmethod
    def getListado(cls):
        return cls._listado

    def getPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas
    
    @classmethod
    def setListado(cls,nuevo):
        cls._listado=nuevo
    
    def setPelaje(self,nuevo):
        self._pelaje=nuevo
    
    def setPatas(self,nuevo):
        self._patas=nuevo
    
    def isPelaje(self):
        return self._pelaje