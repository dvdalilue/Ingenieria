'''
Created on 28/11/2013

@author: Audry Morillo
         Michael Woo
'''
from __future__ import division
from sys import exit
from clases import *
from funciones import *

global comite_programa, articulos
comite_programa = []
articulos = []

def ImprimirOpciones():
    print '''\nOpciones disponibles:
             1- Crear articulo.
             2- Crear miembro del comite programa.
             3- Listar miembros del comite programa.
             4- Asignar presidente del comite programa.
             5- Asignar puntuacion a un articulo.
             6- Listar articulos.
             7- Calcular promedio de puntuacion de un articulo.
             8- Seleccionar articulos.
             9- Salir del programa.
             0- Mostrar esta ayuda.\n'''
  
def CrearArticulo():
    print '\nDatos sobre el autor: \n'
    nombre = raw_input("Nombre: ")
    apellido = raw_input("Apellido: ")
    institucion = raw_input("Insitucion: ")
    email = raw_input("Correo electronico: ")
    pais = raw_input("Pais de procedencia: ")
    autor = Persona(nombre, apellido, institucion, email, pais)
    
    print '\nDatos del articulo: \n'
    titulo = raw_input("Titulo: ")
    topico = raw_input("Topico: ")
    resumen = raw_input("Resumen: ")
    texto = raw_input("Texto: ")
    pclaves = raw_input("Palabras clave: ")
    articulos.append(Articulo(autor,titulo,topico,resumen,texto,pclaves))
    
def CrearComitePrograma():
    print '\nDatos sobre el miembro: \n'
    nombre = raw_input("Nombre: ")
    apellido = raw_input("Apellido: ")
    institucion = raw_input("Insitucion: ")
    email = raw_input("Correo electronico: ")
    pais = raw_input("Pais de procedencia: ")
    especialidad = raw_input("Especialidad: ")
    comite_programa.append(ComitePrograma(nombre,apellido,institucion,email,pais,especialidad))   
    
def ListarElementos(lista):
    i = 0
    for elem in lista:
        print i.__str__()+"- "+elem.__str__()
        i += 1
    
def ObtenerOpcion():
    opcion = input("Ingrese una opcion: ")
    #Crear un articulo
    if(opcion == 1):
        CrearArticulo()
    #Crear miembro del comite programa
    if(opcion == 2):
        CrearComitePrograma()
    #Listar miembros del comite programa
    if(opcion == 3):
        ListarElementos(comite_programa)
    #Asignar presidente del comite programa
    if(opcion == 4):
        tienePresidente = False
        for elem in comite_programa:
            if(elem.EsPresidente == True):
                print "\nEl comite ya posee presidente.\n"
                tienePresidente = True
                break
        if(tienePresidente == False):        
            print "\nLos miembros del comite programa son:\n"
            ListarElementos(comite_programa)
            presidente = input("Indique el numero de quien sera presidente del comite: ")
            while(presidente >= len(comite_programa) or presidente < 0):
                presidente = input("Elija un miembro dentro del rango de disponibles: ")
            comite_programa[presidente].AsignarPresidencia()
    #Asignar puntuacion a un articulo
    if(opcion == 5):
        try:
            print "\nLos articulos disponibles a evaluar son:\n"
            ListarElementos(articulos)
            articulo = input("Indique que articulo se evaluara: ")
            while(articulo >= len(articulos) or articulo < 0):
                articulo = input("Elija un articulo dentro del rango de disponibles: ")
                
            print "\nMiembros del comite programa: "
            ListarElementos(comite_programa)
            evaluador = input("Indique que miembro del comite programa evaluara el articulo: ")
            while(evaluador >= len(comite_programa) or evaluador < 0):
                evaluador = input("Elija un miembro dentro del rango de disponibles: ")
            nota = input("Indique la nota asignada: ")
            if (comite_programa[evaluador].EvaluarArticulo(nota,articulos[articulo]) == False):
                print "\nLa nota asignada debe estar entre 1 y 5."
        except ExcepcionJurado:
            print "\nUn jurado no puede evaluar un mismo articulo dos veces.\n"
    #Listar articulos
    if(opcion == 6):
        ListarElementos(articulos)
    #Calcular promedio de puntuacion de un articulo
    if(opcion == 7):
        print "\nLos articulos disponibles son:\n"
        ListarElementos(articulos)
        articulo = input("Indique el articulo al que se le calculara el promedio de puntuacion: ")
        while(articulo >= len(articulos) or articulo < 0):
            articulo = input("Elija un articulo dentro del rango de disponibles: ")
        articulos[articulo].Promediar()
        print "\nEl promedio es: "+articulos[articulo].GetPromedio().__str__()
    #Seleccionar articulos
    if(opcion == 8):
        try:
            aceptados = input("Indique el numero de articulos a aceptar: ")
            empatados = input("Indique el numero de articulos empatados permitidos: ")
            print "\nArticulos aceptados:\n"
            ListarElementos(Escoger_Aceptados(aceptados))
            print "\nArticulos empatados:\n"
            ListarElementos(Escoger_Empatados(aceptados,empatados))
        except ExcepcionListaAceptados:
            print "\nNo se puede elegir un numero de articulos mayor al numero de disponibles a aceptar.\n"
    #Finalizar la ejecucion del programa
    if(opcion == 9):
        exit()        
                
if __name__ == "__main__":
    while(True):
        ImprimirOpciones()
        ObtenerOpcion()