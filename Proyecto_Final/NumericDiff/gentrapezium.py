import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class GenTrapezium:
    def __init__(self):
        self.xn=""     #All the x values 
        self.result = ''

    def general_trapezium_algorithm(self, entry, xn,h):
        self.matrix = []
        self.xn= xn[0]
        length= len(self.xn)
        try:
            if(length!=0 and h!=0):
                initY = entry.evaluar(xn[0])
                finalY = entry.evaluar(xn[-1])
                sumVals = initY + finalY
                for i in range (1,len(xn)-1):
                    sumVals+=entry.evaluar(xn[i])
                self.result = src(h/2*sumVals)
            else:
                self.result = 'Error: Invalid entries'
        except Exception as e:
            print(e)
            self.result = 'Error: Invalid entries'
    def get_Result(self):
        return self.result