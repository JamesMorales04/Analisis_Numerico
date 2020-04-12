import sympy as sp
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
    def derivar(self,entrada):
    	x = sp.Symbol('x')
    	derivada = sp.diff(self.funcion,x)
    	return derivada
    def parse(self,entrada):
    	function=parse_expr(entrada)
    	return function	




