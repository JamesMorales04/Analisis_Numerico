from Funciones import Funciones
class Verificar:

    def verificar_funcion(self,funcion,xi):
        if(funcion==""):
            return True
        else:
            try:
                prueba_funcion=Funciones(funcion)
                if ((prueba_funcion.evaluar(xi))==True) or prueba_funcion.evaluar(xi)=="" :
                    print("buenas")
                    return True
                else:
                    return False
            except:
                return True

    def verificar_busqueda(self,funcion,xi,incremento,iteraciones):
        error=""
        try:
            print(float(incremento),float(iteraciones),float(xi))
            if(self.verificar_funcion(funcion,float(xi))):
                error+=self.invalidFunction()
            if(float(incremento)==0):
                error+=self.invalid_increment()
            if(float(iteraciones)<=1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error

    def verificar_biseccion(self,funcion,xi,valor_final,iteraciones,tolerancia):
        error=""
        try:
            if(self.verificar_funcion(funcion,float(xi))):
                error+=self.invalidFunction()
            else:
                raiz=Funciones(funcion)
                if((raiz.evaluar(float(xi))*raiz.evaluar(float(valor_final)))>0):
                    error+="\nEl intervalo no contiene raiz"
            if(float(tolerancia)<=0):
                error+=self.invalidTolerance()
            if(float(iteraciones)<=1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error

    def verificar_punto_fijo(self,funcion,gfuncion,xi,iteraciones,tolerancia):
        error=""
        try:
            if(self.verificar_funcion(funcion,float(xi)) and self.verificar_funcion(gfuncion,float(xi))):
                error+=self.invalidFunction()
            if(float(tolerancia)<=0):
                error+=self.invalidTolerance()
            if(float(iteraciones)<=1):
                error+=self.invalidIterations()
        except:
            print("entra al except???? de pj")
            error=self.empty_field()
        return error

    def verificar_newton(self,function,xi,iterations,tolerance):
        error=""
        try:
            
            if(self.verificar_funcion(function,float(xi))):
                error+=self.invalidFunction()
            
            if(float(tolerance)<=0):
                error+=self.invalidTolerance()
            if(float(iterations)<=1):
                error+=self.invalidIterations()
        except:
            print("entra al except???? de newton")
            error=self.empty_field()
        return error

    def invalidFunction(self):
        return "The function is invalid, \nSquare: (x**n)\nRoot: sqrt(n)\neuler: exp(n)\nPi: pi()\nIdentities: sin(n),cos(n),tan(n),sec(n)\nnatural logarithm: log(n)"                
    def invalidTolerance(self):
        return "\nThe tolerance is invalid"
    def invalidIterations(self):
        return "\nThe iterations are not valid"
    def invalid_increment(self):
        return "\nThe entered increment is invalid"
    def empty_field(self):
        return "\nOne of the fields is empty"