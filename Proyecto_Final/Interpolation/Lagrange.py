import sympy as sym


class Lagrange:
    def __init__(self):
        self.xValues = []
        self.yValues = []
        self.LValues = []
        self.polynomial = 0
    
    def lagrange_interpol_algorithm(self,xVector,yVector):
        self.xValues = xVector
        self.yValues = yVector
        x = sym.Symbol('x')

        phases = len(xVector)
        numerator = 1
        denominator
        for i in range(phases):

            for j in range(phases):
                if(j!=i):
                    numerator = numerator*(x-self.xValues[j])
                    denominator = denominator*(self.xValues[i]-self.xValues[j])
            
            self.LValues.append(numerator/denominator)
            self.polynomial += self.LValues[i]*self.yValues[i]

        self.polynomial = sym.exapand(self.polynomial)
