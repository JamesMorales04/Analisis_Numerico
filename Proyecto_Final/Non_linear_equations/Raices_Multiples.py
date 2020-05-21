from Functions import *
import math

class Raices_Multiples:

    def __init__(self):
        self.valores = []
        self.raiz = ''

    def algoritmo_raices_mult(self, xi, function,iter, tol, err_type):

        try:
            Yi = function.evaluar(xi)
            d1F = function.derivarM(function,1,xi)
            d2F = function.derivarM(function,2,xi)
            if(Yi == 0):
                self.raiz = f"{xi} is a solution"
            elif(iter<=0):
                self.raiz = "Innvalid iterations value"
            elif(tol<0):
                self.raiz = "Innvalid tolerance threshold"
            else:
                error = tol+1000000
                counter = 1
                xi_1 = xi
                Yi_1 = Yi
                self.valores.append([counter, xi, '%E' %Yi, '%E' %d1F, '%E' %d2F, '%E' %error])

                while(Yi!=0 and error>=tol and counter<=iter):
                    xi = float(xi_1 - Yi_1*d1F/(d1F**2 - Yi_1*d2F))                                           #Ended Here
                    Yi = function.evaluar(xi)
                    #Absolute error
                    if(err_type):
                        error = math.fabs(xi-xi_1)           #By using math.fabs(x) this code can generate an error whe x is complex
                    #Relative error
                    else:
                        error = math.fabs((xi-xi_1)/xi)      #By using math.fabs(x) this code can generate an error whe x is complex
                        print("Absolute error")
                    
                    d1F = function.derivarM(function,1,xi)
                    d2F = function.derivarM(function,2,xi)
                    counter+=1
                    self.valores.append([counter,'%f' %xi, '%E' %Yi, '%E' %d1F, '%E' %d2F, '%E' %error])
                    Yi_1 = Yi
                    xi_1 = xi


                if(Yi == 0):
                    self.raiz = f"{xi} is a root"
                elif(error<=tol):
                    self.raiz = f"{xi} is an aproximation to the root"
                else:
                    self.raiz = "Number of iterations exceeded"
                    
        except Exception as e:
            print(e)
            self.raiz = "Error"



    
    def value_table(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)

