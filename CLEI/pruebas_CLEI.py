'''
Created on 28/11/2013

@author: Audry Morillo
         Michael Woo
'''
import unittest
from clases import *
from funciones import *

class Test(unittest.TestCase):

        
    def setUp(self):
        self.persona = Persona("Audry","Morillo","USB","audrymorillo@gmail.com",
                          "Venezuela")
        self.asistente = Asistente("Audry","Morillo","USB","audrymorillo@gmail.com",
                      "Venezuela","1020","nose","04261395425","100","28-11-13")
        self.comite_programa = ComitePrograma("Audry","Morillo","USB",
                                "audrymorillo@gmail.com", "Venezuela","Musico")
        self.c1 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.c2 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.c3 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.c4 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.d = Articulo(self.persona,"TituloD","TopicoD","ResumenD","TextoD",
                            ['d1','d2','d3'])
        self.e = Articulo(self.asistente,"TituloE","TopicoE","ResumenE","TextoE",
                         ['e1','e2','e3'])
        self.f = Articulo(self.comite_programa,"TituloF","TopicoF","ResumenF",
                     "TextoF", ['f1','f2','f3'])
        
    def test_Presidente(self):
        self.assertFalse(self.comite_programa.EsPresidente)
        self.comite_programa.AsignarPresidencia()
        self.assertTrue(self.comite_programa.EsPresidente)
        
    def test_evaluarArticulo(self):
        
        self.assertTrue(self.comite_programa.EvaluarArticulo(5,self.d))
        self.assertTrue(self.c1.EvaluarArticulo(5,self.d))
        self.assertTrue(self.c2.EvaluarArticulo(3,self.d))
        self.assertTrue(self.c3.EvaluarArticulo(4,self.d))
        self.assertTrue(self.c4.EvaluarArticulo(5,self.d))
        self.assertTrue(self.comite_programa.EvaluarArticulo(5,self.e))
        self.assertTrue(self.c1.EvaluarArticulo(5,self.e))
        self.assertTrue(self.c2.EvaluarArticulo(3,self.e))
        self.assertTrue(self.c3.EvaluarArticulo(3,self.e))
        self.assertTrue(self.c4.EvaluarArticulo(5,self.e))
        self.assertTrue(self.comite_programa.EvaluarArticulo(5,self.f))
        self.assertTrue(self.c1.EvaluarArticulo(5,self.f))
        self.assertTrue(self.c2.EvaluarArticulo(3,self.f))
        self.assertTrue(self.c3.EvaluarArticulo(3,self.f))
        self.assertTrue(self.c4.EvaluarArticulo(5,self.f))
        self.assertEqual(self.d.Evaluar(), None)
        self.assertEqual(self.e.Evaluar(), None)
        self.assertEqual(self.f.Evaluar(), None)
        aceptados = Escoger_Aceptados(1)
        empatados = Escoger_Empatados(1,2)
        print aceptados   
        print empatados
        
    def tearDown(self):
        self.persona = Persona("Audry","Morillo","USB","audrymorillo@gmail.com",
                          "Venezuela")
        self.asistente = Asistente("Audry","Morillo","USB","audrymorillo@gmail.com",
                      "Venezuela","1020","nose","04261395425","100","28-11-13")
        self.comite_programa = ComitePrograma("Audry","Morillo","USB",
                                "audrymorillo@gmail.com", "Venezuela","Musico")
        self.c1 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.c2 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.c3 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.c4 = ComitePrograma("NombreC","ApellidoC","InstitucionC","EmailC",
                            "PaisC", "EspecialidadC")
        self.d = Articulo(self.persona,"TituloD","TopicoD","ResumenD","TextoD",
                            ['d1','d2','d3'])
        self.e = Articulo(self.asistente,"TituloE","TopicoE","ResumenE","TextoE",
                         ['e1','e2','e3'])
        self.f = Articulo(self.comite_programa,"TituloF","TopicoF","ResumenF",
                     "TextoF", ['f1','f2','f3'])
        
    
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()