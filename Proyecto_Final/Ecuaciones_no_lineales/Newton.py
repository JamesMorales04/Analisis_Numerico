from Funciones import *
import math
class Newton:
    def __init__(self):
        self.values=[]
        self.raiz=""

    def algoritmo_newton(self, xi, Funcion,iterations, tolerance, err_type):
        print(err_type)
        xi_1 = xi
        counter = 1
        error = tolerance+1
        fx=Funcion.evaluar(xi)
        dfx=Funcion.evaluar_derivada(xi)
        
        while ((error > tolerance) and (fx != 0) and (dfx!=0) and (counter < iterations)):
            xi_1 = xi_1-(Funcion.evaluar(xi)/Funcion.evaluar_derivada(xi))
            fx=Funcion.evaluar(xi_1)
            dfx=Funcion.evaluar_derivada(xi)
            self.values.append([counter, xi, fx,dfx, error])
            if(err_type):
                error = math.fabs((xi - xi_1)/ xi)
            else:
                error = math.fabs(xi - xi_1)
            xi = xi_1
            counter+=1
        self.values.append([counter, xi, fx,dfx, error])

        if(fx == 0):
            self.raiz=f"[{xi} is a root]"
        elif (error<tolerance):
            self.raiz=f"[{xi} is an approximated root]"
        elif(dfx == 0):
            self.raiz=f"[{xi} is possibly a multiple root]"
        else:
            self.raiz=f"Exceeded iterations"

    def tabla_valores(self):
        return self.values
    def get_sol(self):
        return str(self.raiz)
