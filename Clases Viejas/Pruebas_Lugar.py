#*****************************************************************************
# Clase : prueba_lugar.py
#
# Descripcion : Clase que implementa las pruebas unitarias de la clase lugar
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
from lugar import *

#Pruebas del modulo lugar.py

class Test_Lugar(unittest.TestCase):
    #creacion de unos objeto Lugar 
    def setUp(self):
        self.lugar1 = Lugar("Mys-110","MYS",50)
        self.lugar2 = Lugar("Mys-013", "MYS", 70)
        self.lugar3 = Lugar("Mys-110","MYS",50)
    
    def test_crear_lugar(self):
        self.assertEqual(self.lugar1.nombre, "Mys-110") , 
        "Falla asignando nombre"
        self.assertEqual(self.lugar1.ubicacion, "MYS") , 
        "Falla asignando ubicacion"
        self.assertEqual(self.lugar1.capacidad_maxima,50),
        "Falla asignando capacidad maxima"

    def test_is_Equal(self):
        self.lugar1.equals(self.lugar2),  
        "Falla comparando si dos lugares son distintos"    
        self.lugar1.equals(self.lugar3),  
        "Falla comparando si dos lugares son distintos"
         
if __name__ == "__main__":
    unittest.main()