'''
Created on 02/12/2013

@author: Audry Morillo M
         Michael Woo
'''
# Excepcion que ocurre cuando se solicita un numero mayor de articulos a aceptar
# que los disponibles que hay en sistema
class ExcepcionListaAceptados(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return self.valor.__str__()
    
# Excepcion que ocurre cuando un mismo jurado vota por un mismo articulo
class ExcepcionJurado(Exception):
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return self.valor.__str__()