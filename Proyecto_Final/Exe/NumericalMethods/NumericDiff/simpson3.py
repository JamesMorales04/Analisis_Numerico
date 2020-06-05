import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class Simpson13:
    def __init__(self):
        self.result = ''

    def simpson_13_algorithm(self, entry, xi,xs,n):
        xi  =float(xi)
        xs  =float(xs)      
        if (xs<xi):
            self.result= "Not a valid xi and xs"
            return self.result               
        h=(xs-xi)/3
        initY = entry.evaluar(xi)
        finalY = entry.evaluar(xs)
        middle = (xs+xi)/2
        middleY = entry.evaluar(middle)
        self.result = h/3*(initY+finalY+4*middleY)
        return str(self.result)

    def get_Result(self):
        return str(self.result)