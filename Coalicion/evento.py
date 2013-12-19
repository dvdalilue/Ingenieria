#!/usr/bin/python
import datetime

class Eventos(object):
    
    def __init__(self, evento=None ):
        if evento is None:
            evento = []
        self.evento = evento


    def add(self,evento,diai, mesi, anioi, diaf, mesf, aniof, horai, mini, segi, horaf, minf, segf):
        fechai = datetime.date(anioi,mesi,diai)
        fechaf = datetime.date(aniof,mesf,diaf)
        horai = datetime.time(horai,mini,segi)
        horaf = datetime.time(horaf,minf,segf)
        
        self.evento.append([evento,fechai, fechaf, horai,horaf])
        
    def __str__(self):
        return str(self.evento)