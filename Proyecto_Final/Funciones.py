import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class Funciones:
    def __init__(self,entrada):
        self.funcion=parse_expr(entrada)
        self.derivar(self.funcion)

    def evaluar(self,valor):
        valores=self.funcion.evalf(subs=dict(x=valor))
        try:
            aux=float(valores)
            if(isinstance(aux, float)):
                return valores
            else:
                return True
        except:
            return "Final"
    def evaluar_derivada(self,valor):
        valores=self.derivada.evalf(subs=dict(x=valor))
        aux=float(valores)
        if(isinstance(aux, float)):
            return valores
        else:
            return True

    def derivar(self,entrada):
    	x = sp.Symbol('x')
    	self.derivada = sp.diff(entrada,x)
