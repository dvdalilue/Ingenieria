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
    
    def aniadir_miembro(self, CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experiencia=None, Url=None):    
        """ Metodo : Aniadir_Miembro
        Parametros : self 
        int CI 
        string Nombre , Apellido , Institucion_Afiliada , Email, Pais, Cargo, Experiencia
        Descripcion; dado los atributos de un miembro, se crea y se agrega al arreglo
        correspondiente a los miembros del CP
        """
        for n in self.miembros_cp:
            if n.ci == CI:
                print('Ya existe un miembro con esa CI') 
                return False

        Miembro = MiembroCp(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Experiencia, Url)
      
        # se verifica que no se agregue dos veces al mismo miembro
        self.miembros_cp.append(Miembro)
        return True     
     
    def aniadir_articulo(self, Id_Articulo, Titulo, Autor, Palabras_Claves, Topico, Texto, Resumen):
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
        for n in self.lista_articulos:
            if n.id_articulo == Id_Articulo:
                print('Ya existe este articulo')
                return False

        articulo = Articulo(Id_Articulo, Titulo, Autor, Palabras_Claves, Topico, Texto, Resumen)
        
        #se verifica que no se agreguen dos veces el mismo articulo

        self.lista_articulos.append(articulo)
        return True
    
    def Crear_Comite(self):
        """ 
        Metodo : Crear_Comite
       Parametros : self 
       Descripcion; pide al usuario los datos necesarios para crear
              los miembros del comite de programa y agregarlos
              al arreglo miembros_cp
        """
      
        var = int(raw_input('desea agregar un miembro al comite? \n1. Si \n2. No\n'))
        os.system("clear")
        # mietras el usuario quiera agregar miembros al comite, se pediran
        # los datos pertienentes para crearlos
        while (1 == var):
            CI = int(raw_input('introduzca la cedula de identidad: '))
            i = 0
            # se espera que el usuario coloque un CI que no exista en el sistema
            while(i < len(self.miembros_cp)):
                if CI == self.miembros_cp[i].CI:
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
        return self.miembros_cp
    
    def elegir_PresidenteCP(self):
        """  Metodo : elegir_PresidenteCP
        Parametros : self
        Descripcion: Cambia el cargo de una miebro a presidente del CP, si todavia no
        existe uno"""
        for i in self.miembros_cp:
            if i.presidente == True:
                print ('Lo siento, ya existe un presidente')
                return False
        id_miembro_cp = int(raw_input('introduzca la cedula de identidad del miembro que eligio de presidente: '))
        
        # se espera que el usuario coloque un CI que no exista en el sistema
        for i in self.miembros_cp:
            if id_miembro_cp == i.ci:
                i.set_presidente()
                return True
        return False

if __name__=="__main__":
    
    comite = CLEI()
    comite.aniadir_miembro(1,"jose","perez","usb","d@g.com","Ven")
    print comite.miembros_cp[0]
    #comite.elegir_PresidenteCP()
    #print comite.miembros_cp[0]
    comite.aniadir_articulo(1,"titulo","autor",["pal","cla"],"bd","texto","resumen")
    print comite.lista_articulos[0]
    
#    def Crear_Articulo(self):
#        """ Metodo : Crear_Articulo
#       Parametros : self 
#       Descripcion; pide al usuario los datos necesarios para crear
#              los articulos que quieren ser presentados en el CLEI
#        """
#        Titulo = raw_input('Titulo del Articulo: ')
#        Palabras_Claves = []
#        Topico = raw_input('Topico: ')
#        CI = int(raw_input('CI del Autor: '))
#        Nombre = raw_input('Nombre del Autor: ')
#        Apellido = raw_input('Apellido del Autor: ')
#        Institucion_Afiliada= raw_input('Institucion Afiliada del Autor: ')
#        Email= raw_input('Email del Autor: ')
#        Pais= raw_input('Pais del Autor: ')
#        Asistente = False
#        Ponente = False
#        Autor = True
#        Cod_Postal= int(raw_input('Codigo postal del Autor: '))
#        Url= raw_input('Url del Autor: ')
#        Telefono= raw_input('Telefono: ')
#        Autor = Asistente(CI, Nombre, Apellido, Institucion_Afiliada, Email, Pais, Cod_Postal, Telefono, Ponente, Autor, Url)
#        if (self.Aniadir_Articulo(self.id_articulo, Titulo, Autor, Palabras_Claves, Topic)):
#            print('Articulo Agregado')
#            self.id_articulo = self.id_articulo + 1
#    
#    
#    def Realizar_Votacion(self, cod_articulo, CI_miembro_cp, puntaje):
#        """ Metodo : Realizar_Votacion
#       Parametros : self 
#              int cod_articulo , CI_miembro_cp , puntaje
#       Descripcion; se verifica que la persona que vote sea un miembro de cp
#              y luego califica el articulo 
#        """
#        for Miembro in self.miembros_cp:
#            if Miembro.CI == CI_miembro_cp:
#                Juez = Miembro
#                for Articulo in self.Lista_Articulos:
#                    if Articulo.id_articulo == cod_articulo:
#                        return Articulo.Calificar(Juez, puntaje)
#        print('usted no es miembro del comite ')
#        return False
#    
#    def Ordenar_Articulos(self):   
#        """ Metodo : Ordenar_Articulos
#       Parametros : self 
#       Descripcion; toma todos los articulos de Lista_Articulos, verifica
#       cuales tienen un promedio mayor o igual a 3 y los agrega a la
#       lista de aceptables. Luego toma esa lista y las ordena de mayor 
#       a menor puntaje
#        """
#        self.aceptables = []
#        for articulo in  self.Lista_Articulos:
#            if articulo.verificar_Aceptable():
#                self.aceptables.append(articulo)
#        Lista_Ordenada = sorted(self.aceptables, key=lambda aceptable: aceptable.Puntaje_promedio, reverse=True) 
#        return Lista_Ordenada
# 
#    
#    def Filtrar_admitidos(self, n):
#        """ Metodo : Filtrar_admitidos
#       Parametros : self 
#              int n 
#       Descripcion; dado n, el max de articulos admitidos por el CLEI, se
#              se filtran los articulo de Lista_Articulos, para elegir
#              aquellos con mejores puntuaciones (si el numero
#              de empatados supera el valor de n, no se colocan
#              en la lista de admitidos)
#        """
#        admitidos= []
#        # se colocan en Lista Ordenada , los articulos aceptables de mayor
#        # a menor puntaje
#        Lista_Ordenada = self.Ordenar_Articulos()
#       
#        while n > 0:
#        #si n es menor al numero de articulos aceptables, debemos elegir cuales tomar
#            if n < len(Lista_Ordenada):
#        # si el ultimo articulo no esta empatado con el siguiente, tomamos los n primeros
#        # articulos de la lista de articulos aceptables
#                if Lista_Ordenada[n-1].Puntaje_promedio !=  Lista_Ordenada[n].Puntaje_promedio:
#                    admitidos = Lista_Ordenada[0:n]
#                    return admitidos
#                #sino restamos uno, hasta encontrar un articulo que no este empatado con ninguno de
#                # los que no hemos admitido
#                else:
#                    if n > 0:
#                        n = n - 1
#            #si n es mayor o igual a numero de articulos aceptables        
#            else:
#        # admitidos sera igual a aceptables
#                admitidos = Lista_Ordenada
#                return admitidos
#                
#        return admitidos
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
         
