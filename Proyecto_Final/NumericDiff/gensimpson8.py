import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class GenSimpson38:
    def __init__(self):
        self.result = ''

    def general_simpson38_algorithm(self, entry, xi,xs,n):
        self.arr=[]    
        if (int(n)<=0):
            self.result= "Not a valid number"
            return self.result       
        aux =float(xi)
        xi  =float(xi)
        xs  =float(xs)
        initY = entry.evaluar(xi)
        finalY = entry.evaluar(xs)
        h = (xs-xi)/float(n)
        count=0
        sumMultThree=0
        sumNotMultThree=0
        for i in range(int(n)-1):
            aux+=h
            val=entry.evaluar(aux)
            self.arr.append(val)  
        print(self.arr)
        for i in self.arr:
            count+=1
            if (count%3==0): 
                sumMultThree+=i
            else:
                sumNotMultThree+=i
        self.result= (3/8*h*(initY+finalY+2*sumMultThree+3*sumNotMultThree))
        return str(self.result)

    def get_Result(self):
        return self.result