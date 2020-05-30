from decimal import *
import copy

class staggered_Pivoting:
    def __init__(self):
        self.original= []
        self.new = []
        self.total= []
        self.result=[]
        self.rows = []
        self.s = []
        getcontext().prec = 25

    def partial_staggered_algorithm(self,matrix,matrixb):
        if len(matrixb) <= 0 or matrixb is None:
            self.result.append("No matrix b")
        elif len(matrix) <= 0 or matrix is None:
            self.result.append("No matrix a")
        elif not self.check_diagonal(self.merge(matrix,matrixb)):
            self.result.append("No valid matrix")
        else:
            #matrix=self.merge(matrix,matrixb)
            self.imprimirMatriz(matrix)
            self.original=copy.deepcopy(matrix)
            no_error=True
            mayor = []
            pMayor = 0
            vMayor = 0.0
            temp = []
            for i in range(len(matrix)):
                self.s.append(0)
            self.busquedaDelMayorDeCadaFila(matrix)
            for k in range(len(matrix)):
                for c in range(k, len(matrix), 1):
                    mayor.append(abs(matrix[c][k] / self.s[c]))
                    if vMayor <= abs(matrix[c][k] / self.s[c]): 
                        vMayor = abs(matrix[c][k] / self.s[c])
                        pMayor = c
                if vMayor != 0:
                    temp = matrix[pMayor]
                    matrix[pMayor] = matrix[k]
                    matrix[k] = temp
                    for i in range(k+1, len(matrix), 1):
                        M = matrix[i][k]/matrix[k][k]
                        for j in range(len(matrix)+1):
                            matrix[i][j] = matrix[i][j]- M*matrix[k][j] 
                        self.imprimirMatriz(matrix)
                    vMayor = 0.0
                    pMayor = 0
                else:
                    self.result.append("No valid matrix o div wth 0")
                    break
                self.imprimirMatriz(matrix)
                self.new = matrix
                if(self.check_diagonal(self.new)):
                    self.variable_resolution()
                    self.row_definition()
                else:
                    self.result.append("No solutions or infinite solutions or Div 0")

                self.imprimirMatriz(matrix)
        
    def check_diagonal(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(j==i):
                    self.result.append(0)
                    if(matrix[i][j]==0):
                        print("falso en el valor: "+str(matrix[i][j]))
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
        for i in range(0,len(matrix),1):
            print(i)
            print("matrix" + str(matrix[i]))
            print("append" + str(matrixb[0][i]))
            matrix[i].append(matrixb[0][i])
        return matrix

    def row_definition(self):
        self.rows = []
        for i in range(1,(len(self.new)+1)):
            self.rows.append(f"x{i}")
        self.rows.append("b")

    def imprimirMatriz(self, A):
        for i in range(len(A)):
            print(A[i])

    def busquedaDelMayorDeCadaFila(self, A):
        for i in range(len(A)):
            for j in range(len(A)):
                if abs(A[i][j])> self.s[i]:
                    self.s[i] = abs(A[i][j])

    def value_table(self):
        self.total = []
        print("*** NEW ***"+str(len(self.new[0])))
        for i in range(len(self.new)):
            self.total.append([])
            for j in range(len(self.new[i])):
                self.total[i].append(Decimal(self.new[i][j]))
        print("*** TOTAL ***"+str(len(self.total)))
        return self.total

    def get_results(self):
        results=""
        aux=1
        for i in range(len(self.new)):
            results+=f"X{aux}: "+(str)(self.result[i])+"\n"
            aux+=1
        return results

#[2,1,1]
#[4,-6,0]
#[-2,7,2]
#[5,-2,9]
