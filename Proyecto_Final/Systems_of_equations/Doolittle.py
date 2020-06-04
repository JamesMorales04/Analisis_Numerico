from decimal import *
import copy

class Doolittle:
    def __init__(self):
        self.l= []
        self.l_aux=[]
        self.original= []
        self.u= []
        self.uaux=[]
        self.new = []
        self.newaux=[]
        self.total= []
        self.result=[]
        self.rows = []
        self.xvalues=[]
        self.stepsL=[]
        self.stepsU=[]
        self.steps_row= []
        self.lsolution = []
        self.no_error=True
        self.times=0
        getcontext().prec = 25

    def doolittle_algorithm(self,matrr):
        matrix= []
        for i in range(0,len(matrr)):
            matrix.append(matrr[i])
        self.original=matrix
        length= len(matrix)
        for i in range (length):
            self.l.append([0] * length)
            self.u.append([0] * length)
            self.l[i][i] = 1
            self.xvalues.append([0] * length)
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
            self.stepsL.append(copy.deepcopy(self.l))
            self.stepsU.append(copy.deepcopy(self.u))
        print(self.stepsL)
        for i in range (0,length):
            self.l[i][i] = 1        
        self.l_aux=self.l
        self.get_steps()

                  

    def progresiveL(self,matrixb):
        answerZ=[] 
        answerZ.append(matrixb[0][0])
        for i in range (1,len(matrixb[0])):
            aux=matrixb[0][i]
            j=0
            while j!=i: #If it is not the diagonal, continue subbing
                aux-=self.l[i][j]*answerZ[j]
                j+=1
            answerZ.append(aux)
        return answerZ #It is perfect

    def variable_resolution(self):
        self.newaux= self.new
        self.newaux.reverse()
        for i in range (len(self.newaux)):
            self.newaux[i].reverse()  #Reverse is okay.
        answerX=[]
        answerX.append(self.newaux[0][0]/self.newaux[0][1]) #Añadiendo x1...

        for i in range (1,len(self.newaux)):
            aux=self.newaux[i][0] 
            j=1
            while (j!=(i+1)):
                aux-=self.newaux[i][j]*answerX[j-1] 
                j+=1
            if j<=(len(self.newaux)):
                aux/=self.newaux[i][j] 
                answerX.append(aux)
            
        #It is perfect
        answerX.reverse() 
        for i in range(len(self.xvalues)):
            self.xvalues[i][i] = answerX[i] #Valores de x

    def merge(self,matrix,matrixb):
        for i in range(0,len(matrix)):
            self.uaux[i].append(matrixb[i])
        return self.uaux


    def runb(self,matrixb):
        self.uaux= copy.deepcopy(self.u)
        self.xvalues=[]
        self.lsolution=[]
        self.new=[]
        for i in range (len(matrixb[0])):
            self.xvalues.append([0] * len(matrixb[0]))
        self.total=[]
        self.rows=[]
        self.lsolution=self.progresiveL(matrixb)
        self.new = self.merge(self.uaux,self.lsolution) #merge with u with the solution created  

        self.variable_resolution()
        self.row_definition()  

    def row_definition(self):
        for i in range(1,len(self.xvalues)+1):
            self.rows.append(f"x{i}")
        self.rows.append("///")
        for i in range(1,len(self.xvalues)+1):
            self.rows.append(f"x{i}")
        self.rows.append("z")
        self.rows.append("///")
        for i in range(1,len(self.xvalues)+1):
            self.rows.append(f"x{i}")

    def value_table(self):
        for i in range (len(self.uaux)):
            self.uaux[i].reverse() #Reverse it again
        self.uaux.reverse()

        for i in range(0,len(self.original)):
            self.total.append([])
            for j in range(len(self.l[0])):
                self.total[i].append(Decimal(self.l[i][j]))
            self.total[i].append("///")
            for j in range(len(self.uaux[0])):
                self.total[i].append(Decimal(self.uaux[i][j]))
            self.total[i].append("///")
            for j in range(len(self.xvalues[0])):
                self.total[i].append(Decimal(self.xvalues[i][j]))
        return self.total

    def get_steps(self):
        aux=[]
        for i in range(0,len(self.stepsL)):
            aux.append([f"Matrix L: Step{i}"])
            for j in self.l[i]:
                aux.append(j)
            aux.append([f"Matrix U: Step{i}"])
            for j in self.stepsU[i]:
                aux.append(j)

        for i in range(1,len(self.l[0])+1):
            self.steps_row.append(f"x{i}")
        self.stepsL=aux
    def get_steps_table(self):
        return self.stepsL

    def get_steps_rows(self):
        return self.steps_row

    def get_results(self):
        results=""
        aux=1
        num=0
        for i in self.xvalues:
            results+=f"X{aux}: "+(str)(i[num])+"\n"
            aux+=1
            num+=1
        return results
 
    def get_total(self):
        return self.total

    def get_noerror(self):
        return self.no_error


#n= Doolittle()
#n.doolittle_algorithm([[45,-3,-4],[-12,36,7],[-6,4,57],[-3,-5,-10]],[8,-5,-8,78])
"""
[45,-3,-7,8]
[-12,36,9,-5]
[-6,4,57,-8]
[-3,-5,-10,78]

[100,-50,300,53]
"""