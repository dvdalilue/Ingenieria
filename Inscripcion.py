#*****************************************************************************
# Clase : Inscripcion
#
# Descripcion : Clase implementa la inscripcion de un asistente al CLEI
#
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
import datetime

class Inscripcion(object):
    
    
    def __init__(self, asistente, fecha_inscripcion , monto):
        
        """Constructor"""
        self.asistente = asistente
        self.fecha_inscripcion = fecha_inscripcion
        self. monto = monto
        
    def __str__(self):
        
        keys = self.__dict__.keys()
        keys = sorted(keys, key=str.lower)
        datos = "\n"
        for n in keys:
            datos += "\n%s: %s"%(n,str(self.__dict__[n]))
        datos += "\n"
        return datos
        