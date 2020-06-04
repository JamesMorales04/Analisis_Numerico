import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class Simpson13:
    def __init__(self):
        self.polinomial=""
        self.xn=""     #All the x values 
        self.result = ''

    def simpson_13_algorithm(self, entry, xi,xs,n):
        h=(float(xs)-float(xi))/3
        initY = entry.evaluar(float(xi))
        finalY = entry.evaluar(float(xs))
        middle = (float(xs)+float(xi))/2
        middleY = entry.evaluar(middle)
        self.result = str(h/3*(initY+finalY+4*middleY))
        return str(self.result)

    def get_Result(self):
        return str(self.result)