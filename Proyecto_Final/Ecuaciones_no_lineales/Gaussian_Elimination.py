import copy
class Gaussian_Elimination:
    def __init__(self):
        self.original=[]
        self.new=[]
        self.result=[]

    def gaussian_elimination_algorithm(self,matrix):
        self.original=copy.deepcopy(matrix)
        column=0
        no_error=True
        i=1
        while i <= len(matrix) and no_error:
            for j in range(i,len(matrix)):
                multiplier=matrix[j][column]/matrix[i-1][column]
                for k in range(column,len(matrix[j])):
                    matrix[j][k]=matrix[j][k]-matrix[i-1][k]*multiplier            
            column+=1
            i+=1 
        self.new=matrix

        if(self.check_diagonal()):
            self.variable_resolution()
        else:
            self.result="No tiene solucion o posee infinitas soluciones"

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
    def tabla_valores(self):
        return self.valores


cosa=Gaussian_Elimination()
cosa.gaussian_elimination_algorithm([[2,-3,4,1,10],[-4,2,1,-2,-10],[1,3,-5,3,32],[-3,-1,1,-1,-21]])
