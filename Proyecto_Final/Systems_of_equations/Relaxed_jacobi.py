import copy
import math
from decimal import *

class Relaxed_jacobi:
    def __init__(self):
        self.original=[]
        self.new=[]
        self.result=[]
        self.rows=[]
        self.total=[]
        self.final_result=[]
        self.div=False
        getcontext().prec = 25

    def Relaxed_jacobi_algorithm(self,matrix,matrixb,initvalues,lamb,tol,iter):
        self.original=copy.deepcopy(matrix)
        self.result.append(initvalues[0])
        error_total=20
        t=0
        print(iter>=t)
        divider=1
        while error_total>tol and divider!=0 and iter>=t:
            i=0
            valores=[]
            while i<len(matrix) and divider!=0:
                j=0
                total=matrixb[0][i]
                op=""
                while j<len(matrix[i]) and divider!=0:
                    if(i!=j):
                            total=total-(matrix[i][j]*self.result[t][j])
                    else:
                        divider=matrix[i][j]
                    j+=1
                if divider!=0:
                    valores.append(lamb*(total/divider)+(1-lamb)*self.result[t][i])
                    i+=1
            if divider!=0:
                self.result.append(valores)
                if(t==0):
                    self.new.append([t,self.result[t],t])
                else:
                    error_total=self.error_calculator(self.result[t],self.result[t-1])
                    if error_total==0:
                        self.div=True
                        divider=0
                    self.new.append([t,self.result[t],error_total])
                t+=1
            else:
                aux=[]
                for i in range(len(matrix[i])):
                    aux.append(0)
                self.new.append([0,aux,0])
                self.div=True
        self.row_definition()


    def error_calculator(self,now,previus):
        resultop=0.0
        resultdown=0.0
        for i in range(0,len(previus)):
            try:
                resultop+=math.pow((now[i]-previus[i]),2)
                resultdown+=math.pow(now[i],2)
            except:
                resultop=0.0
                resultdown=0.0
                break
        if(resultdown==0):
            return 0
        else:
            return math.sqrt(resultop)/math.sqrt(resultdown)

    def row_definition(self):
        self.rows.append("n")
        for i in range(0,len(self.result[0])):
            self.rows.append(f"x{i}")
        self.rows.append("Error")
        

    def value_table(self):
        x=0
        for i in self.new:
            self.total.append([])
            self.total[x].append(i[0])
            for j in i[1]:
                self.total[x].append(Decimal(j))
            self.total[x].append(Decimal(i[2]))
            x+=1
        self.final_result=copy.deepcopy(self.total[len(self.total)-1])
        self.final_result.pop(0)
        self.final_result.pop()
        return self.total

    def get_sol(self):
        results=""
        if self.div:
            results="Div0 No solution"
        else:
            aux=0
            for i in self.final_result:
                results+=f"X{aux}: "+(str)('%E'%i)+"\n"
                aux+=1
        return results
"""
[13,-4,-5]
[3,-7,2]
[-4,5,-16]


[13,-4,-9]
[3,-7,4]
[-4,15,-16]


[-23,5,34]
[1,1,1]





[34,-5,6,12]
[-9,43,21,-8]
[-12,4,75,22]
[7,5,-13,65]

[37,123,16,9]

[0,0,0,0]

cosa=Relaxed_jacobi()
cosa.Relaxed_jacobi_algorithm([[13,-4,-5],[3,-7,2],[-4,5,-16]],[[-23,5,34]],[[0,0,0]],1,0.00005)
"""
