from decimal import *
import copy

class partial_Pivoting:
    def __init__(self):
        self.original= []
        self.new = []
        self.total= []
        self.result=[]
        self.rows = []
        self.error=False
        self.steps= []
        self.steps_row= []
        getcontext().prec = 25

    def partial_pivoting_algorithm(self,matrix,matrixb):
        matrix=self.merge(matrix,matrixb)
        self.original=copy.deepcopy(matrix)
        column=0
        i=1
        lenght=len(matrix)
        n=0
        while n < lenght and not self.error: 
            self.steps.append(copy.deepcopy(matrix))
            pos=n  
            bigger=matrix[n][n]
            for i in range (n+1,lenght):
                if (abs(matrix[i][n]) > bigger):
                    bigger= abs(matrix[i][n])
                    pos = i
            temp=matrix[n]
            big=matrix[pos] 
            matrix[n]=big
            matrix[pos]=temp #SWAP
            row=n+1
            if matrix[n][n] == 0:
                self.error=True 
            for i in range (row,lenght):
                multiplier=matrix[i][n]/matrix[row-1][n]
                if matrix[n][n] == 0:
                    self.error=True 
                for j in range(n,len(matrix[i])):                      
                    matrix[i][j]=matrix[i][j]-matrix[row-1][j]*multiplier             
            n+=1
            self.steps.append(copy.deepcopy(matrix))
            
        self.new= matrix
        self.get_steps()

        if(not self.error):
            if (self.check_diagonal()):
                self.variable_resolution()
                self.row_definition()
        else:
            self.result="No solutions or infinite solutions"
        
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
            aux=0
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
        if (self.error):
            results="No solutions or infinite solutions"
            return results
        for i in self.result:
            results+=f"X{aux}: "+(str)(i)+"\n"
            aux+=1

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

    def get_error(self):
        return self.error
"""
[2,1,1]
[4,-6,0]
[-2,7,2]
[5,-2,9]
"""

"""
[2,-3,4,1]
[-4,2,1,-2]
[1,3,-5,3]
[-3,-1,1,-1]
[10,-10,32,-21]
"""
#cosa.partial_pivoting_algorithm([[1/4,1/5,1/6,1/7],[1/3,1/4,1/5,1/6],[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5]],[60,70,106,84])