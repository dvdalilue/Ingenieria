#*****************************************************************************
# Clase : Persona
#
# Descripcion : Clase que implementa las Personas que participan en  el CLEI
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

class Persona(object):

    def __init__(self, ci, nombre, apellido, institucion_afiliada,
                  email, pais, url = None):
        
        """Constructor"""
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.institucion_afiliada = institucion_afiliada
        self.email = email
        self.pais = pais
        self.url = url

    def __str__(self):
        
        keys = self.__dict__.keys()
        keys = sorted(keys, key=str.lower)
        datos = "\n"
        for n in keys:
            datos += "\n%s: %s"%(n,str(self.__dict__[n]))
        datos += "\n"
        return datos


#*****************************************************************************
# Clase : Asistente
#
# Descripcion : Clase que hereda de Persona e implementa las Personas
#           inscritas que participan en  el CLEI
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

class Asistente(Persona):
    
    def __init__(self, ci, nombre, apellido, institucion_afiliada, email, 
                 pais,cod_postal, telefono, ponente, autor, url= None):
        
        """Constructor"""
        super(Asistente, self).__init__(ci, nombre, apellido, 
              institucion_afiliada, email, pais, url)
        
        self.ponente = False
        self.autor = False
        self.cod_postal = cod_postal
        self.url = url
        self.telefono = telefono
        
#*****************************************************************************
# Clase : Miembro_Cp
#
# Descripcion : Clase que hereda de Persona e implementa las Personas
#           que forman parte del Comite de programa  el CLEI
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
class MiembroCp(Persona):
    
    def __init__(self, ci, nombre, apellido, institucion_afiliada, email, 
                 pais, experticia = None, url = None):
        
        """Constructor"""
        super(MiembroCp, self).__init__(ci, nombre, apellido, 
              institucion_afiliada, email, pais, url)
        
        self.presidente = False
        self.experticia = experticia
    
    def set_presidente(self):
        """  Metodo : Set_Presidente
        Parametros : self
        boolean val
        Descripcion: Cambia el cargo de un miembro """
        self.presidente = True
    
#if __name__=="__main__":
    
    #p = Miembro_Cp(3,"Maria", "Andrade", "USB", "ma@usb.ve" ,"Venezuela")
    #p = Miembro_Cp(4,"Jose", "Camejo","USB", "jc@usb.ve","Venezuela ", ["op", "bd"])
    #p = Asistente(3,"Maria", "Andrade", "USB", "ma@usb.ve" ,
    #"Venezuela",True, False, 25, 555, "google.com")
    #print p
    
