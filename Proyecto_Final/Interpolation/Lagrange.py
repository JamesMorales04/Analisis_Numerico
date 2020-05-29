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
        denominator = 1
        for i in range(phases):

            for j in range(phases):
                if(j!=i):
                    numerator = numerator*(x - self.xValues[j])
                    denominator = denominator*(self.xValues[i]-self.xValues[j])
            
            self.LValues.append(numerator/denominator)
            print('Numerator')
            print(numerator)
            print('Denominator')
            print(denominator)
            self.polynomial += self.LValues[i]*self.yValues[i]
            numerator = 1
            denominator = 1

        #print(lagi.polynomial.evalf(subs=dict(x=-1)))
        #self.polynomial = self.polynomial.evalf(subs=dict(x=-1))


if __name__ == "__main__":
    X = [-4,-2,-1]
    Y = [-2.5962588,-0.6969583,0.9081217]

    lagi = Lagrange()
    lagi.lagrange_interpol_algorithm(X,Y)
    print(sym.expand(lagi.polynomial))
    #To evaluate
    #x = sym.Symbol('x')
    #print(lagi.polynomial.evalf(subs=dict(x=-1)))
    print(type(lagi.polynomial))
    pass
