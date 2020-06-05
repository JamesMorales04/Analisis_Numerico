import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class trapezium:
    def __init__(self):
        self.result= "null"

    def algorithm_trapezium(self, entry, xi,xs):
        xi  =float(xi)
        xs  =float(xs)      
        if (xs<xi):
            self.result= "Not a valid xi and xs"
            return self.result     
        initial= entry.evaluar(xi)
        final  = entry.evaluar(xs)
        h=xs-xi
        self.result = (h/2)*(initial+final)
        return str(self.result)
        
    def get_Result(self):
        return str(self.result)
"""
exp(x)-ln(x+4)
[1,1.3,1.5,1.8,2.3]
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[1,1.3,1.5,1.8,2.3])
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[2,3.1,4,5])

"""