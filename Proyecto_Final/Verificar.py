from Funciones import Funciones
class Verificar:

    def verificar_funcion(self,funcion,valor_inicial):
        if(funcion==""):
            return True
        else:
            try:
                prueba_funcion=Funciones(funcion)
                if ((prueba_funcion.evaluar(valor_inicial))==True) or prueba_funcion.evaluar(valor_inicial)=="" :
                    print("buenas")
                    return True
                else:
                    return False
            except:
                return True

    def verificar_busqueda(self,funcion,valor_inicial,incremento,iteraciones):
        error=""
        try:
            print(float(incremento),float(iteraciones),float(valor_inicial))
            if(self.verificar_funcion(funcion,float(valor_inicial))):
                error+="La funcion es invalida,\nPotencia: (x**n)\nRaiz: sqrt(n)\nExponencia: exp(n)\nPi: pi()\nIdentidades: sin(n),cos(n),tan(n),sec(n)\nLogaritmo natural: log(n)"
            if(float(incremento)==0):
                error+="\nEl incremento ingresado es invalido "
            if(float(iteraciones)<=1):
                error+="\nLas iteraciones ingresadas son invalidas "
        except:
            error="Uno de los campos esta vacio"
        return error

    def verificar_biseccion(self,funcion,valor_inicial,valor_final,iteraciones,tolerancia):
        error=""
        try:
            if(self.verificar_funcion(funcion,float(valor_inicial))):
                error+="La funcion es invalida,\nPotencia: (x**n)\nRaiz: sqrt(n)\nExponencia: exp(n)\nPi: pi()\nIdentidades: sin(n),cos(n),tan(n),sec(n)\nLogaritmo natural: log(n)"
            else:
                raiz=Funciones(funcion)
                if((raiz.evaluar(float(valor_inicial))*raiz.evaluar(float(valor_final)))>0):
                    error+="\nEl intervalo no contiene raiz"
            if(float(tolerancia)<=0):
                error+="\nLa tolerancia es invalida "
            if(float(iteraciones)<=1):
                error+="\nLas iteraciones ingresadas son invalidas "
        except:
            error="Uno de los campos esta vacio"
        return error

    def verificar_punto_fijo(self,funcion,gfuncion,valor_inicial,iteraciones,tolerancia):
        error=""
        try:
            if(self.verificar_funcion(funcion,float(valor_inicial)) and self.verificar_funcion(gfuncion,float(valor_inicial))):
                error+="La funcion es invalida,\nPotencia: (x**n)\nRaiz: sqrt(n)\nExponencia: exp(n)\nPi: pi()\nIdentidades: sin(n),cos(n),tan(n),sec(n)\nLogaritmo natural: log(n)"
            if(float(tolerancia)<=0):
                error+="\nLa tolerancia es invalida "
            if(float(iteraciones)<=1):
                error+="\nLas iteraciones ingresadas son invalidas "
        except:
            error="Uno de los campos esta vacio"
        return error