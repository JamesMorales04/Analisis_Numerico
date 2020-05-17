import copy
from decimal import *

class Total_Pivoting:
    def __init__(self):
        self.matrixAB = []
        self.original = []
        self.new = []
        self.result = []
        self.greater = 0
    
    def total_pivoting_algorithm(self,matrixA = [],matrixB = []):

        if(len(matrixA)==0 or len(matrixB)==0):
            return 'The required matrixes where not passed'
        if(len(matrixA)<len(matrixB)):
            return 'The number of equations doesnt match the number of variables'
        
        self.matrixAB = self.__merge(matrixA,matrixB)
        self.original = copy.deepcopy(self.matrixAB)
        stages = len(matrixA)
        
        for stage in range(stages):
            #
            row, col = self.__LocateGreatestValue(stage,stages)
            print(str(row)+'       '+str(col))
        
        print(self.matrixAB[3][3]) 
    
    def __LocateGreatestValue(self,stage,stages):

        location = (0,0)

        for i in range(stage,stages):
            for j in range(stage,stages):
                if(abs(self.matrixAB[i][j])>self.greater):
                    self.greater = self.matrixAB[i][j]
                    location = (i,j)
        
        return location[0],location[1]


    def __merge(self,matrixA,matrixB):
        for row in range(len(matrixA)):
            matrixA[row].append(matrixB[row])

        print(matrixA)
        return matrixA

if __name__ == "__main__":
    tp = Total_Pivoting()
    a = [[1,2,3,4],[4,5,6,7],[9,7,6,5],[10048,11,111,345]]
    b = [1,2,3,4]
    tp.total_pivoting_algorithm(a,b)