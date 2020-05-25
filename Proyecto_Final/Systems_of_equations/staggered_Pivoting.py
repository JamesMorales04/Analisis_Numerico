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
        elif self.check_diagonal:
            self.result.append("No valid matrix")
        else:
            print("len matrix b is :"+ str(len(matrixb)))
            matrix=self.merge(matrix,matrixb)
            self.imprimirMatriz(matrix)
            self.original=copy.deepcopy(matrix)
            no_error=True
            for i in range(len(matrix)):
                self.s.append(0)
            self.busquedaDelMayorDeCadaFila(matrix)
            mayor = []
            pMayor = 0
            vMayor = 0.0
            temp = []
            if(vMayor == 0):
                self.result.append("No solutions or infinite solutions or Div 0")
            else:
                for k in range(len(matrix)):
                    for c in range(k, len(matrix), 1):
                        mayor.append(abs(matrix[c][k] / self.s[c]))
                        if vMayor <= abs(matrix[c][k] / self.s[c]): 
                            vMayor = abs(matrix[c][k] / self.s[c])
                            pMayor = c
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
                self.imprimirMatriz(matrix)
                self.new= matrix
                if(self.check_diagonal()):
                    self.variable_resolution()
                    self.row_definition()
                else:
                    self.result.append("No solutions or infinite solutions or Div 0")
                self.imprimirMatriz(matrix)
        
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
        for i in range(0,len(matrix),1):
            print(i)
            print("matrix" + str(matrix[i]))
            print("append" + str(matrixb[0][i]))
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

    def imprimirMatriz(self, A):
        for i in range(len(A)):
            print(A[i])

    def busquedaDelMayorDeCadaFila(self, A):
        for i in range(len(A)):
            for j in range(len(A)):
                if abs(A[i][j])> self.s[i]:
                    self.s[i] = abs(A[i][j])

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

#[2,1,1]
#[4,-6,0]
#[-2,7,2]
#[5,-2,9]
