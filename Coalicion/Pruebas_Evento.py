#*****************************************************************************
# Clase : pruebas_evento.py
#
# Descripcion : Clase que implementa las pruebas unitarias de la clase Evento
#
# Autores : David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1 , 3, 4
# Seccion : 1
#
#*****************************************************************************

import unittest
from evento import *
from lugar import Lugar


#Pruebas del modulo evento.py

class Test_Evento(unittest.TestCase): 
    #Creacion de objetos lugar, Evento, Sesion de Ponencias, Charla Invitada
    def setUp(self):
        self.fecha_ini1 = datetime.date(2013,12,19)
        self.fecha_fin1 = datetime.date(2013,12,20)
        self.hora_ini1 = datetime.time(8,0,0)
        self.hora_fin1 = datetime.time(9,0,0)
        self.lugar1 = Lugar("Mys-013","MYS",50)
        self.moderador1 = Persona.MiembroCp(4,"Jose", "Camejo","USB", "jc@usb.ve",
                                             "Venezuela ", ["op", "bd"])
        self.evento = Evento("Evento1",self.fecha_ini1,self.fecha_fin1,
                             self.hora_ini1,self.hora_fin1,self.lugar1)
        self.ses_de_pon1 = SesionDePonencias("SesionDePonencia1",self.fecha_ini1,
                                            self.fecha_fin1, self.hora_ini1,
                                            self.hora_fin1,self.lugar1,
                                            "ponencia1","ponencia2")
        self.charla = CharlaInvitada("Charlita",self.fecha_ini1, self.fecha_fin1, 
                                      self.hora_ini1, self.hora_fin1,self.lugar1,
                                      self.moderador1, "Marlene", "resumen", 
                                      "Clave", "bd")
        
    def test_crearEvento(self):
        
        self.assertEqual(self.evento.nombre,"Evento1"), "Falla asignando nombre"
        self.assertEqual(self.evento.fecha_ini,self.fecha_ini1), 
        "Falla asignando fecha inicio"    
        self.assertEqual(self.evento.fecha_fin,self.fecha_fin1), 
        "Falla asignando fecha fin"
        self.assertEqual(self.evento.hora_ini,self.hora_ini1), 
        "Falla asignando hora inicio" 
        self.assertEqual(self.evento.hora_fin,self.hora_fin1), 
        "Falla asignando hora fin"
        self.assertEqual(self.evento.lugar,self.lugar1), 
        "Falla asignando lugar"  
       
    def test_crearSesionDePonencia(self):
        
        self.assertEqual(self.ses_de_pon1.nombre,"SesionDePonencia1"),
        "Falla asignando nombre"
        self.assertEqual(self.ses_de_pon1.fecha_ini,self.fecha_ini1), 
        "Falla asignando fecha inicio"    
        self.assertEqual(self.ses_de_pon1.fecha_fin,self.fecha_fin1), 
        "Falla asignando fecha fin"
        self.assertEqual(self.ses_de_pon1.hora_ini,self.hora_ini1), 
        "Falla asignando hora inicio" 
        self.assertEqual(self.ses_de_pon1.hora_fin,self.hora_fin1), 
        "Falla asignando hora fin"
        self.assertEqual(self.ses_de_pon1.lugar,self.lugar1), 
        "Falla asignando lugar"    

    def test_crearCharlaInvitada(self):
        
        self.assertEqual(self.charla.nombre,"Charlita"),
        "Falla asignando nombre"
        self.assertEqual(self.charla.fecha_ini,self.fecha_ini1), 
        "Falla asignando fecha inicio"    
        self.assertEqual(self.charla.fecha_fin,self.fecha_fin1), 
        "Falla asignando fecha fin"
        self.assertEqual(self.charla.hora_ini,self.hora_ini1), 
        "Falla asignando hora inicio" 
        self.assertEqual(self.charla.hora_fin,self.hora_fin1), 
        "Falla asignando hora fin"
        self.assertEqual(self.charla.lugar,self.lugar1), 
        "Falla asignando lugar"     
        self.assertEqual(self.charla.moderador,self.moderador1), 
        "Falla asignando moderador"
        self.assertEqual(self.charla.charlista,"Marlene"), 
        "Falla asignando charlista"
        self.assertEqual(self.charla.resumen,"resumen"), 
        "Falla asignando resumen"
        self.assertEqual(self.charla.palabras_claves,"Clave"), 
        "Falla asignando palabras claves"
        self.assertEqual(self.charla.topico,"bd"), 
        "Falla asignando topico"
       
        
if __name__ == "__main__":
    unittest.main()
