#*****************************************************************************
# Clase : Articulo.py
#
# Descripcion : Clase que implementa los Articulos a presentar en el CLEI
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************
from Persona import *

class Articulo:

    def __init__(self, id, titulo, autor, palabras_claves, 
                 topico, texto, resumen):
        
        """Constructor"""
        self.id_articulo = id
        self.titulo = titulo
        self.autor = autor
        self.palabras_claves = palabras_claves
        self.texto = self.texto
        self.resumen = self.resumen
        self.topico = topico
        self.jurado = []         # Arreglo de miembro_cp que evaluan el articulo
        self.aceptable = False   
        # es true si el puntaje promedio del articulo es mayor o igual a 3,00
        self.calificaciones = []   # almacena el voto de cada miembro de cp
        self.puntaje_promedio = 0
        
    def calificar(self, miembro_cp, puntuacion):
        """ Metodo : Calificar
       Parametros : self 
             Miembro_Cp  miembro_cp, 
             int  puntuacion (entero entre 1 y 5)
       Descripcion; dado un miembro del cp y una puntuacion se le asigna
                      esa calificacion al articulo
      """
    # se verifica que un miembro no vote mas de una vez
        if miembro_cp in self.jurado:
            print 'ya voto'
            return False
        
            # si la puntuacion es valida se alamacena en el 
            # arreglo de Calificaciones
            # y se registra el miembro que voto por el articulo 
            # en el arreglo Jurado
        if 0 < puntuacion <= 5:
            # and puntuacion <= 5:
            self.calificaciones.append(puntuacion)
            self.jurado.append(miembro_cp) 
            return True
            
        print('La calificacion no tuvo exito : puntaje invalido,'+ 
                                'debe ingresar un numero del 1 al 5,')
        return False
              
    def calcular_promedio(self):
        """ Metodo : calcular_promedio
       Parametros : self
       Descripcion; toma el arreglo de Calificaciones y suma cada uno de los
                       votos dividiendolo por el numero de votantes
      """
        self.puntaje_promedio = 0
        for n in self.calificaciones:
            self.puntaje_promedio += n

        if self.puntaje_promedio > 0:
            self.puntaje_promedio = (self.puntaje_promedio)/(float(len(self.calificaciones)))

    def verificar_aceptable(self):
        """ Metodo : verificar_Aceptable
        Parametros : self
        Descripcion; calcula el puntaje promedio de un articulo, si es mayor
        o igual a 3,00 coloca el atributo aceptable en True, 
        sino permanece False
        """
        if len(self.jurado) > 2:
            self.calcular_promedio()
            if self.puntaje_promedio >= float(3):
                self.aceptable = True
        return self.aceptable
        
            
    def __str__(self):
        """ Metodo : __str__
        Parametros : self
        Descripcion: imprime en un string los datos de un articulo
        """
        keys = self.__dict__.keys()
        datos = ""
        for n in keys:
            if n != 'Calificaciones' and n != 'id_Articulo' and n != 'Jurado':
                datos += "\n%s: %s"%(n,str(self.__dict__[n]))
        datos += "\n"
        return datos
    
#if __name__ =="__main__":

#art = Articulo(1,"Titulo1", "Pedro Perez", ["Palabra" ,"clave"], "bases de datos" )
#   print art
