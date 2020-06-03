from Functions import Functions
class Verify:

    def verify_function(self,function,xi):
        if(function==""):
            return True
        
        else:
            try:
                prueba_function=Functions(function)
                if ((prueba_function.evaluar(xi))==True or (prueba_function.evaluar(xi))=="Final") or prueba_function.evaluar(xi)=="" or ('x' not in function) :
                    return True
                else:
                    return False
            except:
                return True

    def verify_search(self,function,xi,incremento,iteraciones):
        error=""
        try:
            if(self.verify_function(function,float(xi))):
                error+=self.invalidFunction()
            if(float(incremento)==0):
                error+=self.invalid_increment()
            if(float(iteraciones)<=1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error

    def verify_bisection(self,function,xi,valor_final,iteraciones,tolerancia):
        error=""
        try:
            if(self.verify_function(function,float(xi))):
                error+=self.invalidFunction()
            else:
                raiz=Functions(function)
                if((raiz.evaluar(float(xi))*raiz.evaluar(float(valor_final)))>0):
                    error+="\nEl intervalo no contiene raiz"
            if(float(tolerancia)<=0):
                error+=self.invalidTolerance()
            if(float(iteraciones)<=1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error

    def verify_fixed_point(self,function,gfunction,xi,iteraciones,tolerancia):
        error=""
        try:
            if(self.verify_function(function,float(xi)) or self.verify_function(gfunction,float(xi))):
                error+=self.invalidFunction()
            if(float(tolerancia)<=0):
                error+=self.invalidTolerance()
            if(float(iteraciones)<=1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error

    def verify_newton(self,function,xi,iterations,tolerance):
        error=""
        try:
            
            if(self.verify_function(function,float(xi))):
                error+=self.invalidFunction()
            
            if(float(tolerance)<=0):
                error+=self.invalidTolerance()
            if(float(iterations)<=1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error


    def verify_secant(self, xi_1 , xi_2, function, iter, tol):
        error = ''
        try:
            if(self.verify_function(function,float(xi_1)) or self.verify_function(function, float(xi_2))):
                error+=self.invalidFunction()
            if(float(tol)<0):
                error+=self.invalidTolerance()
            if(float(iter)<=0):
                error+=self.invalidIterations()
        except Exception:
            error = self.empty_field()
        return error

    def verify_raices_mult(self,xi,function,iterations,tolerance):
        error=""
        try:
            
            if(self.verify_function(function,float(xi))):
                error+=self.invalidFunction()
            
            if(float(tolerance)<=0):
                error+=self.invalidTolerance()
            if(float(iterations)<1):
                error+=self.invalidIterations()
        except:
            error=self.empty_field()
        return error

    def verify_length(self,Matrix):
        aux=[]
        for i in Matrix:
            aux.append(len(i))
        print(aux)
        for i in aux:
            for j in aux:
                if(j!=i):
                    return True
        return False 
        
    def verify_seidel_Jacobi(self,a,b,init,iter,tol,lamb):
        error=""
        try:
            lamb=float(lamb)
            iter=int(iter)
            tol=float(tol)
            if(self.verify_length(a)):
                error+=self.invalidMatrixInput()
            if(len(a)==0 or len(b[0])==0):
                error+=self.invalidMatrixInput()
            if(len(a)!=len(b[0]) or len(a)!=len(init[0]) or len(a[0])!=len(b[0]) ):
                error+=self.invalidMatrixInput()
            if(len(init[0])==0):
                error+=self.invalidInitVals()
            if(tol<=0):
                error+=self.invalidTolerance()
            if(iter<=1):
                error+=self.invalidIterations()
        except:
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
    def invalidMatrixInput(self):
        return "\nInvalid Matrix Input"
    def invalidInitVals(self):
        return "\nInvalid Initial Values"