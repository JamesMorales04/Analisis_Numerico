from Funciones import *
import math
class Newton:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algoritmo_newton(self, xi, Funcion,iteraciones, tolerancia, tipo_de_error):
        print(tipo_de_error)
        xi_1 = xi
        contador = 1
        error = tolerancia+1
        GFuncion = Funcion.derivar(Funcion)
        print("derivada es "+GFuncion)
        fx=Funcion.evaluar(xi)
        GFuncion= Funcion #Aqui deberia hacer el parse 
        dfx=GFuncion.evaluar(xi)
        self.valores.append([contador, xi, fx,dfx, error])
        while ((error > tolerancia) and (fx != 0) and (dfx!=0) and (contador < iteraciones)):
            xi_1 = xi_1-(Funcion.evaluar(xi)/GFuncion.evaluar(xi))
            fx=Funcion.evaluar(xi_1)
            dfx=GFuncion.evaluar(xi_1)
            if(tipo_de_error):
                error = math.fabs((xi - xi_1)/ xi)
            else:
                error = math.fabs(xi - xi_1)
            xi = xi_1
            contador+=1
            self.valores.append([contador, xi, fx,dfx, error])

        if(fx == 0):
            self.raiz=f"[{xi} is a root]"
        elif (error<tolerancia):
            self.raiz=f"[{xi} is an approximated root]"
        elif(dfx == 0):
            self.raiz=f"[{xi} is possibly a multiple root]"
        else:
            self.raiz=f"Exceeded iterations"



    def tabla_valores(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)
