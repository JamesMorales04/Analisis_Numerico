from Functions import *
import math
class Regla_falsa:

    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algorithm_regla_falsa(self,xi,xu,Function,tolerancia,iteraciones,tipo_de_error):
        print(tipo_de_error)
        if((Function.evaluar(xi))*(Function.evaluar(xu))>0 or tolerancia<0):
            self.raiz="Wrong values"
        if(Function.evaluar(xi)==0):
                self.raiz="xi is a root"
        else:
            contador=1
            xm=xi-(Function.evaluar(xi)*(xi-xu))/(Function.evaluar(xi)-Function.evaluar(xu))
            xm_anterior=0
            error=tolerancia+10
            
            while (error>tolerancia and Function.evaluar(xm)!=0 and iteraciones>contador):
                valor=Function.evaluar(xm)
                self.valores.append([contador,xi,xu,xm,'%E' %valor,'%E' %error])
                if((Function.evaluar(xm)*Function.evaluar(xi))>0):
                    xi=xm
                else:
                    xu=xm
                xm_anterior=xm
                xm=xi-(Function.evaluar(xi)*(xi-xu))/(Function.evaluar(xi)-Function.evaluar(xu))
                if(tipo_de_error):
                    error=math.fabs(xm-xm_anterior)
                else:
                    error=math.fabs((xm-xm_anterior)/xm)
                contador+=1
            self.valores.append([contador,xi,xu,xm,'%E' %Function.evaluar(xm),'%E' %error])
            if(Function.evaluar(xm)==0):
                self.raiz=f"[{xm} is a root]"
            else:
                if(error<tolerancia):
                    self.raiz=f"[{xm} is an approximated root]"
                else:
                    self.raiz=f"Exceeded iterations"

    def value_table(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)

