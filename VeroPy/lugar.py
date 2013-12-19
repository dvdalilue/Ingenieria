#!/usr/bin/python

class Lugar(object):
    def __init__(self, influgares=None, lugares = None):
        if influgares is None:
            influgares = []
            lugares = []
        self.influgares = influgares
        self.lugares = lugares

    def add(self,nombre,ubicacion, capacidad):
        self.influgares.append([nombre,ubicacion, capacidad])
        self.lugares.append(nombre)

    def __str__(self):
        return str(self.influgares)

    def buscar(self, valor):
        if valor in self.lugares:
            print("el lugar esta creado")
        else:
            print("el lugar no existe")		