import sympy
from sympy.parsing.sympy_parser import parse_expr

class Funciones:
    def __init__(self,entrada):
        self.funcion=parse_expr(entrada)
    def evaluar(self,valor):
        valores=self.funcion.evalf(subs=dict(x=valor))
        aux=float(valores)
        if(isinstance(aux, float)):
            return valores
        else:
            return True





