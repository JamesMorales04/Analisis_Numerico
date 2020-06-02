import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class NewtonInterpolation:
    def __init__(self):
        self.xn=""     #All the x values 
        self.result = ''

    def algorithm_newtonInterpolation(self, entry, xi,xs,h):
        xi = float(xi)
        xs = float(xs)
        initY = entry.evaluar(xi)
        finalY = entry.evaluar(xs)
        total = initY+finalY
        lastX = xi
        sumPar = 0
        sumImpar = 0
        count = 1
        for i in range(xi+h,xs,h):
            count+=1
            valY = entry.evaluar(i)
            if(count%2==0):
                sumPar+=valY
            else:
                sumImpar+=valY
        self.result=str(h/3*(total+4*sumPar+2*sumImpar))
    
    def get_Result(self):
        return self.result
"""
n= NewtonInterpolation()

exp(x)-ln(x+4)
[1,1.3,1.5,1.8,2.3]
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[1,1.3,1.5,1.8,2.3])
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[2,3.1,4,5])

"""