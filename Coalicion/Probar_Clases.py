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
import Articulo
from Persona import Persona, Asistente, Miembro_Cp


# Pruebas de la clase Articulo
class Test_Articulo(unittest.TestCase):

    # creacion del articulo con el que se trabajara en el modulo
    def setUp(self):
        self.art = Articulo.Articulo(1,"Titulo1", ["Pedro Perez"], ["Palabra" ,"clave"], ["bases de datos"])
        self.perrito = Articulo.Articulo(2,"Titulo2", ["Jose Perez"], ["Pal" ,"cla"], ["bases datos"])
        self.m1 = Miembro_Cp(3,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela")
        self.m2 = Miembro_Cp(4,"Blanco", "Rojo", "USB", "br@usb.ve" ,"Venezuela")
        self.m3 = Miembro_Cp(5,"Verdi", "Camejo", "USB", "vc@usb.ve" ,"Venezuela")
        self.m4 = Miembro_Cp(6,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela")
        self.m5 = Miembro_Cp(7,"Blanco", "Rojo", "USB", "br@usb.ve" ,"Venezuela")
        self.m6 = Miembro_Cp(8,"Verdi", "Camejo", "USB", "vc@usb.ve" ,"Venezuela")
    
    def test_art(self):

        self.assertEqual(self.art.Titulo, "Titulo1")
        self.assertEqual(self.art.Autor, ["Pedro Perez"])
        self.assertEqual(self.art.Palabras_Claves, ["Palabra", "clave"])
        self.assertEqual(self.art.Topico, ["bases de datos"])
        self.assertEqual(self.art.Jurado, [])
        self.assertEqual(self.art.Aceptable, False)
        self.assertEqual(self.art.Calificaciones, [] )
        self.assertEqual(self.art.Puntaje_promedio, 0.0)
     
    # prueba del metodo calificar 
    def test_calificar_articulo(self):
    
    # colocando la primera evaluacion del articulo
        self.art.Calificar(self.m1, 1)
        self.assertEqual(self.art.Calificaciones, [1]), "falla colocando la primera puntuacion"
        self.assertEqual(self.art.Jurado[0], self.m1) , "falla colocando al primer jurado"

    def test_calificar_articulo2(self):

        # colocando la segunda evaluacion del articulo
        self.art.Calificar(self.m1, 1)
        self.art.Calificar(self.m2, 4)
        self.assertEqual(self.art.Calificaciones, [1,4]) ,"falla colocando la segunda puntuacion"
        self.assertEqual(self.art.Jurado[1], self.m2) , "falla colocando al segundo jurado"
    #colocando la tercera con un valor de puntaje invalido
    def test_calificar_articulo3(self):
        
        self.assertFalse(self.art.Calificar(self.m3,6))
        self.assertEqual(self.art.Calificaciones, []),"falla colocando la tercera puntuacion"
    
    def test_calificar_articulo4(self):
 
        self.assertTrue(self.art.Calificar(self.m2,3))
        self.assertFalse(self.art.Calificar(self.m2,4))
        self.assertEqual(self.art.Calificaciones, [3] ),"falla colocando  puntuacion de un juez que ya voto"
        
    def test_promedio(self):

        self.assertTrue(self.art.Calificar(self.m1, 1))
        self.assertTrue(self.art.Calificar(self.m2, 4))
        self.assertTrue(self.art.Calificar(self.m3, 5))
        self.assertEqual(self.art.Calificaciones, [1,4,5]) ,"falla colocando la tercera puntuacion"
        self.art.calcular_promedio()
        self.assertEqual(self.art.Puntaje_promedio, 3.3333333333333335)
 
    def test_verificar_Aceptable_ATrue(self):

        self.assertTrue(self.art.Calificar(self.m1, 4))
        self.assertTrue(self.art.Calificar(self.m2, 2))
        self.assertTrue(self.art.Calificar(self.m3, 5))
        self.assertTrue(self.art.Calificar(self.m4, 3))
        self.art.calcular_promedio()
        self.assertEqual(self.art.Puntaje_promedio, 3.5) 
        self.assertTrue(self.art.verificar_Aceptable()) , "Falla verificando un articulo aceptable"
 
    def test_verificar_Aceptable_BFalse(self):
 
        self.art.Calificar(self.m5,1)
        self.art.Calificar(self.m6,1)
        self.art.calcular_promedio()
        self.assertFalse(self.art.verificar_Aceptable()) , "Falla verifcando articulo no aceptable"
 
    def test_verificar_Aceptable_falta_jurado(self):
        self.perrito.Calificar(self.m1, 3)
        self.assertFalse(self.perrito.verificar_Aceptable()) , "Falla verifcando articulo con un solo jurado"
        
        self.perrito.Calificar(self.m2, 4)
        self.assertFalse(self.perrito.verificar_Aceptable()) , "Falla verifcando articulo con dos jurados"

        self.perrito.Calificar(self.m3, 3)
        self.assertTrue(self.perrito.verificar_Aceptable()) , "Falla verifcando articulo con tres jurados"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_persona']
    unittest.main()
