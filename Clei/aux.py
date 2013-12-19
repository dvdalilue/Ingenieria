  def __str__(self):
        """ Metodo : to_String
        Parametros : self
        Descripcion; imprime en un string los datos de una Persona Inscrita"""        
        datos_persona = ""
        datos_persona += "\nCI: " + str(self.CI)
        datos_persona += "\nNombre: " + str(self.Nombre)
        datos_persona += "\nApellido: " + str(self.Apellido)
        datos_persona += "\nInstitucion_Afiliada: " + str(self.Institucion_Afiliada)
        datos_persona += "\nEmail: " + str(self.Email)
        datos_persona += "\nPais: " +  str(self.Pais)
        if  self.Url != None:
            datos_persona += "\nUrl:" + str(self.Url)
        datos_persona += "\nAsistente: " + str(self.Asistente)
        datos_persona += "\nPonente: " + str(self.Ponente)
        datos_persona += "\nAutor: " + str(self.Autor)
        datos_persona += "\nCod_Postal: " + str(self.Cod_Postal)
        datos_persona += "\nTelefono: " + str(self.Telefono) + "\n"
          
        return datos_persona    

    def __str__(self):
        """ Metodo : to_String
        Parametros : self
        Descripcion: imprime en un string los datos de una Persona"""
        datos_persona = ""
        datos_persona += "\nCI: " + str(self.CI)
        datos_persona += "\nNombre: " + str(self.Nombre)
        datos_persona += "\nApellido: " + str(self.Apellido)
        datos_persona += "\nInstitucion_Afiliada: " + str(self.Institucion_Afiliada)
        datos_persona += "\nEmail: " + str(self.Email)
        datos_persona += "\nPais: " +  str(self.Pais)
        if  self.Url != None:
            datos_persona += "\nUrl:" + str(self.Url)
        
        return datos_persona  
