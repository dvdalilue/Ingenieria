'''
Created on 28/11/2013

@author: Audry Morillo 
         Michael Woo
'''
from funciones import Agregar_enOrden, articulos_por_aceptar
from excepciones import *

# Si una persona puede estar en el CLEI en mas de una modalidad,
# por que entonces no utilizar herencia multiple? y que Person herede de
# todos.
class Persona(object):
    def __init__(self, Nombre, Apellido, Institucion, Email, Pais):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Institucion = Institucion
        self.Email = Email
        self.Pais = Pais

    def __str__(self):
        return 'Nombre Completo: '+self.Nombre+' '+self.Apellido+'\n'+'Institucion: '+self.Institucion+'\n'

class Asistente(Persona):
    def __init__(self, Nombre, Apellido, Institucion, Email, Pais,
                 Direccion_Postal, Url, Telefono, Monto_Pago, Fecha_Inscripcion):
        super(Asistente, self).__init__(Nombre, Apellido, Institucion, Email, Pais)
        #Persona.__init__(Nombre, Apellido, Institucion, Email, Pais)
        self.Direccion_Postal = Direccion_Postal
        self.Url = Url
        self.Telefono = Telefono
        self.Monto_Pago = Monto_Pago
        self.Fecha_Inscripcion = Fecha_Inscripcion

    def __str__(self):
        return super(Asistente,self).__str__()+'Fecha de Inscripcion : '+self.Fecha_Inscripcion+'\n'

class ComitePrograma(Persona):
    def __init__(self, Nombre, Apellido, Institucion, Email, Pais,
                             Especialidad):
        super(ComitePrograma, self).__init__(Nombre, Apellido, Institucion, Email, Pais)
        self.Especialidad = Especialidad
        self.EsPresidente = False

    # Agregar en diagrama de clases
    def AsignarPresidencia(self):
        if(self.EsPresidente == False):
            self.EsPresidente = True

    # Evalua un articulo: Retorna True si la puntuacion es valida,
    #                                                          False si la puntuacion no es valida en el rango
    def EvaluarArticulo(self, Puntaje, Texto):
        if (Puntaje >= 1 and Puntaje <= 5):
            for eval in Texto.GetArbitraje():
                if eval[0] == self:
                    raise ExcepcionJurado("No puede evaluar el mismo articulo dos veces")
            Texto.SetArbitraje((self, Puntaje))
            return True
        else:
            return False

    def __str__(self):
        return super(ComitePrograma, self).__str__()+'Especialidad: '+self.Especialidad.__str__()+'\n'

class Articulo:
    def __init__(self, Autor, Titulo, Topico, Resumen, Texto, Palabras_Clave):
        self.Autor = Autor
        self.Titulo = Titulo
        self.Topico = Topico
        self.Resumen = Resumen
        self.Texto = Texto
        self.Palabras_Clave = Palabras_Clave
        # Los siguientes atributos son privados pues unicamente son necesarios
        # para la aceptacion de un articulo a la conferencia, no para ser utlizados
        # por cualquier otra rutina. OJO REVISAR.

        # Agregar en diagrama de clases
        self.__Arbitros = []
        # Agregar en diagrama de clases
        self.__Promedio_Puntuacion = 0

    # Agregar en diagrama de clases

    # Para llevar el control de las evaluaciones del articulo se utilizara una
    # lista con una dupla de la forma (Arbitro, Puntaje)
    def SetArbitraje(self, Evaluacion):
        self.__Arbitros.append(Evaluacion)

    def GetArbitraje(self):
        return self.__Arbitros

    def Promediar(self):
        self.__Promedio_Puntuacion = 0
        # Se calcula el promedio de puntaje del articulo
        for puntaje in self.__Arbitros:
            self.__Promedio_Puntuacion += puntaje[1]
        self.__Promedio_Puntuacion /= len(self.__Arbitros)

    def GetPromedio(self):
        return self.__Promedio_Puntuacion

    def Evaluar(self):
        self.Promediar()
        # NOTA: Falta ver como hacer que los punto flotante solo tengan de
        #             precision 2 decimales. Igual preguntar a profesores si,
        #                efectivamente se manejaran 2 decimales.
        if (self.__Promedio_Puntuacion >= 3.00 and len(self.__Arbitros) >= 2):
            # Funcion para agregar por orden descendente de puntaje los articulos
            # a la lista de articulos que estan pendientes por aceptacion.
            # Facilita la eleccion de articulos aceptados y empatados.
            Agregar_enOrden(articulos_por_aceptar, self)
            
    # No se implemento un setAutor y se dejo que fuese un parametro de entrada
    # en el constructor debido a que de esta forma no se permite que exista
    # algun metodo que pueda cambiar de autor de un articulo a conveniencia, es
    # decir, a un articulo unicamente se le asociara un autor cuanto una
    # instancia de el sea creada.

    def __str__(self):
        return 'Titulo: '+self.Titulo+' \n'+self.Autor.__str__()+'Palabras claves: '+self.Palabras_Clave.__str__()+'\n'