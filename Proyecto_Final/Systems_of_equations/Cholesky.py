
import copy
import math
from decimal import *

class Cholesky:

    def __init__(self):
        self.matrixAB = []
        self.original = []
        self.matrixL = []
        self.matrixU = []
        self.result = []

    def cholesky_algorithm(self,matrixA,matrixB =[]):
        
        self.original = copy.deepcopy(matrixA)
        self.matrixL = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        self.matrixU = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        print('MatrixA')
        self.printMatrix(matrixA)
        print('MatrixL')
        self.printMatrix(self.matrixL)
        print('MatrixU')
        self.printMatrix(self.matrixU)


        self.__getMatrices(matrixA)

        print('MatrixL')
        self.printMatrix(self.matrixL)
        print('MatrixU')
        self.printMatrix(self.matrixU)

    def __getMatrices(self,matrixA):
        stages = len(matrixA)

        for stage in range(stages):
            for row in range(stage,stages):
                valuesSumU = 0
                valuesSumL = 0
                for col in range(0,stage+1):
                    #valuesSum+=self.matrixL[row][col]*self.matrixU[col][row]
                    valuesSumU+=self.matrixL[stage][col]*self.matrixU[col][row]
                    valuesSumL+=self.matrixL[row][col]*self.matrixU[col][stage]
                    #print(type(valuesSumU))
                
                if(row==stage):
                    #print(self.matrixL)
                    val =matrixA[stage][stage]-valuesSumL
                    self.matrixL[stage][stage] = math.sqrt(val)
                    self.matrixU[stage][stage] = self.matrixL[stage][stage]
                    #print(self.matrixL)
                else:
                    self.matrixL[row][stage] = (matrixA[row][stage] - valuesSumL)/self.matrixL[stage][stage]
                    self.matrixU[stage][row] = (matrixA[stage][row] - valuesSumU)/self.matrixL[stage][stage]
                '''
                print(f"Row {row}")
                print('MatrixL')
                self.printMatrix(self.matrixL)
                print('MatrixU')
                self.printMatrix(self.matrixU)
                s = input('')
                '''
        
    def printMatrix(self,matrix):
        for i in matrix:
            print(i)

if __name__ == "__main__":
    ch = Cholesky()
    a =[[34,-5,-7,-8],[-5,23,-4,-8],[-5,-6,45,17],[-3,-7,9,67]]
    ch.cholesky_algorithm(a)







