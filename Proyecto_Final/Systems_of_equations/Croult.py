import copy
from decimal import *

class Croult:
    def __init__(self):
        self.original=[]
        self.oldb=[]
        self.total=[]
        self.result=[]
        self.resultsz=[]
        self.rows=[]
        self.matrixL=[]
        self.matrixU=[]
        self.new=[]
        self.no_error=True
        getcontext().prec = 25

    def croult_algorithm(self,matrix,matrixb):
        self.make_matrixLU(matrix)
        self.original=copy.deepcopy(matrix)
        acumU=0
        acumL=1
        for i in range(0,len(matrix)):
            self.result.append(0)
            self.resultsz.append(0)
            if(i!=0):
                for j in range(acumL,len(matrix[i])):
                    aux=self.get_column(self.matrixU,i)
                    self.matrixL[j][i]=self.multiply_lists(self.matrixL[j],aux,matrix[j][i])
                acumL+=1
            for k in range(acumU,len(matrix[i])):
                aux= self.get_column(self.matrixU,k)
                if(i!=k):
                    self.matrixU[i][k]=self.multiply_lists(self.matrixL[i],aux,matrix[i][k])
            acumU+=1
        matrixb[0].reverse()
        self.oldb=copy.deepcopy(self.matrixL)
        self.new=self.sort_matrix(self.matrixL)
        self.new=self.merge(self.new,matrixb)
        if(self.check_diagonal()):
            self.variable_resolution()
            self.result.reverse()
            self.resultsz=[copy.deepcopy(self.result)]
            self.new=self.merge(self.matrixU,self.resultsz)
        else:
            self.no_error=False
        if(self.check_diagonal() and self.no_error):
            self.variable_resolution()
            self.row_definition()
            self.matrixL=self.merge(self.oldb,matrixb)
            self.matrixU=self.merge(self.matrixU,self.resultsz)
            self.original=self.merge(self.original,matrixb)
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

    
    def sort_matrix(self,matrix):
        aux=[]
        j=len(matrix)-1
        while j>=0:
            matrix[j].reverse()
            aux.append(matrix[j])
            j-=1
        return aux

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

    def make_matrixLU(self,matrix):
        for i in range(0,len(matrix)):
            self.matrixL.append([])
            self.matrixU.append([])
            savel="L"
            saveu=0
            for j in range(0,len(matrix[i])):
                if(i==j):
                    saveu=1
                    if(j==0):
                        self.matrixL[i].append(matrix[i][j])
                    else:
                        self.matrixL[i].append(savel)
                    self.matrixU[i].append(saveu)
                    savel=0
                    saveu="U"
                elif(j==0):
                    self.matrixL[i].append(matrix[i][j])
                    self.matrixU[i].append(saveu)
                else:
                    self.matrixL[i].append(savel)
                    self.matrixU[i].append(saveu)

    def get_column(self,matrix,column):
        newColumn=[]
        for i in matrix:
            newColumn.append(i[column])
        return newColumn

    def multiply_lists(self,row,column,result):
        total=0.0
        divider=1.0
        for i in range(0,len(column)):
            if(column[i]!="U" and row[i]!="L"):
                total+=row[i]*column[i]
            else:
                if(column[i]=="U" and row[i]!=0):
                    divider=row[i]
                elif(row[i]=="L" and column[i]!=0):
                    divider=column[i] 
        result=(result-total)/divider
        return result

    def row_definition(self,tables):
        for i in range(0,tables):
            for i in range(1,len(self.result)+1):
                self.rows.append(f"x{i}")
            self.rows.append("b")
            self.rows.append("///")

    def value_table(self):
        for i in range(0,len(self.original)):
            self.total.append([])
            for j in range(0,len(self.original[i])):
                self.total[i].append(Decimal(self.original[i][j]))
            self.total[i].append("///")
            for j in range(0,len(self.original[i])):
                self.total[i].append(Decimal(self.matrixL[i][j]))
            self.total[i].append("///")    
            for j in range(0,len(self.original[i])):
                self.total[i].append(Decimal(self.matrixU[i][j]))
            self.total[i].append("///")
        return self.total

    def get_results(self):
        results=""
        aux=1
        for i in self.result:
            results+=f"X{aux}: "+(str)(i)+"\n"
            aux+=1
        return results
    def get_noerror(self):
        return self.no_error


"""
[20,-1,3,4]
[6,23,4,3]
[7,21,46,9]
[-3,-9,12,38]
"""
cosa=Croult()
cosa.croult_algorithm([[0,1/5,1/6,1/7],[1/3,1/4,1/5,1/6],[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5]],[[60,70,106,84]])