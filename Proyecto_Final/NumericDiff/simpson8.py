
import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *

class Simpson38:

    def __init__(self):
        self.result = ''

    def simpson_38_algorithm(self,function,xi,xs):
        xi = float(xi)
        xs = float(xs)
        initY = function.evaluar(xi)
        finalY = function.evaluar(xs)
        h = (xs-xi)/4

        sumYs = initY+finalY+3*function.evaluar(xi+h)+3*function.evaluar(xi+2*h)

        self.result = str(h*3/8*sumYs)
        return str(self.result)
    
    def get_Result(self):
        return self.result