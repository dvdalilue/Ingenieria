'''
Created on 28/11/2013

@author: Audry Morillo
         Michael Woo
'''
from excepciones import *
# Modulo de funciones para el sistema CLEI
# Articulos que se dividiran en la lista de articulos aceptados y empatados.
# Son articulos cuyo promedio es mayor a 3 y poseen al menos 2 arbitrajes.
global articulos_por_aceptar
articulos_por_aceptar = []

def Agregar_enOrden(lista, texto):
    #Caso Lista vacia o ultimo elemento de la lista
    if(lista == [] or lista[len(lista)-1].GetPromedio() > texto.GetPromedio()):
        lista.append(texto)
        return lista
    #Caso Lista no vacia
    for i in range(len(lista)):
        if(lista[i].GetPromedio() <= texto.GetPromedio()):
            lista.insert(i,texto)
            return lista

def Escoger_Aceptados(num_aceptados):
    aceptados = []
    if(num_aceptados > len(articulos_por_aceptar)):
        raise ExcepcionListaAceptados('El numero de articulos a aceptar es mayor que el de disponibles en sistema')
    for i in range(num_aceptados):
        aceptados.append(articulos_por_aceptar[i])
    return aceptados

# Se debe verificar si el numero de articulos empatados se especifica por
# usuario.
def Escoger_Empatados(num_aceptados, num_empatados):
    empatados = []
    if(num_aceptados+num_empatados > len(articulos_por_aceptar)):
        raise ExcepcionListaAceptados('El numero de articulos a aceptar es mayor que el de disponibles en sistema')
    else:
        puntaje = articulos_por_aceptar[num_aceptados].GetPromedio()
            
    for i in range(num_empatados):
        if(articulos_por_aceptar[num_aceptados+i].GetPromedio() == puntaje):
            empatados.append(articulos_por_aceptar[num_aceptados+i])
            
    return empatados