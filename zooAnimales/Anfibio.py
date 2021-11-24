from zooAnimales.Animal import Animal

class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre, edad, habitat, genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas+=1
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)
    
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        cls.salamandras+=1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
    
    @classmethod
    def getListado(cls):
        return cls._listado

    def getColorPiel(self):
        return self._colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    
    @classmethod
    def setListado(cls,nuevo):
        cls._listado=nuevo
    
    def setColorPiel(self,nuevo):
        self._colorPiel=nuevo
    
    def setVenenoso(self,nuevo):
        self._venenoso=nuevo
    
    def isVenenoso(self):
        return self._venenoso