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

    def evaluar_derivada(self,valor):
        valores=self.derivada.evalf(subs=dict(x=valor))
        aux=float(valores)
        if(isinstance(aux, float)):
            return valores
        else:
            return True

    def derivar(self):
    	x = sp.Symbol('x')
    	self.derivada = sp.diff(self.funcion,x)


cosa= Funciones("x**2")
cosa.derivar()
cosa.evaluar(2)

