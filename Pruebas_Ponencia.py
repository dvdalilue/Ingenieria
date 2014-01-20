#*****************************************************************************
# Clase : pruebas_ponencia.py
#
# Descripcion : Clase que implementa las pruebas unitarias para las ponencias
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
from lugar import Lugar
from Ponencia import Ponencia
from Persona import Ponente

class Test_Ponencia(unittest.TestCase):
  #Creacion del objeto Ponencia
  def setUp(self):
    #Creacion del expositor de la ponencia
    self.expositor = Ponente(20, "Pedro", "Perez", "UC", "pperez@uc.ve",
                             "Venezuela", 1071, 0, "http://hola2.com")
    #Creacion de articulo a presentar
    self.articulo = Articulo(1,"Titulo1",["Pedro Perez"], ["Palabra", "Clave"],
                             ["Bases de Datos"], "Texto", "Resumen")
    #Creacion de lugar de la ponencia
    self.lugar = Lugar("MYS-110","MYS",50)
    #Creacion de los topicos de la ponencia
    self.topico = ["Topico1","Topico2","Topico3"]
    #Creacion de la ponencia
    self.ponencia = Ponencia(self.expositor, self.articulo, self.lugar,
                             self.topico)
  
  def test_crear_Ponencia(self):
    self.assertEqual(self.ponencia.expositor, self.expositor), 
    "Falla asignando ponente"
    self.assertEqual(self.ponencia.articulo_a_presentar, self.articulo),
    "Falla asignando articulo"
    self.assertEqual(self.ponencia.ubicacion, self.lugar),
    "Falla asiganando lugar"
    self.assertEqual(self.ponencia.topico, self.topico),
    "Falla asigando topicos"

if __name__ == "__main__":
  unittest.main()
