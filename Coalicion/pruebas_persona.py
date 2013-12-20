#*****************************************************************************
# Clase : Probar_Clases.py
#
# Descripcion : Clase que implementa las pruebas unitarias
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
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
    self.persona = Persona(10, "Carlos", "Gomez", "UCAB", "cg@ucab.ve", "Venezuela")
    self.asistente = Asistente(20, "Andrea", "Alvarez", "USB", "aa@usb.ve", "Venezuela", 1071, 0, True, False, "ttp://hola1.com" )
    self.invitado = Invitado(30, "Marcos", "Perez", "UCV", "mp@ucv.ve", "Venezuela", "http://hola2.com" )
    self.miembro_cp = Miembro_Cp(40, "Leonardo", "Martinez", "USB", "lm@usb.ve", "Venezuela", "http://hola3.com" )

  def test_crear_Persona(self):
        self.assertEqual(self.persona.ci, 10)
	self.assertEqual(self.persona.nombre, "Carlos")
	self.assertEqual(self.persona.apellido, "Gomez")
	self.assertEqual(self.persona.institucion_afiliada, "UCAB")
	self.assertEqual(self.persona.email, "cg@ucab.ve")
	self.assertEqual(self.persona.pais, "Venezuela")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_persona']
    unittest.main()
