from Functions import *
import math
class Newton:
    def __init__(self):
        self.values=[]
        self.raiz=""

    def algoritmo_newton(self, xi, Function,iterations, tolerance, err_type):
        print(err_type)
        xi_1 = xi
        counter = 1
        error = tolerance+1
        fx=Function.evaluar(xi)
        dfx=Function.evaluar_derivada(xi)
        
        while ((error > tolerance) and (fx != 0) and (dfx!=0) and (counter < iterations)):
            xi_1 = xi_1-(Function.evaluar(xi)/Function.evaluar_derivada(xi))
            fx=Function.evaluar(xi_1)
            dfx=Function.evaluar_derivada(xi)
            self.values.append([counter, xi, '%E'%fx,dfx, '%E'%error])
            if(err_type):
                error = math.fabs(xi - xi_1)
            else:
                error = math.fabs((xi - xi_1)/xi)
            xi = xi_1
            counter+=1
        self.values.append([counter, xi, '%E'%fx,'%E'%dfx, '%E'%error])

        if(fx == 0):
            self.raiz=f"[{xi} is a root]"
        elif (error<tolerance):
            self.raiz=f"[{xi} is an approximated root]"
        elif(dfx == 0):
            self.raiz=f"[{xi} is possibly a multiple root]"
        else:
            self.raiz=f"Exceeded iterations"

    def value_table(self):
        return self.values
    def get_sol(self):
        return str(self.raiz)
