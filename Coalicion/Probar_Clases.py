#*****************************************************************************
# Clase : Probar_Clases
#
# Descripcion : Clase que implementa las pruebas unitarias
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Liniayo  #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************
import unittest
from Articulo import *

# Pruebas de la clase Articulo
class Test_Articulo(unittest.TestCase):

    # creacion del articulo con el que se trabajara en el modulo
    def setUp(self):
        self.art = Articulo(1,"Titulo1", ["Pedro Perez"], ["Palabra" ,"clave"], ["bases de datos"], "texto", "resumen")
        self.art2 = Articulo(2,"Titulo2", ["Jose Perez"], ["Pal" ,"cla"], ["bases datos"], "texto", "resumen")
        self.m1 = MiembroCp(3,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela")
        self.m2 = MiembroCp(4,"Blanco", "Rojo", "USB", "br@usb.ve" ,"Venezuela")
        self.m3 = MiembroCp(5,"Verdi", "Camejo", "USB", "vc@usb.ve" ,"Venezuela")
        self.m4 = MiembroCp(6,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela")
        self.m5 = MiembroCp(7,"Blanco", "Rojo", "USB", "br@usb.ve" ,"Venezuela")
        self.m6 = MiembroCp(8,"Verdi", "Camejo", "USB", "vc@usb.ve" ,"Venezuela")
    
    def test_art(self):

        self.assertEqual(self.art.titulo, "Titulo1")
        self.assertEqual(self.art.autor, ["Pedro Perez"])
        self.assertEqual(self.art.palabras_claves, ["Palabra", "clave"])
        self.assertEqual(self.art.topico, ["bases de datos"])
        self.assertEqual(self.art.jurado, [])
        self.assertEqual(self.art.aceptable, False)
        self.assertEqual(self.art.calificaciones, [] )
        self.assertEqual(self.art.puntaje_promedio, 0.0)
     
    # prueba del metodo calificar 
    def test_calificar_articulo(self):
    
    # colocando la primera evaluacion del articulo
        self.art.calificar(self.m1, 1)
        self.assertEqual(self.art.calificaciones, [1]), "falla colocando la primera puntuacion"
        self.assertEqual(self.art.jurado[0], self.m1) , "falla colocando al primer jurado"

    def test_calificar_articulo2(self):

        # colocando la segunda evaluacion del articulo
        self.art.calificar(self.m1, 1)
        self.art.calificar(self.m2, 4)
        self.assertEqual(self.art.calificaciones, [1,4]) ,"falla colocando la segunda puntuacion"
        self.assertEqual(self.art.jurado[1], self.m2) , "falla colocando al segundo jurado"
    #colocando la tercera con un valor de puntaje invalido
    def test_calificar_articulo3(self):
        
        self.assertFalse(self.art.calificar(self.m3,6))
        self.assertEqual(self.art.calificaciones, []),"falla colocando la tercera puntuacion"
    
    def test_calificar_articulo4(self):
 
        self.assertTrue(self.art.calificar(self.m2,3))
        self.assertFalse(self.art.calificar(self.m2,4))
        self.assertEqual(self.art.calificaciones, [3] ),"falla colocando  puntuacion de un juez que ya voto"
        
    def test_promedio(self):

        self.assertTrue(self.art.calificar(self.m1, 1))
        self.assertTrue(self.art.calificar(self.m2, 4))
        self.assertTrue(self.art.calificar(self.m3, 5))
        self.assertEqual(self.art.calificaciones, [1,4,5]) ,"falla colocando la tercera puntuacion"
        self.art.calcular_promedio()
        self.assertEqual(self.art.puntaje_promedio, 3.3333333333333335)
 
    def test_verificar_Aceptable_ATrue(self):

        self.assertTrue(self.art.calificar(self.m1, 4))
        self.assertTrue(self.art.calificar(self.m2, 2))
        self.assertTrue(self.art.calificar(self.m3, 5))
        self.assertTrue(self.art.calificar(self.m4, 3))
        self.art.calcular_promedio()
        self.assertEqual(self.art.puntaje_promedio, 3.5) 
        self.assertTrue(self.art.verificar_aceptable()) , "Falla verificando un articulo aceptable"
 
    def test_verificar_Aceptable_BFalse(self):
 
        self.art.calificar(self.m5,1)
        self.art.calificar(self.m6,1)
        self.art.calcular_promedio()
        self.assertFalse(self.art.verificar_aceptable()) , "Falla verifcando articulo no aceptable"
 
    def test_verificar_Aceptable_falta_jurado(self):
        self.art2.calificar(self.m1, 3)
        self.assertFalse(self.art2.verificar_aceptable()) , "Falla verifcando articulo con un solo jurado"
        
        self.art2.calificar(self.m2, 4)
        self.assertFalse(self.art2.verificar_aceptable()) , "Falla verifcando articulo con dos jurados"

        self.art2.calificar(self.m3, 3)
        self.assertTrue(self.art2.verificar_aceptable()) , "Falla verifcando articulo con tres jurados"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_persona']
    unittest.main()
