#*****************************************************************************
# Clase : Probar_Clases.py
#
# Descripcion : Clase que implementa las pruebas unitarias
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
from Articulo import Articulo
from CLEI import *
from Persona import *
from Curriculum import Curriculum


#Pruebas del Modulo Persona.py

class Test_Persona(unittest.TestCase):
  #creacion de un objeto persona, Miembro_Cp , Asistente e Invitado
  def setUp(self):
    self.persona = Persona(10, "Carlos", "Gomez", "UCAB", "cg@ucab.ve", 
                           "Venezuela")
    self.persona1 = Persona(11, "Carlos", "Gomez", "UCAB", "cg@ucab.ve", 
                            "Venezuela")
    self.asistente = Asistente(20, "Andrea", "Alvarez", "USB", "aa@usb.ve",
                                "Venezuela", 1071, 0, True, False, 
                                "http://hola1.com" )
    self.asistente1 = Asistente(21, "Andrea", "Alvarez", "USB", "aa@usb.ve", 
                                "Venezuela", 1071, 0, True, False, 
                                "http://hola1.com" )
    self.cv = Curriculum("trabajo", "bases de datos", "operador ldc", 
                         "recreador")
    self.invitado = Invitado(30, "Marcos", "Perez", "UCV", "mp@ucv.ve", 
                             "Venezuela", self.cv )
    self.invitado1 = Invitado(31, "Marcos", "Perez", "UCV", "mp@ucv.ve",
                               "Venezuela", self.cv )
    self.miembro_cp = MiembroCp(40, "Leonardo", "Martinez","USB","lm@usb.ve",
                                 "Venezuela", ["bd", "so"] )
    self.miembro_cp1 = MiembroCp(41, "Leonardo", "Martinez","USB","lm@usb.ve",
                                  "Venezuela", ["bd", "so"] )

  def test_crear_Persona(self):
    
    self.assertEqual(self.persona.ci, 10) , "Falla asignando ci"
    self.assertEqual(self.persona.nombre, "Carlos") , "Falla asignando nombre"
    self.assertEqual(self.persona.apellido, "Gomez"),"Falla asignando apellido"
    self.assertEqual(self.persona.institucion_afiliada, "UCAB") , 
    "Falla asignando institucion afiliada"
    self.assertEqual(self.persona.email, "cg@ucab.ve"),"Falla asignando email"
    self.assertEqual(self.persona.pais, "Venezuela") , "Falla asignando pais"

  def test_is_equal(self):
    
    self.assertFalse(Persona.is_equal(self.persona, self.persona1)),  
    "Falla comparando si dos personas son distintas"
    self.assertTrue(Persona.is_equal(self.persona, self.persona)),  
    "Falla comparando si dos personas son iguales"
    self.assertFalse(Invitado.is_equal(self.invitado, self.invitado1)),  
    "Falla comparando si dos invitados son distintas"
    self.assertTrue(Invitado.is_equal(self.invitado, self.invitado)),  
    "Falla comparando si dos invitados son iguales"
    self.assertFalse(Asistente.is_equal(self.asistente, self.asistente1)),  
    "Falla comparando si dos asistentes son distintas"
    self.assertTrue(Asistente.is_equal(self.asistente, self.asistente)),  
    "Falla comparando si dos asistentes son iguales"
    self.assertFalse(MiembroCp.is_equal(self.miembro_cp, self.miembro_cp1)),  
    "Falla comparando si dos miembros del cp son distintas"
    self.assertTrue(MiembroCp.is_equal(self.miembro_cp, self.miembro_cp)),  
    "Falla comparando si dos miembros del cp son iguales"
   
  
  def test_crear_Asistente(self):
    
    self.assertEqual(self.asistente.ci, 20) , "Falla asignando ci"
    self.assertEqual(self.asistente.nombre, "Andrea"),"Falla asignando nombre"
    self.assertEqual(self.asistente.apellido, "Alvarez"), 
    "Falla asignando apellido"
    self.assertEqual(self.asistente.institucion_afiliada, "USB"), 
    "Falla asignando institucion afiliada"
    self.assertEqual(self.asistente.email, "aa@usb.ve"), 
    "Falla asignando email"
    self.assertEqual(self.asistente.pais, "Venezuela"), "Falla asignando pais" 
    self.assertEqual(self.asistente.cod_postal, 1071), 
    "Falla asignando codigo postal"
    self.assertEqual(self.asistente.telefono, 0) , "Falla asignando telefono"
    self.assertTrue(self.asistente.ponente) , "Falla asignando ponente true"
    self.assertFalse(self.asistente.autor) , "Falla asignando autor false"
    self.assertEqual(self.asistente.url, "http://hola1.com") , 
    "Falla asignando url"
    
  def test_crear_Invitado(self):
    
    self.assertEqual(self.invitado.ci, 30) , "Falla asignando ci"
    self.assertEqual(self.invitado.nombre, "Marcos") ,"Falla asignando nombre"
    self.assertEqual(self.invitado.apellido, "Perez") ,
    "Falla asignando apellido"
    self.assertEqual(self.invitado.institucion_afiliada, "UCV"), 
    "Falla asignando institucion afiliada"
    self.assertEqual(self.invitado.email, "mp@ucv.ve"),"Falla asignando email"
    self.assertEqual(self.invitado.pais, "Venezuela") , "Falla asignando pais"
    self.assertEqual(self.invitado.curriculum_vitae, self.cv) , 
    "Falla asignando cv"
    
    
  def test_crear_Miembro_Cp(self):
     
    self.assertEqual(self.miembro_cp.ci, 40) , "Falla asignando ci"
    self.assertEqual(self.miembro_cp.nombre, "Leonardo"), 
    "Falla asignando nombre"
    self.assertEqual(self.miembro_cp.apellido, "Martinez"), 
    "Falla asignando apellido"
    self.assertEqual(self.miembro_cp.institucion_afiliada, "USB"), 
    "Falla asignando institucion afiliada"
    self.assertEqual(self.miembro_cp.email, "lm@usb.ve"), 
    "Falla asignando email"
    self.assertEqual(self.miembro_cp.pais, "Venezuela"), 
    "Falla asignando pais"
    self.assertEqual(self.miembro_cp.experticia, ["bd", "so"] ), 
    "Falla verificando experticia"
    self.assertFalse(self.miembro_cp.es_presidente), 
    "Falla asignando presidencia"
  
  def test_probar_set_presidente_de_mcp(self):
    self.assertFalse(self.miembro_cp.es_presidente) , 
    "Falla asignando presidencia"
    self.miembro_cp.set_presidente()
    self.assertTrue(self.miembro_cp.es_presidente),
    "Falla cambiando presidencia"

  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_persona']
    unittest.main()
