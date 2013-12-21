#*****************************************************************************
# Clase : Lugar
#
# Descripcion : Clase que implementa los lugares donde puede realizarse un
#                evento en el CLEI
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#***************************************************************************** 

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

