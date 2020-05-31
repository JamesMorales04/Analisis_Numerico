import numpy as np
import string
from sympy import *
import math
class QuadraticSpline:
    def __init__(self):
        self.functions = []
        self.functionsValues = []
        self.constants = []
        self.constantsUseds = []
        self.px = []
        self.rows = []
        self.x = Symbol('x')
        self.result = []
    def algorithm_quadratic_spline(self,xVal,yVal):
        x = xVal[0]
        y = yVal[0]
        points = []
        intervals = []
        alf = list(string.ascii_lowercase) #From a to z
        for i in alf:
            for j in range(1,3):
                s = symbols(str(i)+str(j))
                self.constants.append(s)
        for p in range(len(x)):
            print([x[p],y[p]])
            points.append([x[p],y[p]])
        for i in range(1,len(x)):
            intervals.append([points[i-1][0],points[i][0]])
        dicPoints = dict(points)
        
        print(dicPoints)

    def value_table(self):
        return self.result

    def get_results(self):
        results=""
        aux=1
        for i in self.result:
            results+=f""+(str)(i[0])+"\n"
            aux+=1
        return results