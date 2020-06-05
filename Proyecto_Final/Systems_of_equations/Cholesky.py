
import copy
import math
from decimal import *

class Cholesky:

    def __init__(self):
        self.matrixA = []
        self.matrixAB = []
        self.original = []
        self.total = []
        self.totalStepsL = []
        self.totalStepsU = []
        self.stepsL = []
        self.stepsU = []
        self.matrixL = []
        self.matrixU = []
        self.matrixUZ = []
        self.matrixLB = []
        self.resultX = []
        self.resultZ = []
        self.stateLU = 0
        self.LUOutput = ''
        self.errorMessage = ''
        self.startSolutionIndx = 0
        self.rows = []
        getcontext().prec = 25

    def cholesky_algorithm(self,matrixB=[[]]):
        
        self.errorMessage = ''
        self.startSolutionIndx = len(self.total)
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
        
        self.total =[]
        tempMatrixB = [[f"B{b+1}" for b in range(stages)]]
        self.original = self.__merge(copy.deepcopy(matrixA),tempMatrixB)
        self.matrixA = copy.deepcopy(matrixA)
        self.matrixL = [[0 for x in range(stages)] for y in range(stages)]
        self.matrixU = [[0 for x in range(stages)] for y in range(stages)]
        self.resultX = [f"X{x+1}" for x in range(stages)]
        self.resultZ = [[f"Z{z+1}" for z in range(stages)]]
        self.stepsL = [[0 for x in range(stages)] for y in range(stages)]
        self.stepsU = [[0 for x in range(stages)] for y in range(stages)]
        self.fillStepsLU()
        self.value_table()

        try:
            for stage in range(stages):
                for row in range(stage,stages):
                    valuesSumU = 0
                    valuesSumL = 0
                    for col in range(0,stage+1):
                        if(not isinstance(self.matrixL[stage][col],str)):
                            valuesSumU+=self.matrixL[stage][col]*self.matrixU[col][row]
                            valuesSumL+=self.matrixL[row][col]*self.matrixU[col][stage]


                    if(row==stage):
                        val =matrixA[stage][stage]-valuesSumL
                        self.matrixL[stage][stage] = math.sqrt(val)
                        self.stepsL[stage][stage] = self.matrixL[stage][stage]
                        self.matrixU[stage][stage] = self.matrixL[stage][stage]
                        self.stepsU[stage][stage] = self.matrixU[stage][stage]
                    else:
                        self.matrixL[row][stage] = (matrixA[row][stage] - valuesSumL)/self.matrixL[stage][stage]
                        self.stepsL[row][stage] = self.matrixL[row][stage]
                        self.matrixU[stage][row] = (matrixA[stage][row] - valuesSumU)/self.matrixL[stage][stage]
                        self.stepsU[stage][row] = self.matrixU[stage][row]
                    
                    self.value_table()
            
            self.LUOutput = 'No error while generating matrices L and U'
            self.stateLU= 0

        except DivisionByZero as zeros:
            self.stateLU= -1
            print(e)
            self.LUOutput = 'Error: Invalid A Matrix'
        except TypeError as e:
            self.stateLU=-2
            print(e)
            self.LUOutput = 'Error: Invalid A Matrix'
        except Exception as e:
            self.stateLU=-2
            print(e)
            self.LUOutput = 'Error Invalid A Matrix'
        
    def printMatrix(self,matrix):
        for i in matrix:
            print(i)
            
    def fillStepsLU(self):
        for i in range(len(self.matrixL)):
            self.stepsL[i][i] = f"L{i+1}{i+1}"
            for j in range(i):
                self.stepsL[i][j] =f"L{i+1}{j+1}"

        for i in range(len(self.matrixU)):
            for j in range(i,len(self.matrixU)):
                self.stepsU[i][j] = f"U{i+1}{j+1}"

    def __getVarsValuesZ(self):

        numRows = len(self.matrixLB)
        self.resultZ = [[0 for x in range(numRows)]]                 #Pay attention here
        self.resultZ[0][0] = (self.matrixLB[0][-1])/self.matrixLB[0][0]
        for row in range(numRows):
            total = 0
            for varValue in range(0,row):
                total+=self.resultZ[0][varValue]*self.matrixLB[row][varValue]
            
            self.resultZ[0][row] = (self.matrixLB[row][-1]-total)/self.matrixLB[row][row]
            self.value_table()

    def __getVarsValuesX(self):

        numRows = len(self.matrixUZ)-1
        self.resultX = [0 for x in range(numRows+1)]
        self.resultX[-1] = (self.matrixUZ[-1][-1])/self.matrixUZ[-1][-2]

        for row in range(numRows,-1,-1):
            total = 0
            for varValue in range(numRows,row,-1):
                total+=self.resultX[varValue]*self.matrixUZ[row][varValue]
            self.resultX[row] = (self.matrixUZ[row][-1]-total)/self.matrixUZ[row][row]
            self.value_table()


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
    
    def getSteps(self):
        if(self.errorMessage==''):
            returnVals = copy.deepcopy(self.total)
            for i in range(len(self.total)-1,self.startSolutionIndx-1,-1):
                self.total.pop(i)
            self.rows = []
            return returnVals
        else:
            return []

    def value_table(self):
        if(self.errorMessage==''):
            lastRow = len(self.total)-1
            for i in range(0,len(self.original)):
                self.total.append([])
                lastRow+=1
                for j in range(0,len(self.original[i])):
                    if(isinstance(self.original[i][j],str)):
                        self.total[lastRow].append(self.original[i][j])
                    else:
                        self.total[lastRow].append(Decimal(self.original[i][j]))
                self.total[lastRow].append("///")
                for j in range(0,len(self.matrixL)):
                    if(isinstance(self.stepsL[i][j],str)):
                        self.total[lastRow].append(self.stepsL[i][j])
                    else:
                        self.total[lastRow].append(Decimal(self.stepsL[i][j]))
                if(isinstance(self.resultZ[0][i],str)):
                    self.total[lastRow].append(self.resultZ[0][i])
                else:
                    self.total[lastRow].append(Decimal(self.resultZ[0][i]))
                self.total[lastRow].append("///")    
                for j in range(0,len(self.matrixU)):
                    if(isinstance(self.stepsU[i][j],str)):
                        self.total[lastRow].append(self.stepsU[i][j])
                    else:
                        self.total[lastRow].append(Decimal(self.stepsU[i][j]))
                if(isinstance(self.resultX[i],str)):
                    self.total[lastRow].append(self.resultX[i])
                else:
                    self.total[lastRow].append(Decimal(self.resultX[i]))
            
            self.fillDivisionPerPhase()
            return self.total
        else:
            return []
    
    def fillDivisionPerPhase(self):

        spaceRow = [' ' for col in range(len(self.total[0]))]
        self.total.append(spaceRow)
        self.total.append(spaceRow)
        
    
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
    #a =[[8,2,2,5],[4,5,7,-8],[-4,7,12,11],[8,-3,-11,28]]
    #b = [[-12,13,31,-32]]
    #a = [[2,-3,4,1],[-4,2,1,-2],[1,3,-5,3],[-3,-1,1,-1]]

    a = [[34,-5,-7,-8],[-5,23,-4,-8],[-5,-6,45,17],[-3,-7,9,67]]
    b=[[100,200,300,-500]]
    ch.getMatrices(a)
    #ch.printMatrix(ch.stepsL)
    #print('---------------------')
    #ch.printMatrix(ch.stepsU)

    #ch.printMatrix(ch.total)
    #print('--------------')
    #ch.printMatrix(ch.matrixL)
    #ch.printMatrix(ch.matrixU)

    #b = [[10,-10,32,-21]]
    ch.cholesky_algorithm(b)

    #print(len(ch.total[0]))

    #print('--------------')
    #ch.printMatrix(ch.stepsL)
    #ch.printMatrix(ch.stepsU)
    #print(ch.resultX)







