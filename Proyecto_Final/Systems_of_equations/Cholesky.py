
import copy
import math
from decimal import *

class Cholesky:

    def __init__(self):
        self.matrixAB = []
        self.original = []
        self.total = []
        self.matrixL = []
        self.matrixU = []
        self.matrixUZ = []
        self.matrixLB = []
        self.resultX = []
        self.resultZ = []
        self.rows = []
        getcontext().prec = 25

    def cholesky_algorithm(self,matrixA,matrixB =[]):
        
        print('MatrixA')
        print(matrixA)
        print('MatrixB')
        print(matrixB)
        self.original = copy.deepcopy(self.__merge(matrixA,matrixB))
        self.matrixL = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        self.matrixU = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        '''
        print('MatrixA')
        self.printMatrix(matrixA)
        print('MatrixL')
        self.printMatrix(self.matrixL)
        print('MatrixU')
        self.printMatrix(self.matrixU)
        '''


        error = self.__getMatrices(matrixA)
        if(error==0):
            matrixLCopy = copy.deepcopy(self.matrixL)
            self.matrixLB = self.__merge(matrixLCopy,matrixB)
            #print('\nMatrixLB')
            self.printMatrix(self.matrixLB)
            self.__getVarsValuesZ()
            #print('\nZ')
            #print(self.resultZ)
            matrixUCopy = copy.deepcopy(self.matrixU)
            self.matrixUZ = self.__merge(matrixUCopy,self.resultZ)
            
            #print('\nMatrixUZ')
            self.printMatrix(self.matrixUZ)
            
            self.__getVarsValuesX()
            #print('\nX')
            #print(self.resultX)
            
            #Factorization
            #print('\nMatrixL')
            self.printMatrix(self.matrixL)
            #print('\nMatrixU')
            self.printMatrix(self.matrixU)

            self.row_definition()
            #print(len(self.rows))

        
        else:
            return 'Problem while factorizing the matrix'

    def __getMatrices(self,matrixA):
        stages = len(matrixA)

        try:
            for stage in range(stages):
                for row in range(stage,stages):
                    valuesSumU = 0
                    valuesSumL = 0
                    for col in range(0,stage+1):
                        valuesSumU+=self.matrixL[stage][col]*self.matrixU[col][row]
                        valuesSumL+=self.matrixL[row][col]*self.matrixU[col][stage]

                    if(row==stage):
                        val =matrixA[stage][stage]-valuesSumL
                        self.matrixL[stage][stage] = math.sqrt(val)
                        self.matrixU[stage][stage] = self.matrixL[stage][stage]
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
            return 0

        except DivisionByZero as zeros:
            print(zeros)
            return -1
        except Exception as e:
            print(e)
            return -2
        
    def printMatrix(self,matrix):
        for i in matrix:
            print(i)

    def __getVarsValuesZ(self):

        numRows = len(self.matrixLB)
        self.resultZ = [[0 for x in range(numRows)]]
        self.resultZ[0][0] = (self.matrixLB[0][-1])/self.matrixLB[0][0]
        for row in range(numRows):
            total = 0
            for varValue in range(0,row):
                total+=self.resultZ[0][varValue]*self.matrixLB[row][varValue]
            self.resultZ[0][row] = (self.matrixLB[row][-1]-total)/self.matrixLB[row][row]

    def __getVarsValuesX(self):

        numRows = len(self.matrixUZ)-1
        self.resultX = [0 for x in range(numRows+1)]
        self.resultX[-1] = (self.matrixUZ[-1][-1])/self.matrixUZ[-1][-2]

        for row in range(numRows,-1,-1):
            total = 0
            for varValue in range(numRows,row,-1):
                total+=self.resultX[varValue]*self.matrixUZ[row][varValue]
            self.resultX[row] = (self.matrixUZ[row][-1]-total)/self.matrixUZ[row][row]


    def __merge(self,matrixA,matrixB):

        for row in range(len(matrixA)):
            matrixA[row].append(matrixB[0][row])

        return matrixA
        
    def row_definition(self):
        numRows = len(self.resultX)
        for i in range(1,numRows+1):
            self.rows.append(f"A{i}")
        self.rows.append("B")
        self.rows.append("///")
        for i in range(1,numRows+1):
            self.rows.append(f"L{i}")
        self.rows.append("Z")
        self.rows.append("///")
        for i in range(1,numRows+1):
            self.rows.append(f"U{i}")
        self.rows.append("X")

    def value_table(self):
        for i in range(0,len(self.original)):
            self.total.append([])
            for j in range(0,len(self.original[i])):
                self.total[i].append(Decimal(self.original[i][j]))
            self.total[i].append("///")
            for j in range(0,len(self.matrixL)):
                self.total[i].append(Decimal(self.matrixL[i][j]))
            self.total[i].append(Decimal(self.resultZ[0][i]))
            self.total[i].append("///")    
            for j in range(0,len(self.matrixU)):
                self.total[i].append(Decimal(self.matrixU[i][j]))
            self.total[i].append(Decimal(self.resultX[i]))
        return self.total
    
    def get_results(self):
        results=""
        aux=1
        for i in self.resultX:
            results+=f"X{aux}: "+(str)(i)+"\n"
            aux+=1
        return results

if __name__ == "__main__":
    ch = Cholesky()
    a =[[8,2,2,5],[4,5,7,-8],[-4,7,12,11],[8,-3,-11,28]]
    b = [[-12,13,31,-32]]
    ch.cholesky_algorithm(a,b)







