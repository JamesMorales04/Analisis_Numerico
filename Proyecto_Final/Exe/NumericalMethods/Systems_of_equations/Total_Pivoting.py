import copy
from decimal import *

class Total_Pivoting:

    def __init__(self):

        self.matrixAB = []
        self.original = []
        self.xVarsCols = []
        self.rows = []
        self.total = []
        self.result = []
        self.greater = 0
        self.errorMessage = ''
    
    def total_pivoting_algorithm(self,matrixA = [],matrixB = []):

        self.errorMessage = ''

        if(len(matrixB)!=0 and len(matrixA)!=0 and len(matrixB[0])!=0):

            if(len(matrixA)==len(matrixB[0])):

                self.matrixAB = self.__merge(matrixA,matrixB)
                self.original = copy.deepcopy(self.matrixAB)
                stages = len(matrixA)
                error = False
                
                for i in range(stages):
                    self.xVarsCols.append(i)
                
                for stage in range(stages-1):
                    row, col = self.__LocateGreatestValue(stage,stages)
                    if(self.greater != 0):
                        self.__SwitchRow(stage,row)
                        self.__SwitchCol(stage,stages,col)
                        self.__GaussianReduction(stage,stages)
                    else:
                        error = True
                        break
                if(error):
                    self.errorMessage = 'Error: The equation sistem has no solution or has infinite solutions'
                else:
                    self.__getVarsValues()
                    self.row_definition()
            else:
                self.errorMessage = 'Error: The number of equations doesnt match the number of variables'
        else:
            self.errorMessage = 'Error: The required matrixes where not passed'
    
    def __getVarsValues(self):

        numRows = len(self.matrixAB)-1
        self.result = [0]*len(self.xVarsCols)
        indx = self.xVarsCols[-1]

        if(self.matrixAB[-1][-2]!=0):
            self.result[indx] = self.matrixAB[-1][-1]/self.matrixAB[-1][-2]
            for row in range(numRows-1,-1,-1):
                if(self.matrixAB[row][row]!=0):
                    totalSum = 0
                    for col in range(numRows,row,-1):
                        indx = self.xVarsCols[col]
                        totalSum+= self.result[indx]*self.matrixAB[row][col]
                    indx = self.xVarsCols[row]
                    self.result[indx] = (self.matrixAB[row][-1]-totalSum)/self.matrixAB[row][row]
                else:
                    self.errorMessage = 'Error. The given sistem has infinite solutions'
                    break
        else:
            self.errorMessage = 'Error. The given sistem has infinite solutions'
    
    def __GaussianReduction(self,stage,stages):
        
        for row in range(stage+1,stages):
            multiplier = self.matrixAB[row][stage]/self.matrixAB[stage][stage]
            for col in range(stage,stages+1):
                self.matrixAB[row][col] += -multiplier*self.matrixAB[stage][col]
    
    '''
    Debugging tool
    def printMatrix(self):

        for i in self.matrixAB:
            print(i)
    ''' 
    def __SwitchRow(self,stage,row):

        if(stage != row):
            oldStageRow = self.matrixAB[stage]
            self.matrixAB[stage] = self.matrixAB[row]
            self.matrixAB[row] = oldStageRow

    def __SwitchCol(self,stageCol,rows,col):

        if(stageCol!=col):
            oldStageCol = []
            for i in range(rows):
                oldStageCol = self.matrixAB[i][stageCol]
                self.matrixAB[i][stageCol] = self.matrixAB[i][col]
                self.matrixAB[i][col] = oldStageCol
            
            oldVarInStage = self.xVarsCols[stageCol]
            self.xVarsCols[stageCol] = self.xVarsCols[col]
            self.xVarsCols[col] = oldVarInStage
        
    def __LocateGreatestValue(self,stage,stages):

        location = (0,0)
        self.greater = 0

        for row in range(stage,stages):
            for col in range(stage,stages):
                if(abs(self.matrixAB[row][col])>abs(self.greater)):
                    self.greater = self.matrixAB[row][col]
                    location = (row,col)
        return location[0],location[1]


    def __merge(self,matrixA,matrixB):

        for row in range(len(matrixA)):
            matrixA[row].append(matrixB[0][row])

        return matrixA

    def row_definition(self):

        for i in range(1,len(self.result)+1):
            self.rows.append(f"x{i}")
        self.rows.append("b")
        self.rows.append("///")
        for i in range(1,len(self.result)+1):
            self.rows.append(f"x{i}")
        self.rows.append("b")

    def value_table(self):
        for i in range(0,len(self.matrixAB)):
            self.total.append([])
            for j in range(0,len(self.matrixAB[i])):
                self.total[i].append(Decimal(self.original[i][j]))
            self.total[i].append("///")
            for j in range(0,len(self.matrixAB[i])):
                self.total[i].append(Decimal(self.matrixAB[i][j]))

        #print(self.total)
        return self.total

    def get_results(self):

        if(len(self.errorMessage) == 0):
            results=""
            aux=1
            for i in self.result:
                results+=f"X{aux}: "+(str)(i)+"\n"
                aux+=1
            return results
        else:
            return self.errorMessage

if __name__ == "__main__":
    tp = Total_Pivoting()
    a = [[2,-3,4,1],[-4,2,1,-2],[1,3,-5,3],[-3,-1,1,-1]]
    b = [[10,-10,32,-21]]
    tp.total_pivoting_algorithm(a,b)