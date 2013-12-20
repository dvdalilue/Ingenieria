CLEI - [CI-3715] Ingenieria de Software I
==========

Tareas del Lab de Ingenieria de Soft.

Diagrama de Clases del CLEI, Clases, Funcionalidades & Pruebas Unittest

Diagrama de Clases
------

En la primera entrega se realizo el diagrama de clases que
representara todas las partes y permitiera que se dieran todos los
requerimientos que exige el CLEI 

Clases & Unittest
-----------

A partir de la segunda etapa, se implemetaron las clases
correspondientes al diagrama para lograr las funcionalidades
requeridas para la Tarea 2. Adicionalmente la creacion de un main.py
para la interaccion de la clases, simulando el software de
CLEI. Tambien la creacion de un archivo de pruebas unitarias, haciendo
uso del `TDD` con un codigo parecido al siguiente:

```python
from Articulo import *

class Test_Articulo(unittest.TestCase):

    # creacion del articulo con el que se trabajara en el modulo
    def setUp(self):
        self.art = Articulo(1,"Titulo1", ["Pedro Perez"], ["Palabra" ,"clave"], ["bases de datos"], "texto", "resumen")
        self.art2 = Articulo(2,"Titulo2", ["Jose Perez"], ["Pal" ,"cla"], ["bases datos"], "texto", "resumen")
        self.m1 = MiembroCp(3,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela")
        self.m2 = MiembroCp(4,"Blanco", "Rojo", "USB", "br@usb.ve" ,"Venezuela")
        self.m3 = MiembroCp(5,"Verdi", "Camejo", "USB", "vc@usb.ve" ,"Venezuela")
        self.m4 = MiembroCp(6,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela")
     
    # prueba del metodo calificar 
    def test_calificar_articulo(self):
    
    # colocando la primera evaluacion del articulo
        self.art.calificar(self.m1, 1)
        self.assertEqual(self.art.calificaciones, [1]), "falla colocando la primera puntuacion"
        self.assertEqual(self.art.jurado[0], self.m1) , "falla colocando al primer jurado"

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

if __name__ == "__main__":
    unittest.main()
``` 

En estas pruebas, cada una cuando comienza. Realiza el setUp, asi que
en cada una debe hacer algo independiente de las demas.



