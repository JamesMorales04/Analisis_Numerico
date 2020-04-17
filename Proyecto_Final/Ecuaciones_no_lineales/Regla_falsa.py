from Funciones import Funciones
import math
class Regla_falsa:

    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algoritmo_regla_falsa(self,xi,xu,Funcion,tolerancia,iteraciones,tipo_de_error):
        print(tipo_de_error)
        if((Funcion.evaluar(xi))*(Funcion.evaluar(xu))>0 or tolerancia<0):
            self.raiz="Wrong values"
        if(Funcion.evaluar(xi)==0):
                self.raiz="xi is a root"
        else:
            contador=1
            xm=xi-(Funcion.evaluar(xi)*(xi-xu))/(Funcion.evaluar(xi)-Funcion.evaluar(xu))
            xm_anterior=0
            error=tolerancia+10
            
            while (error>tolerancia and Funcion.evaluar(xm)!=0 and iteraciones>contador):
                valor=Funcion.evaluar(xm)
                self.valores.append([contador,xi,xu,xm,'%E' %valor,'%E' %error])
                if((Funcion.evaluar(xm)*Funcion.evaluar(xi))>0):
                    xi=xm
                else:
                    xu=xm
                xm_anterior=xm
                xm=xi-(Funcion.evaluar(xi)*(xi-xu))/(Funcion.evaluar(xi)-Funcion.evaluar(xu))
                if(tipo_de_error):
                    error=math.fabs(xm-xm_anterior)
                else:
                    error=math.fabs(xm-xm_anterior)/xm
                contador+=1
            self.valores.append([contador,xi,xu,xm,'%E' %Funcion.evaluar(xm),'%E' %error])
            if(Funcion.evaluar(xm)==0):
                self.raiz=f"[{xm} is a root]"
            else:
                if(error<tolerancia):
                    self.raiz=f"[{xm} is an approximated root]"
                else:
                    self.raiz=f"Exceeded iterations"

    def tabla_valores(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)

