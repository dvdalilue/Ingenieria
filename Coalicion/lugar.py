#!/usr/bin/python

class Lugar(object):
    def __init__(self, Nombre, Ubicacion, Capacidad_maxima):
       
       self.Nombre = Nombre
       self.Ubicacion = Ubicacion
       self.Capacidad_maxima = Capacidad_maxima
       
    def Equals(self, Lugar):
        if self.Nombre == Lugar.Nombre:
	   print "Ambos Lugares tIenen el mismo Nombre"
	   if self.Ubicacion == Lugar.Ubicacion:
	    return True
	else:
	    return False
            
    def __str__(self):
        keys = self.__dict__.keys()
        datos = ""
        for n in keys:
            datos += "\n%s: %s"%(n,str(self.__dict__[n]))
        datos += "\n"
        return datos

 if __name__=="__main__":
    
    l = Lugar("MYS", "Mys-019", 300)
    print l