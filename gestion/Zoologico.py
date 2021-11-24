class Zoologico():
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]
    
    def agregarzonas(self,Zona):
        Zona.setZoo(self)
        self._zonas.append(Zona)
    
    def cantidadTotalAnimales(self):
        pass

    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zonas
    
    def setNombre(self,nuevo):
        self._nombre=nuevo
    
    def setUbicacion(self,nuevo):
        self._ubicacion=nuevo
    
    def setZonas(self,nuevo):
        self._zonas=nuevo

