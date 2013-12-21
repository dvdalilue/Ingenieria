#*****************************************************************************
# Clase :Pruebas_CleiI.py
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


# Pruebas de la clase CLEI
class Test_CLEI(unittest.TestCase):      
    
    #se crea el objeto CLEI sobre el que se realizaran las pruebas
    def setUp(self):
        self.CLEI = CLEI()
        #creamos autor
        self.Gries = Asistente(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False,True,1015, "http://g.com",212)
      
        
    
    # prueba de aniadir miembro cp
    def test_aniadir_miembro_Cp(self):
    #prueba agregando al primer miembro
        self.assertTrue(self.CLEI.aniadir_miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so")), "Falla agregar un miembro"
        #prueba agregando un miembro nuevo con misma CI
        self.assertFalse(self.CLEI.aniadir_miembro(2,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina", "bd")), "Falla agregar un miembro con misma CI"
        #prueba agregando un nuevo miembro
        self.assertTrue(self.CLEI.aniadir_miembro(3,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina","bd")), "Falla agregar un miembro "
 
    # prueba de aniadir articulo
    def test_aniadir_articulo(self):
		
        # prueba agregando articulo
        self.assertTrue(self.CLEI.aniadir_articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], "logica", "texto1", "resumen1")) , "Fallo agregar un articulo"
        # verificando que no se agreguen dos veces el mismo articulo
        self.assertFalse(self.CLEI.aniadir_articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], "logica", "texto1", "resumen1")) , "Fallo agregar un articulo existente"
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_persona']
    unittest.main()