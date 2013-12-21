#*****************************************************************************
# Clase : CLEI.py
#
# Descripcion : Clase que implementa los Articulos a presentar en el CLEI
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

from Articulo import *
from Persona import MiembroCp
import os

class CLEI(object):
    
    def __init__(self):
        """Constructor"""
        self.lista_articulos = []
        self.miembros_cp = []
        self.aceptables = []
        self.admitidos = []
        self.empatados = []
        self.id_articulo = 0        # variable global que se utilizara para identificar univocamente los articulos
    
    def aniadir_miembro(self, ci, nombre, apellido, institucion_afiliada, email, pais, experticia=None):    
        """ Metodo : aniadir_miembro
        Parametros : self 
        int ci 
        string nombre , apellido , institucion_afiliada , email, pais, cargo, experticia
        Descripcion; dado los atributos de un miembro, se crea y se agrega al arreglo
        correspondiente a los miembros del CP
        """
        # se verifica que no se agregue dos veces al mismo miembro
        for n in self.miembros_cp:
            if n.ci == ci:
                print('Ya existe un miembro con esa CI') 
                return False

        miembro = MiembroCp(ci, nombre, apellido, institucion_afiliada, email, pais, experticia) 
        self.miembros_cp.append(miembro)
        return True     
     
    def aniadir_articulo(self, id_articulo, titulo, autor, palabras_claves,topico, texto, resumen):
        """ Metodo : aniadir_miembro
       Parametros : self 
             int id_articulo
             string titulo
             Autor autor
             string[] palabras_Claves
             string[] Topico
       Descripcion; dado los atributos de un articulo, se crea y se agrega al arreglo
              de articulos
      """
		#se verifica que no se agreguen dos veces el mismo articulo
        for n in self.lista_articulos:
            if n.id_articulo == id_articulo:
                print('Ya existe este articulo')
                return False

        articulo = Articulo(id_articulo, titulo, autor, palabras_claves,topico, texto, resumen)
        self.lista_articulos.append(articulo)
        return True
    
    def crear_comite(self):
        """ 
        Metodo : crear_comite
       Parametros : self 
       Descripcion; pide al usuario los datos necesarios para crear
              los miembros del comite de programa y agregarlos
              al arreglo miembros_cp
        """
        while True:
		  try:
			var = int(raw_input('desea agregar un miembro al comite? \n1. Si \n2. No\n'))
			os.system("clear")
			break
		  except (TypeError, ValueError):
			os.system("clear")
			print "Error, Debe ingresar un numero, trate de nuevo\n"
		# mietras el usuario quiera agregar miembros al comite, se pediran
        # los datos pertienentes para crearlos
        
        while 1 == var:
		  while True:
			  try:
				ci = int(raw_input('introduzca la cedula de identidad: '))
				i = 0
				break
			  except (TypeError, ValueError):
				os.system("clear")
				print "Error, Debe ingresar un numero, trate de nuevo\n"
		  
            # se espera que el usuario coloque un CI que no exista en el sistema
		  while(i < len(self.miembros_cp)):
			if ci == self.miembros_cp[i].ci:
			  while True:
				os.system("clear")
				#se verifica que el valor de la opcion insertada por el usuario sea un entero
				try:
				  ci = int(raw_input('esta cedula de identidad ya esta registrada\nintroduzca la cedula de identidad: '))
				  i = 0
				  break
				except (TypeError, ValueError):
				  os.system("clear")
				  print "Error, Debe ingresar un numero, trate de nuevo\n"
			else:
			  i = i + 1
		  nombre = raw_input('Nombre: ')
		  apellido = raw_input('Apellido: ')
		  institucion_afiliada = raw_input('Institucion Afiliada: ')
		  email = raw_input('Email: ')
		  pais = raw_input('Pais: ')
		  experticia = []
            
		  while True:
			  try:
				var1 = int(raw_input("desea agregar un tema de experiencia? \n1. Si \n2. No\n"))
				os.system("clear")
				break
			  except (TypeError, ValueError):
				os.system("clear")
				print "Error, Debe ingresar un numero, trate de nuevo\n"
			
		  while(var1 == 1):
			experticia.append(raw_input("Topico: "))
			while True:
			  try:
				 var1 = int(raw_input("desea agregar un nuevo tema de experiencia? \n1. Si \n2. No\n"))
				 os.system("clear")
				 break
			  except (TypeError, ValueError):
				os.system("clear")
				print "Error, Debe ingresar un numero, trate de nuevo\n"
		  if (self.aniadir_miembro(ci, nombre, apellido, institucion_afiliada, email, pais, experticia)):
			print('Miembro agregado')
                
		  while True:
			try:
			  var = int(raw_input("desea agregar un miembro al comite? \n1. Si \n2. No\n"))
			  os.system("clear")
			  break
			except (TypeError, ValueError):
			  os.system("clear")
			  print "Error, Debe ingresar un numero, trate de nuevo\n"
        return self.miembros_cp
    
    def elegir_PresidenteCP(self):
        """  Metodo : elegir_PresidenteCP
        Parametros : self
        Descripcion: Cambia el cargo de una miebro a presidente del CP, si todavia no
        existe uno"""
        for i in self.miembros_cp:
            if i.es_presidente == True:
                print ('Lo siento, ya existe un presidente')
                return False
        while True:
		  try:
			id_miembro_cp = int(raw_input('introduzca la cedula de identidad del miembro que eligio de presidente: '))
			break
		  except (TypeError, ValueError):
			os.system("clear")
			print "Error, Debe ingresar un numero, trate de nuevo\n"
        
        # se espera que el usuario coloque un CI que no exista en el sistema
        for i in self.miembros_cp:
            if id_miembro_cp == i.ci:
                i.set_presidente()
                print "\nPresidente elegido con exito\n"
                return True
        print "\nNo existe ese miembro en el comite\n"
        return False

    def crear_articulo(self):
		  
        """ Metodo : crear_articulo
        Parametros : self 
        Descripcion; pide al usuario los datos necesarios para crear
        los articulos que quieren ser presentados en el CLEI
        """
        titulo = raw_input('Titulo del Articulo: ')
        palabras_claves = []
        palabra1 = raw_input('Palabra Clave: ')
        palabras_claves.append(palabra1)
        while True:
            try:
                mas_palabras = int(raw_input("desea agregar mas palabras claves? \n1. Si \n2. No\n"))
                os.system("clear")
                break
            except (TypeError, ValueError):
                os.system("clear")
                print "Error, Debe ingresar un numero, trate de nuevo\n"

        cont = 0
        while mas_palabras == 1 and cont < 5:
            palabra2 = raw_input('Palabra Clave: ')
            palabras_claves.append(palabra2)
            cont = cont + 1
            while True:
                try:
                    mas_palabras = int(raw_input("desea agregar mas palabras claves? \n1. Si \n2. No\n"))
                    os.system("clear")
                    break
                except (TypeError, ValueError):
                    os.system("clear")
                    print "Error, Debe ingresar un numero, trate de nuevo\n"
        topico = raw_input('Topico: ')
        texto =  raw_input('Texto: ')
        resumen =  raw_input('Resumen: ')
       
        while True:
		#se verifica que el valor de la opcion insertada por el usuario sea un entero
            try:
                ci = int(raw_input('CI del Autor: '))
                break
            except (TypeError, ValueError):
                os.system("clear")
                print "Error, Debe ingresar un numero, trate de nuevo\n"
        nombre = raw_input('Nombre del Autor: ')
        apellido = raw_input('Apellido del Autor: ')
        institucion_afiliada= raw_input('Institucion Afiliada del Autor: ')
        email= raw_input('Email del Autor: ')
        pais= raw_input('Pais del Autor: ')
        asistente = False
        ponente = False
        autor = True
        while True:
            #se verifica que el valor de la opcion insertada por el usuario sea un entero
            try:
                cod_postal= int(raw_input('Codigo postal del Autor: '))
                break
            except (TypeError, ValueError):
                os.system("clear")
                print "Error, Debe ingresar un numero, trate de nuevo\n"
        url= raw_input('Url del Autor: ')
        telefono= raw_input('Telefono: ')
        autor = Asistente(ci, nombre, apellido, institucion_afiliada, email, pais, cod_postal, telefono, ponente, autor, url)
        if (self.aniadir_articulo(self.id_articulo, titulo, autor, palabras_claves, topico,texto,resumen)):
            print('Articulo Agregado')
            self.id_articulo = self.id_articulo + 1
 
    def realizar_votacion(self, cod_articulo, ci_miembro_cp, puntaje):
        """ Metodo : realizar_votacion
        Parametros : self 
        int cod_articulo , ci_miembro_cp , puntaje
        Descripcion; se verifica que la persona que vote sea un miembro de cp
        y luego califica el articulo 
        """
        for miembro in self.miembros_cp:
            if miembro.ci == ci_miembro_cp:
                juez = miembro
                for articulo in self.lista_articulos:
                    if articulo.id_articulo == cod_articulo:
                        return articulo.calificar(juez, puntaje)
        print('usted no es miembro del comite ')
        return False

    def ordenar_articulos(self):   
       """ Metodo : ordenar_articulos
      Parametros : self 
      Descripcion; toma todos los articulos de lista_articulos, verifica
      cuales tienen un promedio mayor o igual a 3 y los agrega a la
      lista de aceptables. Luego toma esa lista y las ordena de mayor 
      a menor puntaje
       """
       self.aceptables = []
       for articulo in  self.lista_articulos:
           if articulo.verificar_aceptable():
               self.aceptables.append(articulo)
       lista_ordenada = sorted(self.aceptables, key=lambda aceptable: aceptable.puntaje_promedio, reverse=True) 
       return lista_ordenada
    
    def filtrar_admitidos(self, n):
       """ Metodo : filtrar_admitidos
      Parametros : self 
             int n 
      Descripcion; dado n, el max de articulos admitidos por el CLEI, se
             se filtran los articulo de Lista_Articulos, para elegir
             aquellos con mejores puntuaciones (si el numero
             de empatados supera el valor de n, no se colocan
             en la lista de admitidos)
       """
       admitidos= []
       # se colocan en Lista Ordenada , los articulos aceptables de mayor
       # a menor puntaje
       lista_ordenada = self.ordenar_articulos()
      
       while n > 0:
       #si n es menor al numero de articulos aceptables, debemos elegir cuales tomar
           if n < len(lista_ordenada):
       # si el ultimo articulo no esta empatado con el siguiente, tomamos los n primeros
       # articulos de la lista de articulos aceptables
               if lista_ordenada[n-1].puntaje_promedio !=  lista_ordenada[n].puntaje_promedio:
                   admitidos = lista_ordenada[0:n]
                   return admitidos
               #sino restamos uno, hasta encontrar un articulo que no este empatado con ninguno de
               # los que no hemos admitido
               else:
                   if n > 0:
                       n = n - 1
           #si n es mayor o igual a numero de articulos aceptables        
           else:
       # admitidos sera igual a aceptables
               admitidos = lista_ordenada
               return admitidos
               
       return admitidos

  
