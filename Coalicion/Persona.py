#*****************************************************************************
# Clase : Persona
#
# Descripcion : Clase que implementa las Personas que participan en  el CLEI
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Liniayo  #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************

class Persona(object):

    def __init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Url = None):
        """Constructor"""
        self.CI = CI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Institucion_Afiliada = Institucion_Afiliada
        self.Email = Email
        self.Pais = Pais
        self.Url = Url

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
#           Veronica Liniayo  #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************        

class Asistente(Persona):
    
    def __init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais,Cod_Postal, Telefono, Ponente = False, Autor = False, Url= None):
        """Constructor"""
        super(Asistente, self).__init__(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Url)
        self.Ponente = Ponente
        self.Autor = Autor
        self.Cod_Postal = Cod_Postal
        self.Url = Url
        self.Telefono = Telefono
        
#*****************************************************************************
# Clase : Miembro_Cp
#
# Descripcion : Clase que hereda de Persona e implementa las Personas
#           que forman parte del Comite de programa  el CLEI
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Liniayo  #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************    
class Miembro_Cp(Persona):
    
    def __init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experticia = None, Url = None):
        """Constructor"""
        super(Miembro_Cp, self).__init__(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Url)
        self.Presidente = False
        self.Experticia = Experticia
    
    def set_Presidente(self):
        """  Metodo : Set_Presidente
        Parametros : self
        boolean val
        Descripcion: Cambia el cargo de una miebro """
        self.Presidente = True
    
#if __name__=="__main__":
    
    #p = Miembro_Cp(3,"Maria", "Andrade", "USB", "ma@usb.ve" ,"Venezuela")
    #p = Miembro_Cp(4,"Jose", "Camejo","USB", "jc@usb.ve","Venezuela ", ["op", "bd"])
    #p = Asistente(3,"Maria", "Andrade", "USB", "ma@usb.ve" ,"Venezuela",True, False, 25, 555, "google.com")
    #print p
    
