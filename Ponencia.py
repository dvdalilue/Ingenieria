#*****************************************************************************
# Clase : Ponencia
#
# Descripcion : Clase que implementa las exposiciones sobre articulos en el
#               evento CLEI
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************

class Ponencia(object):
  def __init__(self, expositor, articulo_a_presentar, ubicacion, topico):
    """Constructor"""
    self.expositor = expositor
    self.articulo_a_presentar = articulo_a_presentar
    self.ubicacion = ubicacion
    self.topico = topico