if __name__=="__main__":
    
    conferencia = CLEI()
    #conferencia.aniadir_miembro(1,"jose","perez","usb","d@g.com","Ven")
    #print conferencia.miembros_cp[0]
    #conferencia.elegir_PresidenteCP()
    #print conferencia.miembros_cp[0]
    #conferencia.aniadir_articulo(1,"titulo","autor",["pal","cla"],"bd","texto","resumen")
    #print conferencia.lista_articulos[0]
    ##-----
    #conferencia.crear_comite()
    #print "miembros de la conferencia :"
    #for i in conferencia.miembros_cp:
	  #print i
    ##------
    #conferencia.crear_articulo()
    #for i in conferencia.lista_articulos:
	  #print i
	##.------------------------
   

#    
#     
#     
#    def Filtrar_empatados(self, N):
#        """ Metodo : Filtrar_empatados
#       Parametros : self 
#              int n 
#       Descripcion; dado n, el max de articulos admitidos por el CLEI, se
#              se filtran los articulo de Lista_Articulos, para elegir
#              aquellos con mejores puntuaciones, los que quedaban eran candidatos
#              a ser admitidos y estaban empatados y cabian todos
#              en esa lista, son los que pertencen a la lista empatados
#        """
#        empatados=[]
#        
#        a = self.Filtrar_admitidos(N)
#        #si la lista de admitidos no se lleno, generamos la de empatados
# 
#        if len(a) != N:
#                      
#            # se colocan en Lista Ordenada , los articulos aceptables de mayor
#            # a menor puntaje
#            Lista_Ordenada = self.Ordenar_Articulos()
#            # colocamos en una lista el resto de articulos que no fueron admitidos todavia
#            # (articulos luego del ultimo que fue a la lista de admitidos)
#            No_admitidos= Lista_Ordenada[len(a):len(Lista_Ordenada)]
#            #buscamos el promedio del primero que estaba empatado
#            if len(a) < len(Lista_Ordenada):
#        	indice = Lista_Ordenada[len(a)].Puntaje_promedio
#        	#todos los articulos en la lista de no admitidos con este indice
#        	# lo agregamos a la lista de empatados
#        	for i in No_admitidos:
#        	    if i.Puntaje_promedio == indice:
#        		empatados.append(i)
#        return [a,empatados]        
#        
#        
#    
#    def Generar_Listas(self, num):
#        """ Metodo : Generar_Listas
#       Parametros : self 
#              int n 
#       Descripcion; dado n, el max de articulos admitidos por el CLEI, se
#              generan la lista de articulos admitidos y empatados
#        """
#        if num >= 0:
#            q = self.Filtrar_empatados(num)
 #           l = []
 #           print('Lista de Articulos Admitidos:')
 #           if len(q[0]) != 0: 
 #             for i in q[0]:
 #       	    print 'id_articulo:', str(i.id_articulo) , ',' , ' Titulo:' ,  i.Titulo, ',' ,' Topico:',i.Topico.Nombre
 #       
 #           l = []
 #           print('\nLista de Articulos Empatados: ')
 #           if len(q[1]) != 0: 
 #             for i in q[1]:
 #       	    print('id_articulo:'+ str(i.id_articulo) +','+ ' Titulo:'+  i.Titulo+',' +' Topico:'+i.Topico.Nombre)
 #         
 #           return True
 #       else:
 #           return False
 #         
         
