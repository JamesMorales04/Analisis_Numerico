
import copy
class partial_Pivoting:
    def __init__(self):
        self.original= []
        self.new = []
        self.total= []
        self.result=[]
        self.rows = []
        getcontext().prec = 25

    def partial_pivoting_algorithm(self,matrix,matrixb):
        matrix=self.merge(matrix,matrixb)
        self.original=copy.deepcopy(matrix)
        column=0
        no_error=True
        i=1
        lenght=len(matrix)
        n=0
        while n < lenght: 
            pos=n  
            bigger=matrix[n][n]
            for i in range (n+1,lenght):
                if (abs(matrix[i][n]) > bigger):
                    bigger= matrix[i][n]
                    pos = i
            temp=matrix[n]
            big=matrix[pos] 
            matrix[n]=big
            matrix[pos]=temp #SWAP
            row=n+1
            for i in range (row,lenght):
                multiplier=matrix[i][column]/matrix[row-1][column] 
                for j in range(column,len(matrix[i])):                      
                    matrix[i][j]=matrix[i][j]-matrix[row-1][j]*multiplier             
            n+=1
            column+=1

        if(self.check_diagonal()):
            self.variable_resolution()
            self.row_definition()
        else:
            self.result="No tiene solucion o posee infinitas soluciones"

        for i in self.new:
            print(i)
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
#[2,1,1]
#[4,-6,0]
#[-2,7,2]
#[5,-2,9]

#cosa.partial_pivoting_algorithm([[1/4,1/5,1/6,1/7],[1/3,1/4,1/5,1/6],[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5]],[60,70,106,84])