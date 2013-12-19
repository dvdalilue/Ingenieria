#*****************************************************************************
# Clase : Probar_Clases.py
#
# Descripcion : Clase que implementa las pruebas unitarias
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************
import unittest
from Articulo import Articulo
from CLEI import *
from Persona import *
from Topico import Topico

# Pruebas de la clase Articulo
class Test_Articulo(unittest.TestCase):

    # creacion del articulo con el que se trabajara en el modulo
    def setUp(self):
        self.art = Articulo(1,"Titulo1", ["Pedro Perez"], ["Palabra" ,"clave"], ["bases de datos"] )
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
         
        m1 = Miembro_Cp(3,"Coronel", "Mostaza", "USB", "ma@usb.ve" ,"Venezuela","")
    
    # colocando la primera evaluacion del articulo
        self.art.Calificar(m1, 1)
        assert self.art.Calificaciones == [1] , "falla colocando la primera puntuacion"
        assert self.art.Jurado == [m1] , "falla colocando al primer jurado"
        
        m2 = Miembro_Cp(4,"Blanco", "Rojo", "USB", "br@usb.ve" ,"Venezuela","")
        
        # colocando la segunda evaluacion del articulo
        self.art.Calificar(m2, 4)
        assert self.art.Calificaciones == [1,4] ,"falla colocando la segunda puntuacion" 
        assert self.art.Jurado == [m1,m2] , "falla colocando al segundo jurado"
        
        m3 = Miembro_Cp(5,"Verdi", "Camejo", "USB", "vc@usb.ve" ,"Venezuela","")
        
        #colocando la tercera con un valor de puntaje invalido
        self.art.Calificar(m3,8)
        assert self.art.Calificaciones == [1,4] ,"falla colocando la tercera puntuacion" 
        assert self.art.Jurado == [m1,m2] , "falla colocando al tercer jurado"
        
        self.art.Calificar(m3,5)
        assert self.art.Calificaciones == [1,4,5] ,"falla colocando la tercera puntuacion" 
        assert self.art.Jurado == [m1,m2,m3] , "falla colocando al tercer jurado"
        
        # prueba para verificar que un jurado pueda votar dos veces o mas
        self.assertEqual(self.art.Calificar(m2, 2), False) , "falla si un jurado vuelve a intentar calificar un articulo"
      
    # se inicializan los atributos del articulo para no interrumpir la proxima prueba 
        self.art.Calificaciones = []
        self.art.Jurado = []
    
    # prueba del metodo calcular_promedio
    def test_calcular_promedio(self):
      
    # calificamos un articulo con una puntuacion y calculamos su promedio
        self.art.Calificar("a", 1)
        self.art.calcular_promedio()
        self.assertEqual(self.art.Puntaje_promedio, 1 ) , "Falla calculando promedio con 1 elemento"
        
        self.art.Calificaciones = []
        self.art.Jurado = []
        
        #calificamos un articulo con dos puntuaciones y calculamos su promedio
        self.art.Calificar("a", 2)
        self.art.Calificar("b", 1)
        self.art.calcular_promedio()
        self.assertEqual(self.art.Puntaje_promedio, 1.5 ) , "Falla calculando promedio con 2 elementos"
        
        self.art.Calificaciones = []
        self.art.Jurado = []
        
        #calificamos un articulo con cuatro puntuaciones y calculamos su promedio
        self.art.Calificar("a", 2)
        self.art.Calificar("b", 4)
        self.art.Calificar("c", 5)
        self.art.Calificar("d", 3)
            
        self.art.calcular_promedio()
        self.assertEqual(self.art.Puntaje_promedio, 3.5 ) , "Falla calculando promedio con mas de 2 elementos"
        
        #se inicializan los atributos del articulos
        self.art.Calificaciones = []
        self.art.Jurado = []
        
    #   prueba para verificar si el atributo es aceptable o no
    def test_verificar_Aceptable(self):
        
        # verificar aceptable con promedio mayor a 3
        self.art.Calificar("a", 2)
        self.art.Calificar("b", 4)
        self.art.Calificar("c", 5)
        self.art.Calificar("d", 3)
        self.art.verificar_Aceptable()    
        self.assertEqual(self.art.Aceptable, True ) , "Falla verificando aceptable con promedio mayor a 3"
        
        self.art.Calificaciones = []
        self.art.Jurado = []
        
        # verificar aceptable con promedio  igual a 3
        self.art.Calificar("a", 3)
        self.art.Calificar("b", 3)
        self.art.Calificar("c", 3)
        self.art.verificar_Aceptable()    
        self.assertEqual(self.art.Aceptable, True ) , "Falla verificando aceptable con promedio igual a 3"
        
        self.art.Calificaciones = []
        self.art.Jurado = []
        
        # verificar aceptable con promedio mayor a 3, pero votaciones menor a dos
        self.art.Calificar("a", 4)
        self.art.verificar_Aceptable()
        self.assertEqual(self.art.Aceptable, False ) , "Falla verificando aceptable cuando faltan jurados por evaluar "

