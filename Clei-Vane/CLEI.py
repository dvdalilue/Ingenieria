#*****************************************************************************
# Clase : CLEI.py
#
# Descripcion : Clase que implementa los Articulos a presentar en el CLEI
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************
from Persona import Inscrito, Miembro_Cp
from Articulo import Articulo
from Topico import Topico
import os

class CLEI(object):
    

    def __init__(self):
        """Constructor"""
        self.Lista_Articulos = []
        self.Miembros_Cp = []
        self.Aceptables = []
        self.Admitidos = []
        self.Empatados=[]
        self.Id_Articulo=0        # variable global que se utilizara para identifica univocamente los articulos
    
    def Aniadir_Miembro(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experiencia):    
        """ Metodo : Aniadir_Miembro
       Parametros : self 
             int CI 
             string Nombre , Apellido , Institucion_Afiliada , Email, Pais, Cargo, Experiencia
       Descripcion; dado los atributos de un miembro, se crea y se agrega al arreglo
              correspondiente a los miembros del CP
      """
        Miembro= Miembro_Cp(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experiencia)
      
    # se verifica que no se agregue dos veces al mismo miembro
        for n in self.Miembros_Cp:
            if n.CI == Miembro.CI:
                print('ya existe un miembro con esa CI') 
                return False
        self.Miembros_Cp.append(Miembro)
        return True
     
     
    def Aniadir_Articulo(self,ID, Titulo, Autor, Palabras_Claves, Topico):
        """ Metodo : Aniadir_Miembro
       Parametros : self 
             int id
             string Titulo
             Autor Autor
             string[] Palabras_Claves
             Topico[] Topico
       Descripcion; dado los atributos de un articulo, se crea y se agrega al arreglo
              de articulos
      """
        articulo = Articulo(ID,Titulo, Autor, Palabras_Claves, Topico)
        
        #se verifica que no se agreguen dos veces el mismo articulo
        for n in self.Lista_Articulos:
            if n.Id_Articulo == articulo.Id_Articulo:
                print('ya existe este articulo')
                return False
        self.Lista_Articulos.append(articulo)
        return True
    
     
    def Crear_Comite(self):
        """ 
        Metodo : Crear_Comite
       Parametros : self 
       Descripcion; pide al usuario los datos necesarios para crear
              los miembros del comite de programa y agregarlos
              al arreglo Miembros_Cp
        """
      
        var = int(raw_input('desea agregar un miembro al comite? \n1. Si \n2. No\n'))
        os.system("clear")
        # mietras el usuario quiera agregar miembros al comite, se pediran
        # los datos pertienentes para crearlos
        while (1 == var):
            CI = int(raw_input('introduzca la cedula de identidad: '))
            i = 0
            # se espera que el usuario coloque un CI que no exista en el sistema
            while(i < len(self.Miembros_Cp)):
                if CI == self.Miembros_Cp[i].CI:
                    os.system("clear")
                    CI = int(raw_input('esta cedula de identidad ya esta registrada\nintroduzca la cedula de identidad: '))
                    i = 0
                else:
                    i = i + 1
            Nombre = raw_input('Nombre: ')
            Apellido = raw_input('Apellido: ')
            Institucion_Afiliada = raw_input('Institucion Afiliada: ')
            Email = raw_input('Email: ')
            Pais = raw_input('Pais: ')
            Experiencia = []
            var1 = int(raw_input("desea agregar un tema de experiencia? \n1. Si \n2. No\n"))
            os.system("clear")
            while(var1 == 1): 
                Experiencia.append(raw_input("Topico: "))
                var1 = int(raw_input("desea agregar un nuevo tema de experiencia? \n1. Si \n2. No\n"))
                os.system("clear")
            if (self.Aniadir_Miembro(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experiencia)):
                print('Miembro agregado')
            
            var = int(raw_input("desea agregar un miembro al comite? \n1. Si \n2. No\n"))
            os.system("clear")
        return self.Miembros_Cp
    
    def elegir_PresidenteCP(self):
        """  Metodo : elegir_PresidenteCP
        Parametros : self
        Descripcion: Cambia el cargo de una miebro a presidente del CP, si todavia no
        existe uno"""
        for i in self.Miembros_Cp:
            if i.Cargo== 'Presidente':
                print ('Lo siento, ya existe un presidente')
                return False
        id_miembro_cp = int(raw_input('introduzca la cedula de identidad del miembro que eligio de presidente: '))
        
        # se espera que el usuario coloque un CI que no exista en el sistema
        for i in self.Miembros_Cp:
            if id_miembro_cp == i.CI:
                i.set_Cargo('Presidente')
                return True
        return False
    
    
    def Crear_Articulo(self):
        """ Metodo : Crear_Articulo
       Parametros : self 
       Descripcion; pide al usuario los datos necesarios para crear
              los articulos que quieren ser presentados en el CLEI
        """
        Titulo= raw_input('Titulo del Articulo: ')
        Palabras_Claves= []
        Tema= raw_input('Topico: ')
        Topic= Topico(Tema)
        CI = int(raw_input('CI del Autor: '))
        Nombre = raw_input('Nombre del Autor: ')
        Apellido = raw_input('Apellido del Autor: ')
        Institucion_Afiliada= raw_input('Institucion Afiliada del Autor: ')
        Email= raw_input('Email del Autor: ')
        Pais= raw_input('Pais del Autor: ')
        Asistente = False
        Ponente = False
        Autor = True
        Cod_Postal= int(raw_input('Codigo postal del Autor: '))
        Url= raw_input('Url del Autor: ')
        Telefono= raw_input('Telefono: ')
        Autor= Inscrito(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Asistente, Ponente, Autor, Cod_Postal, Url, Telefono)
        if (self.Aniadir_Articulo(self.Id_Articulo, Titulo, Autor, Palabras_Claves, Topic)):
            print('Articulo Agregado')
            self.Id_Articulo = self.Id_Articulo + 1
    
    
    def Realizar_Votacion(self, cod_articulo, CI_miembro_cp, puntaje):
        """ Metodo : Realizar_Votacion
       Parametros : self 
              int cod_articulo , CI_miembro_cp , puntaje
       Descripcion; se verifica que la persona que vote sea un miembro de cp
              y luego califica el articulo 
        """
        for Miembro in self.Miembros_Cp:
            if Miembro.CI == CI_miembro_cp:
                Juez = Miembro
                for Articulo in self.Lista_Articulos:
                    if Articulo.Id_Articulo == cod_articulo:
                        return Articulo.Calificar(Juez, puntaje)
        print('usted no es miembro del comite ')
        return False
    
    def Ordenar_Articulos(self):   
        """ Metodo : Ordenar_Articulos
       Parametros : self 
       Descripcion; toma todos los articulos de Lista_Articulos, verifica
       cuales tienen un promedio mayor o igual a 3 y los agrega a la
       lista de aceptables. Luego toma esa lista y las ordena de mayor 
       a menor puntaje
        """
        self.Aceptables = []
        for articulo in  self.Lista_Articulos:
            if articulo.verificar_Aceptable():
                self.Aceptables.append(articulo)
        Lista_Ordenada = sorted(self.Aceptables, key=lambda aceptable: aceptable.Puntaje_promedio, reverse=True) 
        return Lista_Ordenada

    
    def Filtrar_Admitidos(self, n):
        """ Metodo : Filtrar_Admitidos
       Parametros : self 
              int n 
       Descripcion; dado n, el max de articulos admitidos por el CLEI, se
              se filtran los articulo de Lista_Articulos, para elegir
              aquellos con mejores puntuaciones (si el numero
              de empatados supera el valor de n, no se colocan
              en la lista de admitidos)
        """
        Admitidos= []
        # se colocan en Lista Ordenada , los articulos aceptables de mayor
        # a menor puntaje
        Lista_Ordenada = self.Ordenar_Articulos()
       
        while n > 0:
        #si n es menor al numero de articulos aceptables, debemos elegir cuales tomar
            if n < len(Lista_Ordenada):
        # si el ultimo articulo no esta empatado con el siguiente, tomamos los n primeros
        # articulos de la lista de articulos aceptables
                if Lista_Ordenada[n-1].Puntaje_promedio !=  Lista_Ordenada[n].Puntaje_promedio:
                    Admitidos = Lista_Ordenada[0:n]
                    return Admitidos
                #sino restamos uno, hasta encontrar un articulo que no este empatado con ninguno de
                # los que no hemos admitido
                else:
                    if n > 0:
                        n = n - 1
            #si n es mayor o igual a numero de articulos aceptables        
            else:
        # admitidos sera igual a aceptables
                Admitidos = Lista_Ordenada
                return Admitidos
                
        return Admitidos
     
     
    def Filtrar_Empatados(self, N):
        """ Metodo : Filtrar_Empatados
       Parametros : self 
              int n 
       Descripcion; dado n, el max de articulos admitidos por el CLEI, se
              se filtran los articulo de Lista_Articulos, para elegir
              aquellos con mejores puntuaciones, los que quedaban eran candidatos
              a ser admitidos y estaban empatados y cabian todos
              en esa lista, son los que pertencen a la lista empatados
        """
        Empatados=[]
        
	a = self.Filtrar_Admitidos(N)
	#si la lista de admitidos no se lleno, generamos la de empatados

	if len(a) != N:
	              
	    # se colocan en Lista Ordenada , los articulos aceptables de mayor
	    # a menor puntaje
	    Lista_Ordenada = self.Ordenar_Articulos()
	    # colocamos en una lista el resto de articulos que no fueron admitidos todavia
	    # (articulos luego del ultimo que fue a la lista de admitidos)
	    No_Admitidos= Lista_Ordenada[len(a):len(Lista_Ordenada)]
	    #buscamos el promedio del primero que estaba empatado
	    if len(a) < len(Lista_Ordenada):
		indice = Lista_Ordenada[len(a)].Puntaje_promedio
		#todos los articulos en la lista de no admitidos con este indice
		# lo agregamos a la lista de empatados
		for i in No_Admitidos:
		    if i.Puntaje_promedio == indice:
			Empatados.append(i)
	return [a,Empatados]        
        
        
    
    def Generar_Listas(self, num):
        """ Metodo : Generar_Listas
       Parametros : self 
              int n 
       Descripcion; dado n, el max de articulos admitidos por el CLEI, se
              generan la lista de articulos admitidos y empatados
        """
        if num >= 0:
            q = self.Filtrar_Empatados(num)
	    l = []
	    print('Lista de Articulos Admitidos:')
	    if len(q[0]) != 0: 
	      for i in q[0]:
		    print 'Id_Articulo:', str(i.Id_Articulo) , ',' , ' Titulo:' ,  i.Titulo, ',' ,' Topico:',i.Topico.Nombre
	    
	
	    l = []
	    print('\nLista de Articulos Empatados: ')
	    if len(q[1]) != 0: 
	      for i in q[1]:
		    print('Id_Articulo:'+ str(i.Id_Articulo) +','+ ' Titulo:'+  i.Titulo+',' +' Topico:'+i.Topico.Nombre)
	  
	    return True
        else:
	    return False
          
         
