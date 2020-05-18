import copy
from decimal import *

class Relaxed_gs:
    def __init__(self):
        self.original=[]
        self.new=[]
        self.result=[]
        getcontext().prec = 25

    def Relaxed_gs_algorithm(self,matrix,matrixb,initvalues):
        self.original=copy.deepcopy(matrix)
        self.result.append(initvalues)
        for t in range(0,6):
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
                            #op+=str(total)+"-"+str(matrix[i][j])+"*"+str(valores[j])
                        except:
                            total=total-(matrix[i][j]*self.result[t][j])
                            op+=str(total)+""+str(matrix[i][j])+"*"+str(self.result[t][j])
                    else:
                        divider=matrix[i][j]
                    j+=1
                valores.append(total/divider)
                i+=1
            self.result.append(valores)
        for i in self.result:
            print(i)

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
        for i in matrix:
            print(i)
        
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
        for i in self.result:
            results+=f"X{aux}: "+(str)(i)+"\n"
            aux+=1
        return results
cosa=Relaxed_gs()
cosa.Relaxed_gs_algorithm([[13,-4,-5],[3,-7,2],[-4,5,-16]],[[-23,5,34]],[0,0,0])