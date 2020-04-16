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
            self.raiz="Numero de iteraciones invalidas"
        elif (tolerancia < 0):
            self.raiz="Tolerancia invalida"
        else:
            xi_1 = xi
            contador = 1
            error = tolerancia+1
            self.valores.append([contador, xi, Funcion.evaluar(xi), error])
            while ((error > tolerancia) and (Funcion.evaluar(xi) != 0) and (contador < iteraciones)):
                xi = GFuncion.evaluar(xi)
                if(xi=="Final"):
                    break
                if(tipo_de_error):
                    print("error absoluto")
                    error = abs(xi - xi_1)
                else:
                    print("error relativo")
                    error = abs((xi - xi_1)/ xi)
                xi_1 = xi
                contador+=1
                self.valores.append([contador, xi, Funcion.evaluar(xi), error])
                
            if(Funcion.evaluar(xi) == 0):
                self.raiz=f"[{xi} es una raiz]"
            else:
                if(error<tolerancia):
                    self.raiz=f"{xi}"
                else:
                    self.raiz=f"Fracaso en la iteraciones"

    def tabla_valores(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)
