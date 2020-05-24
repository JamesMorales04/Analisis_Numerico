import copy
from decimal import *

class Gaussian_Elimination:
    def __init__(self):
        self.original=[]
        self.new=[]
        self.total=[]
        self.result=[]
        self.rows=[]
        self.no_error=True
        self.steps=[]
        self.steps_row=[]
        getcontext().prec = 25

    def gaussian_elimination_algorithm(self,matrix,matrixb):
        matrix=self.merge(matrix,matrixb)
        self.original=copy.deepcopy(matrix)
        column=0
        i=1
        while i <= len(matrix) and self.no_error:
            self.steps.append(copy.deepcopy(matrix))
            for j in range(i,len(matrix)):
                if(matrix[i-1][column]!=0):
                    multiplier=matrix[j][column]/matrix[i-1][column]
                else:
                    self.no_error=False
                    break
                for k in range(column,len(matrix[j])):
                    matrix[j][k]=matrix[j][k]-matrix[i-1][k]*multiplier            
            column+=1
            i+=1 
        self.new=matrix
        self.get_steps()
        for i in self.steps:
            print(i)
        for i in self.steps_row:
            print(i)

        if(self.check_diagonal() and self.no_error):
            self.variable_resolution()
            self.row_definition()
        else:
            self.result="No solutions or infinite solutions or Div 0"


    def check_diagonal(self):
        for i in range(0,len(self.new)):
            for j in range(0,len(self.new[i])):
                if(j==i):
                    self.result.append(0)
                    if(self.new[i][j]==0):
                        return False
        return True

    def variable_resolution(self):
        i=len(self.new)-1
        while(i>=0):
            j=len(self.new[i])-1
            aux=1
            while(j>=0):
                if(j!=i):
                    if(len(self.new[i])-1==j):
                        self.result[i]=self.new[i][j]
                    else:
                        self.result[i]-=self.new[i][j]*self.result[j]
                else:
                    aux=self.new[i][j]
                if(j==0):
                    self.result[i]/=aux
            
                j-=1
        
            i-=1     
    def merge(self,matrix,matrixb):
        for i in range(0,len(matrix)):

            matrix[i].append(matrixb[0][i])
        return matrix

    def row_definition(self):
        for i in range(1,len(self.result)+1):
            self.rows.append(f"x{i}")
        self.rows.append("b")
        self.rows.append("///")
        for i in range(1,len(self.result)+1):
            self.rows.append(f"x{i}")
        self.rows.append("b")

    def value_table(self):
        for i in range(0,len(self.new)):
            self.total.append([])
            for j in range(0,len(self.new[i])):
                self.total[i].append(Decimal(self.original[i][j]))
            self.total[i].append("///")
            for j in range(0,len(self.new[i])):
                self.total[i].append(Decimal(self.new[i][j]))


        return self.total

    def get_results(self):
        results=""
        aux=1
        if(self.no_error):
            for i in self.result:
                results+=f"X{aux}: "+(str)(i)+"\n"
                aux+=1
        else:
            return self.result
        return results

    def get_steps(self):
        aux=[]
        for i in self.steps:
            for j in i:
                aux.append(j)
            aux.append([])
        for i in range(1,len(self.steps[0][0])+1):
            self.steps_row.append(f"x{i}")
        self.steps=aux
    def get_steps_table(self):
        return self.steps
    def get_steps_rows(self):
        return self.steps_row
    def get_noerror(self):
        print(self.no_error)
        return self.no_error
"""
cosa=Gaussian_Elimination()
cosa.gaussian_elimination_algorithm([[0,1/5,1/6,1/7],[1/3,1/4,1/5,1/6],[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5]],[[60,70,106,84]])
[2,-3,4,1]
[-4,2,1,-2]
[1,3,-5,3]
[-3,-1,1,-1]

[10,-10,32,-21]
"""