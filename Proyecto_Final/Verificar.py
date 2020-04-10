from Funciones import Funciones
class Verificar:

    def verificar_funcion(self,funcion,valor_inicial):
        if(funcion==''):
            return True
        else:
            try:
                prueba_funcion=Funciones(funcion)
                prueba_funcion.evaluar(valor_inicial)
                return False
            except:
                return True

    def verificar_busqueda(self,funcion,valor_inicial,incremento,iteraciones):
        error=""
        try:
            print(float(incremento),float(iteraciones),float(valor_inicial))
            if(self.verificar_funcion(funcion,float(valor_inicial))):
                error+="La funcion es invalida, \n Los comandos son: Potencia x**2 \n Raiz= sqrt(x) \n Logaritmo natura= log(x) \n pi= pi \n seno,cose,tangente= sen(x),cos(x),tan(x)"
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
                error+="\nLa funcion es invalida\nLos comandos son: Potencia x**2\nRaiz= sqrt(x)\nLogaritmo natura= log(x)\npi= pi\nseno,cose,tangente= sen(x),cos(x),tan(x)"
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
                error+="\nLa funcion es invalida\nLos comandos son: Potencia x**2\nRaiz= sqrt(x)\nLogaritmo natura= log(x)\npi= pi\nseno,cose,tangente= sen(x),cos(x),tan(x)"
            if(float(tolerancia)<=0):
                error+="\nLa tolerancia es invalida "
            if(float(iteraciones)<=1):
                error+="\nLas iteraciones ingresadas son invalidas "
        except:
            error="Uno de los campos esta vacio"
        return error