import copy
import math
from decimal import *

class Relaxed_gs:
    def __init__(self):
        self.original=[]
        self.new=[]
        self.result=[]
        self.rows=[]
        self.total=[]
        self.final_result=[]
        getcontext().prec = 25

    def Relaxed_gs_algorithm(self,matrix,matrixb,initvalues,lamb,tol):
        self.original=copy.deepcopy(matrix)
        self.result.append(initvalues[0])
        error_total=20
        t=0
        while error_total>tol:    
            i=0
            valores=[]
            while i<len(matrix):
                j=0
                total=matrixb[0][i]
                divider=1
                op=""
                while j<len(matrix[i]):
                    if(i!=j):
                        try:             
                            total=total-(matrix[i][j]*valores[j])
                        except:
                            total=total-(matrix[i][j]*self.result[t][j])
                    else:
                        divider=matrix[i][j]
                    j+=1
                valores.append(lamb*(total/divider)+(1-lamb)*self.result[t][i])
                i+=1
            self.result.append(valores)
            if(t==0):
                self.new.append([t,self.result[t],t])
            else:
                error_total=self.error_calculator(self.result[t],self.result[t-1])
                self.new.append([t,self.result[t],error_total])
            t+=1
        self.row_definition()

    def error_calculator(self,now,previus):
        resultop=0
        resultdown=0
        for i in range(0,len(previus)):
            resultop+=math.pow((now[i]-previus[i]),2)
            resultdown+=math.pow(now[i],2)
        return math.sqrt(resultop)/math.sqrt(resultdown)

    def row_definition(self):
        self.rows.append("n")
        for i in range(0,len(self.new[0])):
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

cosa=Relaxed_gs()
cosa.Relaxed_gs_algorithm([[13,-4,-9],[3,-7,4],[-4,15,-16]],[[-23,5,34]],[[-12.3,-11.7,-10.0]],1.24)
"""
