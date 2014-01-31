#*****************************************************************************
#  persona.tests
#
# Descripcion : pruebas unitarias del conjunto de elementos que permiten trabajar con las personas que participan en  el CLEI
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
from persona.models import Persona
from django.test.client import Client


#Pruebas de models y views de persona
class Test_Persona(unittest.TestCase):

  #fixtures = ['persona_views_testdata.json']


  def setUp(self):
	  #creacion de un objeto del tipo persona
	  self.persona1 = Persona.objects.create(cedula = "2", nombre="jose", apellido= "roro", 
			  institucion_afiliada = "usb", email= "a@g.com", pais = "venezuela")
	  #creacion de un objeto cliente para simular la interaccion del usuario con el codigo a nivel view
	  self.client = Client()
	  
#prueba que los datos introducidos en persona sean los correctos
  def test_persona_creada(self):
	  
	  self.assertEqual(self.persona1.cedula, "2") , "Falla asignando la cedula de la persona"
	  self.assertEqual(self.persona1.nombre, "jose") , "Falla asignando el nombre"
	  self.assertEqual(self.persona1.apellido, "roro") ,"Falla asignando el apellido"
	  self.assertEqual(self.persona1.institucion_afiliada,"usb") ,"Falla asignando la institucion afiliad"""
	  self.assertEqual(self.persona1.email, "a@g.com"), "Falla asignando el email"
	  self.assertEqual(self.persona1.pais, "venezuela"), "Falla asignando pais"

#prueba para probar que que el url de persona es redireccionado correctamente

  def test_persona_participante(self):
	  resp = self.client.get('/persona/')
	  self.assertEqual(resp.status_code, 200)
	  #print resp.context
	  self.assertTrue('inscrito_lista' in resp.context)
	  self.assertTrue('comite_lista' in resp.context)
      #    self.assertEqual([persona.pk for persona in resp.context['inscrito_lista']], [1])

