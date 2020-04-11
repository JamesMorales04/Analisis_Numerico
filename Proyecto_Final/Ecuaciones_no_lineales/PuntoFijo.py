from Funciones import *
import math
class PuntoFijo:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algoritmo_puntoFijo(self, xi, Funcion, GFuncion, iteraciones, tolerancia, tipo_de_error):
        print(tipo_de_error)
        if (Funcion.evaluar(xi) == 0):
            self.raiz=f"{xi} es una raiz"
        elif (iteraciones <= 0):
            self.raiz="Numero de iteraciones innalidas"
        elif (tolerancia < 0):
            self.raiz="Tolerancia invalida"
        else:
            xi_1 = xi
            contador = 1
            error = tolerancia+1
            self.valores.append([contador, xi, Funcion.evaluar(xi), error])
            while ((error > tolerancia) and (Funcion.evaluar(xi) != 0) and (contador < iteraciones)):
                xi = GFuncion.evaluar(xi)
                if(tipo_de_error):
                    error = math.fabs((xi - xi_1)/ xi)
                else:
                    error = math.fabs(xi - xi_1)
                xi_1 = xi
                contador+=1
                self.valores.append([contador, xi, Funcion.evaluar(xi), error])
            if(Funcion.evaluar(xi) == 0):
                self.raiz=f"[{xi} es una raiz]"
            else:
                if(error<tolerancia):
                    self.raiz=f"[{xi} es una raiz aproximada]"
                else:
                    self.raiz=f"Fracaso en la iteraciones"

    def tabla_valores(self):
        return self.valores
    def get_raiz(self):
        return str(self.raiz)
