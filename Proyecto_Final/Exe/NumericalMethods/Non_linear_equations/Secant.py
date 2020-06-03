from Functions import *
import math

class Secant:
    def __init__(self):
        self.valores = []
        self.raiz = ''
    
    def algorithm_secant(self, xi_1 , xi_2, function, iter, tol, err_type):
        Yi_1 = function.evaluar(xi_1)
        Yi_2 = function.evaluar(xi_2)

        try:
            if(Yi_1 == 0):
                self.raiz = f"{xi_1} is a solution"
            elif(Yi_2 == 0):
                self.raiz = f"{xi_2} is a solution"
            elif(iter<=0):
                self.raiz = "Innvalid iterations value"
            elif(tol<0):
                self.raiz = "Innvalid tolerance threshold"
            else:
                Yi = 100
                error = tol+1000000
                counter = 0
                while(Yi!=0 and iter>counter and tol<=error):
                    
                    difY = Yi_1 - Yi_2
                    xi = xi_1 - Yi_1*(xi_1 - xi_2)/difY
                    Yi = function.evaluar(xi)

                    #Absolute error
                    if(err_type):
                        error = math.fabs(xi-xi_1)           #By using math.fabs(x) this code can generate an error whe x is complex
                    #Relative error
                    else:
                        error = math.fabs((xi-xi_1)/xi)      #By using math.fabs(x) this code can generate an error whe x is complex

                    counter +=1
                    self.valores.append([counter, xi, '%E' %function.evaluar(xi), '%E' %difY, '%E' %error])
                    xi_2 = xi_1
                    xi_1 = xi
                    Yi_2 = Yi_1
                    Yi_1 = Yi
                
                if(Yi == 0):
                    self.raiz = f"{xi} is a root"
                elif(error<=tol):
                    self.raiz = f"{xi} is an aproximation to the root"
                else:
                    self.raiz = "Number of iterations exceeded"
        #Exception handling, specially:
        #      - the zero division that can happen whe subtracting F(xi_1)-F(Xi_2)
        #      - the type error that can be generated when converting a complex number with math.fabs()
        except ZeroDivisionError:
            print("Dividing by zero")
            self.raiz = "F(Xi) - F(Xi_1) is cero"
        except TypeError as e:
            print(e)

                
    def value_table(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)

                

