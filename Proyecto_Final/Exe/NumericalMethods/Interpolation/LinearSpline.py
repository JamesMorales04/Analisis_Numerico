from decimal import *
import numpy as np
from sympy import *
import math

class LinearSpline:
    def __init__(self):
        self.x = []
        self.y = []
        self.result = []
        self.rows = []
        self.total = []

    def algorithm_linearSpline(self, xi, yi):
        deno = 0.0
        self.x = xi[0]
        self.y = yi[0]
        if len(self.x) <= 0 or self.x is None:
            self.result.append("No x values")
        elif len(self.y) <= 0 or self.y is None:
            self.result.append("No f(x) values")
        elif len(self.x) != len(self.y):
            if len(self.x) > len(self.y):
                self.result.append("You need more F(x) values or maybe you put more X values than you need")
            else:
                self.result.append("You need more X values or maybe you put more F(x) values than you need")
        else:
            for i in range(1,len(self.x)):
                deno = (self.x[i] - self.x[i-1])
                if deno != 0:
                    pendiente = (self.y[i] - self.y[i-1])/deno
                    resultado = (pendiente * - self.x[i]) + self.y[i]
                    #print("P(X" + str(i) + ") = " + str(pendiente) + "X + " + str(resultado) + "        " + str(self.x[i-1]) + " <= X <= " + str(self.x[i]))
                    self.result.append(["P(X" + str(i) + ") = " + str(pendiente) + "X + " + str(resultado), str(self.x[i-1]) + " <= X <= " + str(self.x[i])])
                else:
                    self.result.append(["Div by 0","please, check your values"])

    def value_table(self):
        return self.result

    def get_results(self):
        results=""
        aux=1
        for i in self.result:
            results+=f""+(str)(i[0])+"\n"
            aux+=1
        return results

    def check_values(self, ar,br):
        if not ar or not br:
            return False
        elif len(ar[0]) != len(br[0]):
            return False
        arr = ar[0]
        arr.sort()
        iter = 1
        for i in arr:
            if i != arr[iter] and i != 0 and iter != (len(arr)-1):
                iter += 1
            elif iter != (len(arr)-1):
                return True
            else:
                return True