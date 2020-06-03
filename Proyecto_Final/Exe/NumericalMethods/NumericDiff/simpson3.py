import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class Simpson13:
    def __init__(self):
        self.polinomial=""
        self.xn=""     #All the x values 
        self.result = ''

    def simpson_13_algorithm(self, entry, xi,xs,h):
        initY = entry.evaluar(float(xi))
        finalY = entry.evaluar(float(xs))
        middleY = entry.evaluar(float(xi)+float(h))
        self.result = str(h/3*(initY+4*middleY+finalY))
        return str(self.result)

    def get_Result(self):
        return self.result