import math

import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
class NewtonInterpolation:
    def __init__(self):
        self.Function=""
        self.xn=""     #All the x values 

    def algorithm_newtonInterpolation(self, xn, entry):

        matrix = []
        self.Function=parse_expr(entry)
        self.xn= xn
        length= len(xn)
        for i in range (length):
            matrix.append([0] * (length + 1))
            matrix[i][0] = self.xn[i]
            matrix[i][1] = self.evaluar(self.xn[i])

        polinomial = "P(X) = "+ str(matrix[0][1])

        for i in range(2,(length+1)): #  col and rows
            for j in range(i-1,length):
                matrix[j][i] = (matrix[j][i-1]-matrix[j-1][i-1])/(matrix[j][0]-matrix[j-i+1][0])
                if (j==i-1):
                    polinomial += " + "+ str(matrix[j][i])
                    for j in range (0,j): #j??
                        polinomial += "(x-" + str(matrix[j][0]) + ")"

        print(polinomial)
        print("---------------------------")
        print(matrix)





    def evaluar(self,valor):
        valores=self.Function.evalf(subs=dict(x=valor))
        try:
            aux=float(valores)
            if(isinstance(aux, float)):
                return valores
            else:
                return True
        except:
            return "Final"
    def value_table(self):
        return self.values
    def get_sol(self):
        return str(self.raiz)


n= NewtonInterpolation()

#n.algorithm_newtonInterpolation([1,1.3,1.5,1.8,2.3],"exp(x)-ln(x+4)")
n.algorithm_newtonInterpolation([2,3.1,4,5],"exp(x)-ln(x+4)")