# Pruebas de la clase CLEI
class Test_CLEI(unittest.TestCase):      
    
    #se crea el objeto CLEI sobre el que se realizaran las pruebas
    def setUp(self):
        self.CLEI = CLEI()
    
    # prueba de aniadir miembro cp
    def test_aniadir_miembro_Cp(self):
    #prueba agregando al primer miembro
        assert self.CLEI.Aniadir_Miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so") == True, "Falla agregar un miembro"
        #prueba agregando un miembro nuevo con misma CI
        assert self.CLEI.Aniadir_Miembro(2,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina", "bd") == False, "Falla agregar un miembro con misma CI"
        #prueba agregando un nuevo miembro
        assert self.CLEI.Aniadir_Miembro(3,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina","bd") == True, "Falla agregar un miembro "
 
    # prueba de aniadir articulo
    def test_aniadir_articulo(self):
    #creamos autor
        self.Gries = Inscrito(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        #creamos topico
        self.logica = Topico("logica")
        
        # prueba agregando articulo
        assert self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica) == True , "Fallo agregar un articulo"
        # verificando que no se agreguen dos veces el mismo articulo
        assert self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica) == False , "Fallo agregar un articulo existente"
    
    # prueba para verificar votacion
    def test_Realizar_Votacion(self):
       
        # se crean los autores
        self.Autor1 = Inscrito(11, "Autor1", "Apeliido1", "MIT", "a1@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        self.Autor2 = Inscrito(12, "Autor2", "Apeliido2", "MIT", "a2@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        self.Autor3 = Inscrito(13, "Autor3", "Apeliido3", "MIT", "a3@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        self.Gries = Inscrito(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
       
        # se crean los topicos
        self.discretas = Topico("discretas")
        self.logica = Topico("logica")
        self.ingenieria = Topico("ingenieria de software")
         
        # se crean los articulos 
        self.CLEI.Aniadir_Articulo(7,"logica y matematica", self.Autor1, [ "logica"], self.logica) 
        self.CLEI.Aniadir_Articulo(5,"discretas", self.Autor2, ["discretas"], self.discretas)
        self.CLEI.Aniadir_Articulo(6,"lingenieria", self.Autor3, ["ingenieria"], self.ingenieria)
        self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica)
        
        # see crean los miembros del cp que evaluaran dichos articulos
        self.CLEI.Aniadir_Miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so") 
        self.CLEI.Aniadir_Miembro(3,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina", "bd")
        self.CLEI.Aniadir_Miembro(1,"Pedro", "Artigas","USB", "pa@gmail.com", "Venezuela", "bd")
 
        # prueba realizando votacion
        assert self.CLEI.Realizar_Votacion(2,1,3) == True , "Fallo al realizar votacion"
        # se verifica que un juez no pueda votar dos veces por un mismo articulo
        assert self.CLEI.Realizar_Votacion(2,1,4) == False , "Fallo al realizar votacion, con el mismo Juez en el mismo articulo"
        #se verifica que no se pueda votar con un puntaje invalido
        assert self.CLEI.Realizar_Votacion(2,2,6) == False , "Fallo al realizar votacion con puntaje invalido"

     
        # prueba para verificar que la lista de aceptables se ordene
    
    def test_Ordenar_articulos(self):
      
        # se crean los autores
        self.Autor1 = Inscrito(11, "Autor1", "Apeliido1", "MIT", "a1@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        self.Autor2 = Inscrito(12, "Autor2", "Apeliido2", "MIT", "a2@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        self.Autor3 = Inscrito(13, "Autor3", "Apeliido3", "MIT", "a3@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
        self.Gries = Inscrito(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
       
        # se crean los topicos
        self.discretas = Topico("discretas")
        self.logica = Topico("logica")
        self.ingenieria = Topico("ingenieria de software")
        
        # se crean los articulos 
        
        self.CLEI.Aniadir_Articulo(3,"logica y matematica", self.Autor1, [ "logica"], self.logica) 
        self.CLEI.Aniadir_Articulo(1,"discretas", self.Autor2, ["discretas"], self.discretas)
        self.CLEI.Aniadir_Articulo(0,"lngenieria", self.Autor3, ["ingenieria"], self.ingenieria)
        self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica)
         
        # see crean los miembros del cp que evaluaran dichos articulos
        self.CLEI.Aniadir_Miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so") 
        self.CLEI.Aniadir_Miembro(0,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina", "bd")
        self.CLEI.Aniadir_Miembro(1,"Pedro", "Artigas","USB", "pa@gmail.com", "Venezuela", "bd")
 
        # se realizan votaciones para cada articulo
        self.CLEI.Realizar_Votacion(0,0,2)
        self.CLEI.Realizar_Votacion(0,1,4)
        self.CLEI.Realizar_Votacion(0,2,3)
    
        self.CLEI.Realizar_Votacion(1,0,5)
        self.CLEI.Realizar_Votacion(1,1,4)
        self.CLEI.Realizar_Votacion(1,2,1)
    
        self.CLEI.Realizar_Votacion(2,0,5)
        self.CLEI.Realizar_Votacion(2,1,5)
        self.CLEI.Realizar_Votacion(2,2,3)
    
        self.CLEI.Realizar_Votacion(3,0,3)
        self.CLEI.Realizar_Votacion(3,1,4)
        self.CLEI.Realizar_Votacion(3,2,3)
    
        # se verifica que los id de los articulos ordenados coincidan con la
        # forma que se esperaba que se ordenaran
        p = self.CLEI.Ordenar_Articulos()
        #otra forma:
        # self.assertEqual(p, sorted(self.CLEI.Aceptables, key=lambda aceptable: aceptable.Puntaje_promedio, reverse=True) ) , "Falla Ordenando"
        l = []
        for i in p:
            l.append(i.Id_Articulo)
    
        self.assertEqual(l, [2,3,1,0] ) , "Falla Ordenando"

    # prueba para verificar los articulos admitidos
    def test_Filtrar_Admitidos(self):
  
	#se crean los autores
	self.Autor1 = Inscrito(11, "Autor1", "Apeliido1", "MIT", "a1@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Autor2 = Inscrito(12, "Autor2", "Apeliido2", "MIT", "a2@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Autor3 = Inscrito(13, "Autor3", "Apeliido3", "MIT", "a3@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Gries = Inscrito(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
    
	# se crean los topicos
	self.discretas = Topico("discretas")
	self.logica = Topico("logica")
	self.ingenieria = Topico("ingenieria de software")
    
	# se crean los articulos 
	self.CLEI.Aniadir_Articulo(3,"logica y matematica", self.Autor1, [ "logica"], self.logica) 
	self.CLEI.Aniadir_Articulo(1,"discretas", self.Autor2, ["discretas"], self.discretas)
	self.CLEI.Aniadir_Articulo(0,"lngenieria", self.Autor3, ["ingenieria"], self.ingenieria)
	self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica)
      
	# see crean los miembros del cp que evaluaran dichos articulos
	self.CLEI.Aniadir_Miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so") 
	self.CLEI.Aniadir_Miembro(0,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina", "bd")
	self.CLEI.Aniadir_Miembro(1,"Pedro", "Artigas","USB", "pa@gmail.com", "Venezuela", "bd")

	# se realizan votaciones para cada articulo
	self.CLEI.Realizar_Votacion(0,0,2)
	self.CLEI.Realizar_Votacion(0,1,4)
	self.CLEI.Realizar_Votacion(0,2,3)

	self.CLEI.Realizar_Votacion(1,0,5)
	self.CLEI.Realizar_Votacion(1,1,4)
	self.CLEI.Realizar_Votacion(1,2,1)

	self.CLEI.Realizar_Votacion(2,0,5)
	self.CLEI.Realizar_Votacion(2,1,5)
	self.CLEI.Realizar_Votacion(2,2,3)

	self.CLEI.Realizar_Votacion(3,0,3)
	self.CLEI.Realizar_Votacion(3,1,4)
	self.CLEI.Realizar_Votacion(3,2,3)

	
	  
	  
	### se verifica filtrar admitidos para un n mayor al numero de articulos aceptables
	r10 = [[4.333333333333333, 2], [3.3333333333333335, 3], [3.3333333333333335, 1], [3.0, 0]]
	
	
	q = self.CLEI.Filtrar_Admitidos(10)
	l = []
	for i in q:
	    l.append([i.Puntaje_promedio, i.Id_Articulo])
	   
	    
	    
	self.assertEqual(l,r10) , "Fallo filtrando articulos con n mayor a numero de articulos"

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []

	# se verifica filtrar admitidos para un el numero de articulos  menos 1 (sin empates en el borde)
	r3 = [[4.333333333333333, 2], [3.3333333333333335, 3], [3.3333333333333335, 1]]
	
	q = self.CLEI.Filtrar_Admitidos(3)
	l = []
	for i in q:
	    l.append([i.Puntaje_promedio, i.Id_Articulo])

	self.assertEqual(l,r3) , "Fallo filtrando articulos con n igual a numero de articulos menos uno"

    
	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []

	# se verifica filtrar admitidos para un n = 2 pero con el segundo articulo empatado
	r2 = [[4.333333333333333, 2]]
	
	q = self.CLEI.Filtrar_Admitidos(2)
	l = []
	for i in q:
	    l.append([i.Puntaje_promedio, i.Id_Articulo])

	self.assertEqual(l,r2) , "Fallo filtrando numero de articulos aceptables con empates mayores a n"

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []

	# se verifica filtrar admitidos para un n = 1 (con ningun empate)
	r1 = [[4.333333333333333, 2]]

	
	q = self.CLEI.Filtrar_Admitidos(1)
	l = []
	for i in q:
	    l.append([i.Puntaje_promedio, i.Id_Articulo])

	self.assertEqual(l,r1) , "Fallo filtrando numero de articulos con n = 1"


	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []

	# se verifica filtrar admitidos para un n = 0
	r0 = []

	
	q = self.CLEI.Filtrar_Admitidos(0)
	l = []
	for i in q:
	    l.append([i.Puntaje_promedio, i.Id_Articulo])

	self.assertEqual(l,r0) , "Fallo filtrando numero de articulos con n = 0"

       # prueba para filtrar empatados
    def test_Filtrar_Empatados(self):

	# se crean los autores
	self.Autor1 = Inscrito(11, "Autor1", "Apeliido1", "MIT", "a1@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Autor2 = Inscrito(12, "Autor2", "Apeliido2", "MIT", "a2@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Autor3 = Inscrito(13, "Autor3", "Apeliido3", "MIT", "a3@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Gries = Inscrito(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
    
	# se crean los topicos
	self.discretas = Topico("discretas")
	self.logica = Topico("logica")
	self.ingenieria = Topico("ingenieria de software")
    
	# se crean los articulos 
    
	self.CLEI.Aniadir_Articulo(3,"logica y matematica", self.Autor1, [ "logica"], self.logica) 
	self.CLEI.Aniadir_Articulo(1,"discretas", self.Autor2, ["discretas"], self.discretas)
	self.CLEI.Aniadir_Articulo(0,"lngenieria", self.Autor3, ["ingenieria"], self.ingenieria)
	self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica)
      
	# se crean los miembros del cp que evaluaran dichos articulos
	self.CLEI.Aniadir_Miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so") 
	self.CLEI.Aniadir_Miembro(0,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina","bd")
	self.CLEI.Aniadir_Miembro(1,"Pedro", "Artigas","USB", "pa@gmail.com", "Venezuela",  "bd")

	# se realizan votaciones para cada articulo

	self.CLEI.Realizar_Votacion(0,0,2)
	self.CLEI.Realizar_Votacion(0,1,4)
	self.CLEI.Realizar_Votacion(0,2,3)

	self.CLEI.Realizar_Votacion(1,0,5)
	self.CLEI.Realizar_Votacion(1,1,4)
	self.CLEI.Realizar_Votacion(1,2,1)

	self.CLEI.Realizar_Votacion(2,0,5)
	self.CLEI.Realizar_Votacion(2,1,5)
	self.CLEI.Realizar_Votacion(2,2,3)

	self.CLEI.Realizar_Votacion(3,0,3)
	self.CLEI.Realizar_Votacion(3,1,4)
	self.CLEI.Realizar_Votacion(3,2,3)

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []
	self.CLEI.Empatados = []
	
	#"se verifican empatados para las mismas opciones que admitidos"
	# se verifica filtrar empatados  para un n mayor al numero de articulos aceptables
	
	q = self.CLEI.Filtrar_Empatados(10)
	l = []
	if len(q[1]) != 0: 
	  for i in q[1]:
	     l.append([i.Puntaje_promedio, i.Id_Articulo])
	
	
	r10 = []
	self.assertEqual(l,r10) , "Fallo filtrando articulos empatados con n mayor a numero de articulos admitidos"

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []
	self.CLEI.Empatados = []

	## se verifica filtrar empatados para un el numero de articulos  menos 1 (sin empates en el borde)
	
	q = self.CLEI.Filtrar_Empatados(3)
	l = []
	if len(q[1]) != 0: 
	  for i in q[1]:
	     l.append([i.Puntaje_promedio, i.Id_Articulo])
	
	
	
	r3 = []
	self.assertEqual(l,r3) , "Fallo filtrando articulos empatados con N= 3"

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []
	self.CLEI.Empatados = []

	# se verifica filtrar empatados para un n = 2 pero con el segundo articulo empatado
	q = self.CLEI.Filtrar_Empatados(2)
	l = []
	if len(q[1]) != 0: 
	  for i in q[1]:
	     l.append([i.Puntaje_promedio, i.Id_Articulo])
	
	
	r2 = [[3.3333333333333335, 3], [3.3333333333333335, 1]]

	self.assertEqual(l,r2) , "Fallo filtrando articulos N = 2"

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []
	self.CLEI.Empatados = []

	## se verifica filtrar admitidos para un n = 1 (con ningun empate en el borde)
	q = self.CLEI.Filtrar_Empatados(1)
	l = []
	if len(q[1]) != 0: 
	  for i in q[1]:
	     l.append([i.Puntaje_promedio, i.Id_Articulo])
	
	

	r1 = []
	self.assertEqual(l,r1) , "Fallo filtrando articulos empatados con n mayor a numero de articulos admitidos"

	self.CLEI.Admitidos = []
	self.CLEI.Aceptables = []
	self.CLEI.Empatados = []

	## se verifica filtrar empatados para un n = 0
	q = self.CLEI.Filtrar_Empatados(0)
	l = []
	if len(q[1]) != 0: 
	  for i in q[1]:
	     l.append([i.Puntaje_promedio, i.Id_Articulo])
	
	

	r0 = []
	self.assertEqual(l,r0) , "Fallo filtrando articulos empatados con n mayor a numero de articulos admitidos"

  ## prueba para generar listas
    def test_Generar_Listas(self):

	# se crean los autores
	self.Autor1 = Inscrito(11, "Autor1", "Apeliido1", "MIT", "a1@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Autor2 = Inscrito(12, "Autor2", "Apeliido2", "MIT", "a2@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Autor3 = Inscrito(13, "Autor3", "Apeliido3", "MIT", "a3@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
	self.Gries = Inscrito(10, "Gries", "Black", "MIT", "gb@hotmail.com", "EEUU",False ,False,True,1015, "http://g.com",212)
    
	# se crean los topicos
	self.discretas = Topico("discretas")
	self.logica = Topico("logica")
	self.ingenieria = Topico("ingenieria de software")
    
	# se crean los articulos 
	self.CLEI.Aniadir_Articulo(3,"logica y matematica", self.Autor1, [ "logica", "fisica cuantica"], self.logica) 
	self.CLEI.Aniadir_Articulo(1,"discretas", self.Autor2, ["discretas"], self.discretas)
	self.CLEI.Aniadir_Articulo(0,"lngenieria", self.Autor3, ["ingenieria"], self.ingenieria)
	self.CLEI.Aniadir_Articulo(2,"logica y matematica", self.Gries, ["discretas", "logica"], self.logica)
      
	# se crean los miembros del cp que evaluaran dichos articulos
	self.CLEI.Aniadir_Miembro(2,"Julio", "Vargas","Instituto Tecnologico", "jv@gmail.com", "Argentina", "so") 
	self.CLEI.Aniadir_Miembro(0,"Andrea", "Vargas","Instituto Tecnologico", "av@gmail.com", "Argentina", "bd")
	self.CLEI.Aniadir_Miembro(1,"Pedro", "Artigas","USB", "pa@gmail.com", "Venezuela", "bd")

	# se realizan votaciones para cada articulo

	self.CLEI.Realizar_Votacion(0,0,2)
	self.CLEI.Realizar_Votacion(0,1,4)
	self.CLEI.Realizar_Votacion(0,2,3)

	self.CLEI.Realizar_Votacion(1,0,5)
	self.CLEI.Realizar_Votacion(1,1,4)
	self.CLEI.Realizar_Votacion(1,2,1)

	self.CLEI.Realizar_Votacion(2,0,5)
	self.CLEI.Realizar_Votacion(2,1,5)
	self.CLEI.Realizar_Votacion(2,2,3)

	self.CLEI.Realizar_Votacion(3,0,3)
	self.CLEI.Realizar_Votacion(3,1,4)
	self.CLEI.Realizar_Votacion(3,2,3)

	# se verifica que generar e imprimir listas de admitidos y empatados
	#se ejecute correctamente
	assert self.CLEI.Generar_Listas(10) == True , "Falla generando listas"
	assert self.CLEI.Generar_Listas(4) == True , "Falla generando listas"
	assert self.CLEI.Generar_Listas(3) == True , "Falla generando listas"
	assert self.CLEI.Generar_Listas(2) == True , "Falla generando listas"
	assert self.CLEI.Generar_Listas(1) == True , "Falla generando listas"
	assert self.CLEI.Generar_Listas(0) == True , "Falla generando listas"
	assert self.CLEI.Generar_Listas(-1) == False , "Falla generando listas"
	
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_persona']
    unittest.main()
