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
        self.matrixU_aux=[]
        self.matrixL_aux=[]
        self.original_aux=[]
        self.new=[]
        self.no_error=True
        getcontext().prec = 25

    def croult_algorithm(self,matrix):
        self.make_matrixLU(matrix)
        self.original=copy.deepcopy(matrix)
        acumU=0
        acumL=1
        for i in range(0,len(matrix)):
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
        

    def runb(self,matrixb):
        self.result=[]
        self.resultsz=[]
        self.total=[]
        self.matrixL_aux=copy.deepcopy(self.matrixL)
        self.matrixU_aux=copy.deepcopy(self.matrixU)
        self.original_aux=copy.deepcopy(self.original)
        matrixb[0].reverse()
        self.oldb=copy.deepcopy(self.matrixL_aux)
        self.new=self.sort_matrix(self.matrixL_aux)
        self.new=self.merge(self.new,matrixb)
        if(self.check_diagonal(0) and self.no_error):
            self.variable_resolution()
            self.result.reverse()
            self.resultsz=[copy.deepcopy(self.result)]
            print(self.resultsz)
            self.new=self.merge(self.matrixU_aux,self.resultsz)

            if(self.check_diagonal(1) and self.no_error):
                self.variable_resolution()
                self.row_definition(3)
                matrixb[0].reverse()
                self.matrixL_aux=self.merge(self.oldb,matrixb)
                print(self.resultsz)
                self.matrixU_aux=self.merge(self.matrixU_aux,self.resultsz)
                self.original_aux=self.merge(self.original_aux,matrixb)
                self.value_table()
            else:
                self.no_error=False
        else:
            self.result="No solutions or infinite solutions or Div 0"
            self.no_error=False
        
    def check_diagonal(self,num):
        for i in range(0,len(self.new)):
            for j in range(0,len(self.new[i])):
                if(j==i):
                    if num == 0:
                        self.result.append(0)
                        self.resultsz.append(0)
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
        self.rows=[]
        for i in range(0,tables):
            for i in range(1,len(self.result)+1):
                self.rows.append(f"x{i}")
            self.rows.append("b")
            self.rows.append("///")

    def value_table(self):
        self.total=[]
        for i in range(0,len(self.original_aux)):
            self.total.append([])
            for j in range(0,len(self.original_aux[i])):
                self.total[i].append(Decimal(self.original_aux[i][j]))
            self.total[i].append("///")
            for j in range(0,len(self.original_aux[i])):
                self.total[i].append(Decimal(self.matrixL_aux[i][j]))
            self.total[i].append("///")    
            for j in range(0,len(self.original_aux[i])):
                self.total[i].append(Decimal(self.matrixU_aux[i][j]))
            self.total[i].append("///")

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
    
    def get_noerror(self):
        print(self.no_error)
        return self.no_error

    def get_total(self):
        return self.total

"""
[20,-1,3,4]
[6,23,4,3]
[7,21,46,9]
[-3,-9,12,38]


[30,-10,20,-14]

cosa=Croult()
cosa.croult_algorithm([[0,1/5,1/6,1/7],[1/3,1/4,1/5,1/6],[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5]],[[60,70,106,84]])
"""