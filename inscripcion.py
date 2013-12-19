import 

class asistente(object):

    def __init__(self, cod, tel, url, asist, desc):

        self.asistencia = asist
        self.cod_postal = cod
        self.telefono = tel
        self.url = url
        self.desc = desc

    def calcularPrecioInsc(self, monto):

        return self.desc*monto
