import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from Functions import *
class gensimpson3:
    def __init__(self):
        self.result = ''

    def algorithm_gensimpson3(self, entry, xi,xs,n):
        self.arr=[]     #All the fxn values 
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
        sumEven=0
        sumUneven=0
        for i in range(int(n)-1):
            aux+=h 
            val=entry.evaluar(aux)
            self.arr.append(val)
        for i in self.arr:
            if (count%2==1): #Arr starts in 1 looking at excel, I think.
                sumEven+=i
            else:
                sumUneven+=i
            count+=1
        self.result= (h/3)*(initY+finalY+4*sumEven+2*sumUneven)

        return str(self.result)

    def get_Result(self):
        return self.result
"""

exp(x)-ln(x+4)
[1,1.3,1.5,1.8,2.3]
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[1,1.3,1.5,1.8,2.3])
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[2,3.1,4,5])

"""