#*****************************************************************************
# Clase : prueba_inscripcion.py
#
# Descripcion : Clase que implementa las pruebas unitarias de la clase inscripcion
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
import datetime
from inscripcion import Inscripcion
from Persona import Asistente

#Pruebas del modulo inscripcion.py

class Test_inscripcion(unittest.TestCase):
    #creacion de unos objeto inscripcion
    def setUp(self):
        self.asistente1 = Asistente(19650146, "Audry", "Morillo", "USB",
                                    "audrymorillo@gmail.com","1020","4428862",
                                    False,False,"http://audry.com")
        self.asistente2 = Asistente(19650147, "Au", "Mori", "USB",
                                    "audrymori@hotmail.com","1020","4428862",
                                    False,False,"http://audry.com")
        self.fecha_inscripcion = datetime.date(2013,12,19)
        self.inscripcion1 = Inscripcion(self.asistente1,self.fecha_inscripcion,
                                        150.00 )
        self.inscripcion2 = Inscripcion(self.asistente2,self.fecha_inscripcion,
                                        130.00 )
 
    def test_crear_inscripcion(self):
        self.assertEqual(self.inscripcion1.asistente, self.asistente1), 
        "Falla asignando asistente"
        self.assertEqual(self.inscripcion1.fecha_inscripcion, 
                         self.fecha_inscripcion), "Falla asignando fecha"
        self.assertEqual(self.inscripcion1.monto, 150.00), 
        "Falla asignando monto"
        
        
if __name__ == "__main__":
    unittest.main()