#!/usr/bin/python

class Lugar(object):
    def __init__(self, nombre, ubicacion, capacidad_maxima):
       
       self.nombre = nombre
       self.ubicacion = ubicacion
       self.capacidad_maxima = capacidad_maxima
       
    def equals(self, Lugar):
        if self.nombre == Lugar.nombre:
	   print "Ambos Lugares tienen el mismo Nombre"
	   if self.ubicacion == Lugar.ubicacion:
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

if __name__=='__main__':
    
    l = Lugar("MYS", "Mys-019", 300)
    print l