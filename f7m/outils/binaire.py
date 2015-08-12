# -*- coding:utf-8 -*-

class binaire(object):
    """
    Objet binaire avec addition et soustraction.
    Entrée/sortie sous forme de string. Manipulation interne en base 10.
    """
    minN=8
    def __init__(self,b):
        self.b=eval("0b"+b)
    def __repr__(self):
        t=bin(self.b)[2:]
        s=self.minN-len(t)
        if s>0:
            t=s*str(0)+t
        return t
    @property
    def base10(self):
        return self.b
    @base10.setter
    def base10(self,b):
        self.b=b
        
    def __add__(self,b):
        t=self.b+b.b
        s=binaire("0")
        s.b=t
        return s
    
    def __sub__(self,b):
        t=self.b-b.b
        if t<0:
            raise Exception("Hum... Je ne sais pas quoi faire avec les nombres plus petits que zéro.")
        s=binaire("0")
        s.b=t
        return s    
