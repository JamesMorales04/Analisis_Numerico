from Funciones import Funciones
import math
class Biseccion:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algoritmo_biseccion(self,xi,xu,Funcion,tolerancia,iteraciones,tipo_de_error):
        print(tipo_de_error)
        if((Funcion.evaluar(xi))*(Funcion.evaluar(xu))>0 or tolerancia<0):
            self.raiz="Valores ingresados invalidos"
        if(Funcion.evaluar(xi)==0):
                self.raiz="xi es una raiz"
        else:
            contador=1
            xm=(xi+xu)/2
            xm_anterior=0
            error=tolerancia+10
            self.valores.append([contador,xi,xu,xm,Funcion.evaluar(xm),error])
            while (error>tolerancia and Funcion.evaluar(xm)!=0 and iteraciones>contador):
                valor=Funcion.evaluar(xm)
                if((Funcion.evaluar(xm)*Funcion.evaluar(xi))>0):
                    xi=xm
                else:
                    xu=xm
                xm_anterior=xm
                xm=(xi+xu)/2
                if(tipo_de_error):
                    error=math.fabs(xm-xm_anterior)
                else:
                    error=math.fabs(xm-xm_anterior)/xm
                contador+=1
                self.valores.append([contador,xi,xu,xm,valor,error])
            if(Funcion.evaluar(xm)==0):
                self.raiz=f"[{xm} es una raiz]"
            else:
                if(error<tolerancia):
                    self.raiz=f"[{xm} es una raiz aproximada]"
                else:
                    self.raiz=f"Fracaso en la iteraciones"

    def tabla_valores(self):
        return self.valores
    def get_raiz(self):
        return str(self.raiz)

