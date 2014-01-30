#*****************************************************************************
# Clase : Curriculum
#
# Descripcion : Clase implementa el curriculum vitae de un invitado del CLEI
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

class Curriculum(object):
    
    def __init__(self, trabajos_previos, experticia, experticia_adicional, informacion_extra):
        """Constructor"""
        
	      self.trabajos_previos = trabajos_previos
        self.experticia = experticia
        self.experticia_adicional = experticia_adicional
        self.informacion_extra = informacion_extra
        
    def __str__(self):
        """to_String que imprime los atributos de la clase con sus valores"""

        keys = self.__dict__.keys()
        keys = sorted(keys, key=str.lower)
        datos = "\n"
        for n in keys:
            datos += "\n%s: %s"%(n,str(self.__dict__[n]))
        datos += "\n"
        return datos
        
#if __name__=="__main__":
    
    #c = Curriculum("trabajo", "bases de datos", "operador ldc", "recreador")
    #print c
    
