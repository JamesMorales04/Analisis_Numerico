import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class trapezium:
    def __init__(self):
        self.value= "null"

    def algorithm_trapezium(self, entry, xi,xs):
        initial= entry.evaluar(xi)
        print(initial)
        final  = entry.evaluar(xs)
        print(final)
        h=float(xs)-float(xi)
        self.value = (h/2)*(initial+final)
        return str(self.value)
"""
exp(x)-ln(x+4)
[1,1.3,1.5,1.8,2.3]
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[1,1.3,1.5,1.8,2.3])
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[2,3.1,4,5])

"""