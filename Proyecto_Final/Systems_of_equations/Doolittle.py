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
        self.xvalues=[]
        getcontext().prec = 25

    def doolittle_algorithm(self,matrr,matrixb):
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
        for i in range (0,length):
            self.l[i][i] = 1        
        
        lsolution=self.progresiveL(matrixb)
        self.new = self.merge(self.u,lsolution) #Hacemos merge de la u con la solución que creé yo para mandarlo al método de James que lo resuelve 
        self.variable_resolution()
        self.row_definition()            

    def progresiveL(self,matrixb):
        answerZ=[] #Progresivo simple con matriz superior (ceros arriba)
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
        self.new.reverse()
        for i in range (len(self.new)):
            self.new[i].reverse()
        answerX=[]
        answerX.append(self.new[0][0]/self.new[0][1]) #Añadiendo x1...

        for i in range (1,len(self.new)):
            aux=self.new[i][0] #El resultado de la X (la igualación)
            j=1
            while (j!=(i+1)):
                aux-=self.new[i][j]*answerX[j-1] #Aquí bien
                j+=1
            if j<=(len(self.new)):
                aux/=self.new[i][j] #Aquí ya se realizó el j+1 
                answerX.append(aux)
            
        #It is perfect
        answerX.reverse() #Cambiar el orden para mostrarlo en pantalla en el orden que es
        for i in range(len(self.xvalues)):
            self.xvalues[i][i] = answerX[i] #Valores de x

    def merge(self,matrix,matrixb):
        for i in range(0,len(matrix)):
            matrix[i].append(matrixb[i])
        return matrix

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
        self.u.reverse()
        for i in range (len(self.new)):
            self.new[i].reverse() #Volver a reversarla 
        for i in range(0,len(self.original)):
            self.total.append([])
            for j in range(len(self.l[0])):
                self.total[i].append(Decimal(self.l[i][j]))
            self.total[i].append("///")
            for j in range(len(self.u[0])):
                self.total[i].append(Decimal(self.u[i][j]))
            self.total[i].append("///")
            for j in range(len(self.xvalues[0])):
                self.total[i].append(Decimal(self.xvalues[i][j]))
        return self.total

    def get_results(self):
        results=""
        aux=1
        for i in self.xvalues:
            results+=f"X{aux}: "+(str)(i)+"\n"
            aux+=1
        print(results) #Falta cambiar esto para la solución
        return results
#n= Doolittle()
#n.doolittle_algorithm([[45,-3,-4],[-12,36,7],[-6,4,57],[-3,-5,-10]],[8,-5,-8,78])
"""
[45,-3,-7,8]
[-12,36,9,-5]
[-6,4,57,-8]
[-3,-5,-10,78]

[100,-50,300,53]
"""