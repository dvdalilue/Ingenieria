#!/usr/bin/python
import datetime
import lugar
import Persona

#*****************************************************************************
# Clase : Evento
#
# Descripcion : Clase que implementa cada evento en  el CLEI
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

class Evento(object):
    
    def __init__(self, nombre, fecha_ini, fecha_fin, hora_ini, hora_fin, lugar):

        # hacer esto antes del constructor
        # dia_ini, mes_ini, anio_ini, hora_ini, min_ini, dia_fin, mes_fin, 
        # anio_fin, hora_fin, min_fin
        # self.fecha_fin = datetime.date(anio_fin,mes_fin,dia_fin)
        # self.hora_ini = datetime.time(hora_ini,min_ini,0)
        
        self.nombre = nombre
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.hora_ini = hora_ini
        self.hora_fin = hora_fin
        self.lugar = lugar
        
    def __str__(self):
        
        keys = self.__dict__.keys()
        keys = sorted(keys, key=str.lower)
        datos = ""
        for n in keys:
            datos += "\n%s: %s"%(n,str(self.__dict__[n]))
        datos += "\n"
        return datos

#*****************************************************************************
# Clase : Sesion_de_Ponencias
#
# Descripcion : Clase que hereda de Evento e implementa las sesiones de 
#                ponencias que se daran en  el CLEI
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

class Sesion_de_ponencias(Evento):

    def __init__(self, nombre, fecha_ini, fecha_fin, hora_ini, hora_fin, 
                 lugar, ponencia1, ponencia2, ponencia3 = None, ponencia4 = None):

        super(Sesion_de_ponencias, self).__init__(nombre, fecha_ini, fecha_fin,
                                                   hora_ini, hora_fin, lugar)
        self.ponencias = []
        
        self.ponencias.append(ponencia1)
        self.ponencias.append(ponencia2)
        if ponencia3 != None:
            self.ponencias.append(ponencia3)
            if ponencia4 != None:
                self.ponencias.append(ponencia4)

    def agregar_ponencia(self, ponencia):

        if len(self.ponencias) < 4:
            self.ponencias.append(ponencia)
            return True
        return False

#*****************************************************************************
# Clase : Charla_invitada
#
# Descripcion : Clase que hereda de Evento e implementa las charlas invitadas
#           que se daran en  el CLEI
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

class Charla_invitada(Evento):

    def __init__(self, nombre, fecha_ini, fecha_fin, hora_ini, hora_fin, lugar, 
                 moderador, charlista, resumen, palabras_claves, topico):

        if not(topico in moderador.Experticia):
            raise Exception

        super(Charla_invitada, self).__init__(nombre, fecha_ini, fecha_fin, 
                                              hora_ini, hora_fin, lugar)

        self.moderador = moderador
        self.charlista = charlista
        self.resumen = resumen
        self.palabras_claves = palabras_claves
        self.topico = topico

        
#if __name__=="__main__":
    
#    fecha_ini1 = datetime.date(2013,12,19)
 #   fecha_fin1 = datetime.date(2013,12,20)
  #  hora_ini1 = datetime.time(8,0,0)
  #  hora_fin1 = datetime.time(9,0,0)
  #  moderador1 = Persona.Miembro_Cp(4,"Jose", "Camejo","USB", "jc@usb.ve",
  #"Venezuela ", ["op", "bd"])
    
  #  try:
  #      p = Charla_invitada("Charlita",fecha_ini1, fecha_fin1, hora_ini1, hora_fin1,
         #"Mys",moderador1, "Marlene", "resumen", "Clave", "op")
  #      print p
  #  except:
   #     print '\nEl moderador es bruto D:\n'

        
