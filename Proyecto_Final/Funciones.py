import sympy
from sympy.parsing.sympy_parser import parse_expr

class Funciones:
    def __init__(self,entrada):
        self.funcion=parse_expr(entrada)
    def evaluar(self,valor):
        return  self.funcion.evalf(subs=dict(x=valor))
