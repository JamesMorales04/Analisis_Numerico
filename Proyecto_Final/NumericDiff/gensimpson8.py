import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class GenSimpson38:
    def __init__(self):
        self.xn=""     #All the x values 
        self.result = ''

    def general_simpson38_algorithm(self, function, xi,xs,h):
        xi = float(xi)
        xs =float(xs)
        sumMultThree = 0
        sumNotMultThree = 0

        initY = function.evaluar(xi)
        finalY = function.evaluar(xs)

        sumTotal = initY+finalY
        counter = 1
        for i in range(xi+1,xs,h):
            counter+=1
            valY = function.evaluar(i)
            if(counter%3==0):
                sumMultThree+=valY
            else:
                sumNotMultThree+=valY
        
        self.result=str(3/8*h*(sumTotal+2*sumMultThree+3*sumNotMultThree))

    def get_Result(self):
        return self.result