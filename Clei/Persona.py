#*****************************************************************************
# Clase : Persona.py
#
# Descripcion : Clase que implementa las Personas que participan en  el CLEI
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
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
        datos = ""
        for n in keys:
            datos += "\n%s: %s"%(n,self.__dict__[n])
        datos += "\n"
        return datos


#*****************************************************************************
# Clase : Inscrito
#
# Descripcion : Clase que hereda de Persona e implementa las Personas
#           inscritas que participan en  el CLEI
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************        

class Inscrito(Persona):
    
    Asistente= False
    Ponente= False
    Autor= False
    Cod_Postal= 0
    Url= ' '
    Telefono= ' '
    
    def __init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Asistente, Ponente, Autor, Cod_Postal, Telefono, Url= None):
        """Constructor"""
        Persona.__init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais)
        self.Asistente = Asistente
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
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************    
class Miembro_Cp(Persona):
    
    Cargo= ' '
    Experiencia = []
    
    def __init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experiencia = None):
        """Constructor"""
        Persona.__init__(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais)
        self.Cargo = "Miembro regular"
        self.Experiencia = Experiencia
    
    def set_Cargo(self, cargo):
        """  Metodo : Set_Presidente
        Parametros : self
              boolean val
        Descripcion: Cambia el cargo de una miebro """
        self.Cargo = cargo
        
    def to_String(self):
        """Metodo : to_String
      Parametros : self
      Descripcion; imprime en un string los datos de un Miembro_Cp"""
        #datos_mcp = Persona.to_String(self)
        datos_mcp += "\nCargo: " + str(self.Cargo)
        datos_mcp += "\nExperiencia: " + str(self.Experiencia)
        
        return datos_mcp
    

if __name__=="__main__":
    
    #m1 = Miembro_Cp(3,"Maria", "Andrade", "USB", "ma@usb.ve" ,"Venezuela")
    #m2 = Miembro_Cp(4,"Jose", "Camejo","USB", "jc@usb.ve","Venezuela ", ["op", "bd"])
    p = Inscrito(3,"Maria", "Andrade", "USB", "ma@usb.ve" ,"Venezuela",False, True, False, 25, 555, "google.com")
    print p
    #print m2.to_String()
    
