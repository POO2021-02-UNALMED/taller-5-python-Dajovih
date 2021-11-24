class Animal:
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales+=1
    
    def movimiento(self):
        return "desplazarse"

    def totalPorTipo(self):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        cadena="Mamiferos: "+str(Mamifero.cantidadMamiferos())+"\nAves: "+str(Ave.cantidadAves())+"\nReptiles: "+str(Reptil.cantidadReptiles())+"\nPeces: "+str(Pez.cantidadPeces())+"\nAnfibios: "+str(Anfibio.cantidadAnfibios())
        return cadena

    def toString(self):
        if self._zona==None:
            cadena="Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero
            return cadena
        else:
            cadena="Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero+", la zona en la que me ubico es "+self._zona+", en el "+self._zona.getZoo().getNombre()
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    
    def getZona(self):
        return self._zona
    
    @classmethod
    def setTotalAnimales(cls,nuevo):
        cls._totalAnimales=nuevo
    
    def setNombre(self,nuevo):
        self._nombre=nuevo
    
    def setEdad(self,nuevo):
        self._edad=nuevo

    def setHabitat(self,nuevo):
        self._habitat=nuevo

    def selfGenero(self,nuevo):
        self._genero=nuevo
    
    def setZona(self,nuevo):
        self._zona=nuevo


