#*****************************************************************************
#  miembro_cp.tests
#
# Descripcion : pruebas unitarias del conjunto de elementos que permiten trabajar
# miembro_cp que participan en  el CLEI
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

from django.utils import unittest
from miembro_cp.models import Miembro_CP , Experticia, Calificacion
from persona.models import Persona
from django.test.client import Client


#Pruebas de models y views de persona
class Test_Miembro_CP(unittest.TestCase):

  def setUp(self):
	  #creacion de un objeto del tipo miembro_cp
	  self.persona1 = Persona.objects.create(cedula = "2", nombre="jose", apellido= "roro", 
			  institucion_afiliada = "usb", email= "a@g.com", pais = "venezuela")
	  self.experticia = Experticia.objects.create(nombre = "Bases de datos")
	  self.mcp1 = Miembro_CP.objects.create(persona = self.persona1, experticia= self.experticia, cargo= {'RE'})
	  #creacion de un objeto cliente para simular la interaccion del usuario con el codigo a nivel view
	  self.client = Client()
	  
#prueba que los datos introducidos en persona sean los correctos
  def test_miembro_cp_creado(self):
	  
	  #self.assertEqual(self.mcp1.cedula, "2") , "Falla asignando la cedula de la persona"
	  #self.assertEqual(self.mcp1.nombre, "jose") , "Falla asignando el nombre"
	  #self.assertEqual(self.mcp1.apellido, "roro") ,"Falla asignando el apellido"
	  #self.assertEqual(self.mcp1.institucion_afiliada,"usb") ,"Falla asignando la institucion afiliad"""
	  #self.assertEqual(self.mcp1.email, "a@g.com"), "Falla asignando el email"
	  #self.assertEqual(self.mcp1.pais, "venezuela"), "Falla asignando pais"
	  #self.assertEqual(self.mcp1.experticia, {"Bases de datos"}) ,"Falla asignando el apellido"
	  #self.assertEqual(self.mcp1.cargo,"Regular") ,"Falla asignando la institucion afiliad"""
	  print self.mcp1
##prueba para probar que que el url de persona es redireccionado correctamente

  #def test_persona_participante(self):
	  #resp = self.client.get('/persona/')
	  #self.assertEqual(resp.status_code, 200)
	  ##print resp.context
	  #self.assertTrue('inscrito_lista' in resp.context)
	  #self.assertTrue('comite_lista' in resp.context)