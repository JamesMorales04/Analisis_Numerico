from decimal import *
import copy

class Doolittle:
    def __init__(self):
        self.l= []
        self.original= []
        self.u= []
        self.new = []
        self.total= []
        self.result=[]
        self.rows = []
        getcontext().prec = 25

    def doolittle_algorithm(self,matrix,matrixb):
        matrix=self.merge(matrix,matrixb)
        self.original=matrix
        length= len(matrix)
        for i in range (length):
            self.l.append([0] * length)
            self.u.append([0] * length)
            self.l[i][i] = 1
        for k in range(length):
            for j in range(k,length):
                sum = 0
                for p in range(k):
                    sum += self.l[k][p]*self.u[p][j]
                self.u[k][j] = (self.original[k][j] - sum)/self.l[k][k]
            for i in range(k,length):
                sum = 0
                for p in range(k):
                    sum += self.l[i][p]*self.u[p][k]
                self.l[i][k] = (self.original[i][k] - sum)/self.u[k][k]
        for i in range (0,length):
            self.l[i][i] = 1        
        print (self.l)

        print("-------------")

        print(self.u)
        print("-------------")

        print(self.original)

        self.new = self.merge(self.u,matrixb)

        if(self.check_diagonal()):
            self.variable_resolution()
            self.row_definition()
        else:
            self.result="No tiene solucion o posee infinitas soluciones"
        print(self.result)   

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
        self.rows.append("///")
        for i in range(1,len(self.result)+1):
            self.rows.append(f"x{i}")
        self.rows.append("///")
        for i in range(1,len(self.result)+1):
            self.rows.append(f"x{i}")

    def value_table(self):
        for i in range(0,len(self.original)):
            self.total.append([])
            for j in range(len(self.original)):
                self.total[i].append(Decimal(self.l[i][j]))
            self.total[i].append("///")
            for j in range(len(self.new)):
                self.total[i].append(Decimal(self.new[i][j]))
            self.total[i].append("///")
            for j in range(len(self.u)):
                self.total[i].append(Decimal(self.original[i][j]))
        return self.total

    def get_results(self):
        results=""
        aux=1
        for i in self.result:
            results+=f"X{aux}: "+(str)(i)+"\n"
            aux+=1
        return results
#n= Doolittle()
#n.doolittle_algorithm([[45,-3,-4],[-12,36,7],[-6,4,57],[-3,-5,-10]],[8,-5,-8,78])