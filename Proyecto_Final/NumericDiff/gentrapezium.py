import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class GenTrapezium:
    def __init__(self):     
        self.result = ''

    def general_trapezium_algorithm(self, entry, xi,xs,n):        
        if (int(n)==0):
            self.result= "No valid number"
            return self.result
        aux = float(xi)
        initY = entry.evaluar(xi)
        finalY = entry.evaluar(xs)
        xi=float(xi)
        xs=float(xs)

        h = (xs-xi)/float(n)
        self.arr = []
        summatory = 0
        for i in range(int(n)-1):
            aux+=h 
            val=entry.evaluar(aux)
            self.arr.append(val)
        for i in self.arr: 
            summatory+=i
        summatory = (h/2)*(initY+finalY+(2* summatory))
        self.result = summatory            
                
        return str(self.result)

    def get_Result(self):
        return str(self.result)

#exp(x)-ln(x+4) 5 5.8 y 19 Nice.