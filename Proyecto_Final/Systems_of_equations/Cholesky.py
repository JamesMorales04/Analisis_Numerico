
import copy
import math
from decimal import *

class Cholesky:

    def __init__(self):
        self.matrixA = []
        self.matrixAB = []
        self.original = []
        self.total = []
        self.matrixL = []
        self.matrixU = []
        self.matrixUZ = []
        self.matrixLB = []
        self.resultX = []
        self.resultZ = []
        self.stateLU = 0
        self.LUOutput = ''
        self.errorMessage = ''
        self.rows = []
        getcontext().prec = 25

    def cholesky_algorithm(self,matrixB=[[]]):
        
        self.errorMessage = ''
        if(len(matrixB)!=0 and len(self.matrixA)==len(matrixB[0])):
            copyMatrixA = copy.deepcopy(self.matrixA)
            self.original = copy.deepcopy(self.__merge(copyMatrixA,matrixB))
            
            if(self.stateLU==0):
                matrixLCopy = copy.deepcopy(self.matrixL)
                self.matrixLB = self.__merge(matrixLCopy,matrixB)

                self.__getVarsValuesZ()

                matrixUCopy = copy.deepcopy(self.matrixU)
                self.matrixUZ = self.__merge(matrixUCopy,self.resultZ)
                
                self.__getVarsValuesX()
                self.row_definition()
            elif(self.stateLU==-1):
                self.errorMessage = 'Error: Invalid input led to a division by Zero'
            elif(self.stateLU==-2):
                self.errorMessage = 'Error: Invalid input'
        elif (len(matrixB)==0):
            self.errorMessage = 'Error: Invalid input in matrix B'
        else:
            self.errorMessage = 'Error: Incompatible number of rows in A and values in B due to invalid inputs or missing values'

    def getMatrices(self,matrixA):
        stages = len(matrixA)
        if(stages==0):
            self.stateLU = -2
            self.LUOutput = 'Error: No matrix A was entered'
            return -2
        
        self.matrixA = copy.deepcopy(matrixA)
        self.matrixL = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        self.matrixU = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]

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
            
            self.LUOutput = 'No error while generating matrices L and U'
            self.stateLU= 0

        except DivisionByZero as zeros:
            self.stateLU= -1
            self.LUOutput = 'Error: Invalid A Matrix'
        except TypeError as e:
            self.stateLU=-2
            self.LUOutput = 'Error: Invalid A Matrix'
        except Exception as e:
            self.stateLU=-2
            self.LUOutput = 'Error Invalid A Matrix'
        
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
        if(self.errorMessage==''):
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
        else:
            return []
    
    def get_results(self):

        if(len(self.errorMessage)==0):
            results=""
            aux=1
            for i in self.resultX:
                results+=f"X{aux}: "+(str)(i)+"\n"
                aux+=1
            return results
        else:
            return self.errorMessage

if __name__ == "__main__":
    ch = Cholesky()
    a =[[8,2,2,5],[4,5,7,-8],[-4,7,12,11],[8,-3,-11,28]]
    b = [[-12,13,31,-32]]
    #a = [[2,-3,4,1],[-4,2,1,-2],[1,3,-5,3],[-3,-1,1,-1]]
    ch.getMatrices(a)
    print('State LU .'+ch.LUOutput)
    print(ch.stateLU)
    #b = [[10,-10,32,-21]]
    ch.cholesky_algorithm(b)
    print(ch.resultX)







