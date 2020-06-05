from kivy import Config
Config.set('graphics','multisamples','0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
import math
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty,StringProperty,NumericProperty
from kivy.uix.popup import Popup
from Non_linear_equations.Incremental_Search import Incremental_Search
from Non_linear_equations.Bisection import Bisection
from Non_linear_equations.FixedPoint import FixedPoint
from Non_linear_equations.Regla_falsa import Regla_falsa
from Non_linear_equations.Newton import Newton
from Non_linear_equations.Secant import Secant
from Non_linear_equations.Raices_Multiples import Raices_Multiples
from Systems_of_equations.Gaussian_Elimination import Gaussian_Elimination
from Systems_of_equations.partial_Pivoting import partial_Pivoting
from Systems_of_equations.Total_Pivoting import Total_Pivoting
from Systems_of_equations.staggered_Pivoting import staggered_Pivoting
from Systems_of_equations.Croult import Croult
from Systems_of_equations.Cholesky import Cholesky
from Systems_of_equations.Doolittle import Doolittle
from Systems_of_equations.Relaxed_gs import Relaxed_gs
from Systems_of_equations.Relaxed_jacobi import Relaxed_jacobi
from Interpolation.NewtonInterpolation import NewtonInterpolation
from Interpolation.Lagrange import Lagrange
from Interpolation.LinearSpline import LinearSpline
from Interpolation.CubicSpline import CubicSpline
from Interpolation.QuadraticSpline import QuadraticSpline
from NumericDiff.trapezium import trapezium
from NumericDiff.gentrapezium import GenTrapezium
from NumericDiff.gensimpson3 import gensimpson3
from NumericDiff.gensimpson8 import GenSimpson38
from NumericDiff.simpson3 import Simpson13
from NumericDiff.simpson8 import Simpson38
from Verify import Verify
from Functions import Functions
from Graph import Graph
from Tables import Tables
from Aids import Aids
function=StringProperty('')
gfunction=StringProperty('')
matrix=StringProperty('')
matrixb=StringProperty('')
splineX=StringProperty('')
splineY=StringProperty('')
interpolationValues=StringProperty('')

class WindowManager(ScreenManager):
    global function
    global gfunction
    global matrix
    global matrixb
    global splineX
    global splineY
    global interpolationValues
    function_global=function
    gfunction_global=gfunction
    matrix_global=matrix
    matrixb_global=matrixb
    splineX_global=splineX
    splineY_global=splineY
    interpolationValues_global=interpolationValues
class Menu_Initial(Screen):
    pass
class Non_linear_equations(Screen):
    pass
class System_of_equations(Screen):
    pass
class Interpolation(Screen):
    pass
class Numeric_differentiation(Screen):
    functions= ObjectProperty(None)
    xi= ObjectProperty(None)
    xs= ObjectProperty(None)
    iterations= ObjectProperty(None)
    sol= ObjectProperty(None)
    iterations= ObjectProperty(None)
    def run(self):
        verify= Verify()
        error=verify.verify_newton_interpolation(self.functions.text,self.iterations.text)
        error+= verify.verify_numeric_differentiation(self.xi.text,self.xs.text)
        if (error==""):
            Function=Functions(self.functions.text)
            if (self.method == "Trapezium"):
                SimpleTrapezium= trapezium()
                self.sol.text= SimpleTrapezium.algorithm_trapezium(Function,self.xi.text,self.xs.text)
            elif (self.method == "Generalized Trapezium"):
                genTrapezium = GenTrapezium()
                self.sol.text= genTrapezium.general_trapezium_algorithm(Function,self.xi.text,self.xs.text,self.iterations.text)           
            elif (self.method == "Simpson8"):
                simpson8= Simpson38()
                self.sol.text= simpson8.simpson_38_algorithm(Function,self.xi.text,self.xs.text)
            elif (self.method == "Simpson3"):
                simpson3= Simpson13()
                self.sol.text= simpson3.simpson_13_algorithm(Function,self.xi.text,self.xs.text,self.iterations.text)            
            elif (self.method == "Generalized Simpson8"):
                genSimpson8= GenSimpson38()
                self.sol.text= genSimpson8.general_simpson38_algorithm(Function,self.xi.text,self.xs.text,self.iterations.text)
            elif (self.method == "Generalized Simpson3"):
                genSimpson3 = gensimpson3()
                self.sol.text= genSimpson3.algorithm_gensimpson3(Function,self.xi.text,self.xs.text,self.iterations.text)
        else:
            show_popWindow("Numeric differentiation",error)   

    def Trapezium(self):
        self.method= "Trapezium"
    def GeneralizedTrapezium(self):
        self.method= "Generalized Trapezium"
    def Simpson8(self):
        self.method="Simpson8"
    def GeneralizedSimpson8(self):
        self.method="Generalized Simpson8"
    def Simpson3(self):      
        self.method="Simpson3"
    def GeneralizedSimpson3(self):
        self.method="Generalized Simpson3"
        
class Non_linear_equations_search(Screen):
    initial_position=ObjectProperty(None)
    increment=ObjectProperty(None)
    iterations=ObjectProperty(None)
    initial_position=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def run(self):
        search=Incremental_Search()
        table=Tables()
        verify=Verify()
        error=verify.verify_search(self.functions.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            Function=Functions(self.functions.text)
            search.Operacion(float(self.initial_position.text),float(self.increment.text),float(self.iterations.text),Function)
            self.sol.text=search.get_sol()
            columns=['Posicion','Valor']
            table.draw(search.value_table(),columns)
        else:
            show_popWindow("Error Incremental Search",error)

    def graphic(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_search(self.functions.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            graph.draw_functionsa(self.functions.text,float(self.initial_position.text),math.fabs(float(self.initial_position.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Incremental Search",error)
    
    def aid(self):
        show_popWindow("Incremental Search Aids",Aids.help_search(self))

class Non_linear_equations_bisection(Screen):
    xi=ObjectProperty(None)
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def run(self):
        bisection=Bisection()
        table=Tables()
        verify=Verify()
        error=verify.verify_bisection(self.functions.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            bisection.algorithm_bisection(float(self.xi.text),float(self.xs.text),Function,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=bisection.get_sol()
            columns=['Iteration','Xi','Xu','Xm','F(xm)','Error']
            table.draw(bisection.value_table(),columns)
        else:
            show_popWindow("Error Bisection",error)

    def graphic(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_bisection(self.functions.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_functionsa(self.functions.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Bisection",error)
    
    def aid(self):
        show_popWindow("Bisection Aids",Aids.help_bisection(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Non_linear_equations_regla_falsa(Screen):
    xi=ObjectProperty(None) 
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def run(self):
        regla_falsa=Regla_falsa()
        table=Tables()
        verify=Verify()
        error=verify.verify_bisection(self.functions.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            regla_falsa.algorithm_regla_falsa(float(self.xi.text),float(self.xs.text),Function,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=regla_falsa.get_sol()
            columns=['Iteration','Xi','Xu','Xm','F(xm)','Error']
            table.draw(regla_falsa.value_table(),columns)
        else:
            show_popWindow("Error Reguli false",error)

    def graphic(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_bisection(self.functions.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_functionsa(self.functions.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Reguli false",error)

    def aid(self):
        show_popWindow("Reguli false Aids",Aids.help_regla_falsa(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Non_linear_equations_fixed_point(Screen):
    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)
    gfunctions=ObjectProperty(None)
    def run(self):
        fixedPoint = FixedPoint()
        table=Tables()
        verify=Verify()
        error=verify.verify_fixed_point(self.functions.text,self.gfunctions.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            GFunction=Functions(self.gfunctions.text)
            fixedPoint.algorithm_fixedPoint(float(self.xi.text),Function,GFunction,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=fixedPoint.get_sol()
            columns=['Iteration','Xi','F(xm)','Error']
            table.draw(fixedPoint.value_table(),columns)

        else:
            show_popWindow("Error Fixed Point",error)

    def graphic(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_fixed_point(self.functions.text,self.gfunctions.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_functionsb(self.functions.text,self.gfunctions.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Fixed Point",error)

    def aid(self):
        show_popWindow("Fixed Point Aids",Aids.help_fixed_point(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Non_linear_equations_newton(Screen):
    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)
    def run(self):
        newton = Newton()
        table=Tables()
        verify=Verify()
        error=verify.verify_newton(self.functions.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            newton.algorithm_newton(float(self.xi.text),Function,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=newton.get_sol()
            columns=['Iteration','Xi','F(xm)',"f'(x)",'Error']
            table.draw(newton.value_table(),columns)

        else:
            show_popWindow("Error newton",error)

    def graphic(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_newton(self.functions.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_functionsc(self.functions.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph newton",error)

    def aid(self):
        show_popWindow("Newton Aids",Aids.help_newton(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo

class Non_linear_equations_secants(Screen):
    x0=ObjectProperty(None)
    x1=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def run(self):
        secant=Secant()
        table=Tables()
        verify=Verify()
        error=verify.verify_secant(self.x1.text,self.x0.text,self.functions.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            secant.algorithm_secant(float(self.x1.text)-float(self.x1.text)*0.2,float(self.x0.text),Function,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=secant.get_sol()
            columns=['Iteration','Xi','F(Xi)','F(xi)-F(Xi_1)','Error']
            table.draw(secant.value_table(),columns)
        else:
            show_popWindow("Secant Error",error)

    def graphic(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_secant(self.x1.text,self.x0.text,self.functions.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_functionsa(self.functions.text,float(self.x0.text),math.fabs(float(self.x0.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Secant",error)
    
    def aid(self):
        show_popWindow("Secant Aids",Aids.help_secant(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Non_linear_equations_raices_multiples(Screen):

    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)
    def run(self):
        raices_m = Raices_Multiples()
        table=Tables()
        verify=Verify()
        error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            raices_m.algorithm_raices_mult(float(self.xi.text),Function,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=raices_m.get_sol()
            columns=['Iteration','Xi','F(xm)',"F'(x)","F''(X)",'Error']
            table.draw(raices_m.value_table(),columns)

        else:
            show_popWindow("Error Multiple Roots",error)

    def graphic(self):
        
        graph=Graph()
        verify=Verify()
        error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_functionsd(self.functions.text,float(self.xi.text) - float(self.xi.text)*0.2,math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Multiple Roots",error)

    def aid(self):
        show_popWindow("Multiple Roots Aids",Aids.help_raices_multiples(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class System_of_equations_gaussian_elimination(Screen):

    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    matrix_method=Gaussian_Elimination()
    rund=False
    def run(self):
        self.matrix_method=Gaussian_Elimination()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(matrixb_clean[0])!=len(matrix_clean) or verify.verify_length(matrix_clean) or len(matrixb_clean[0])!=len(matrix_clean[0])):
                error+="Wrong Matrix Input"
                show_popWindow("Gaussian Elimination",error)
            else:
                self.matrix_method.gaussian_elimination_algorithm(matrix_clean,matrixb_clean)
                self.sol.text=self.matrix_method.get_results()
                if(self.matrix_method.get_noerror()):
                    columns=self.matrix_method.rows
                    table.draw(self.matrix_method.value_table(),columns)
                    self.rund=True

        else:
            show_popWindow("Gaussian Elimination",error)
    def steps(self):
        if(self.rund):
            columns=self.matrix_method.get_steps_rows()
            table=Tables()
            table.draw(self.matrix_method.get_steps_table(),columns)
    def aid(self):
        show_popWindow("Gaussian elimination",Aids.help_gaussian_elimination(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class System_of_equations_partial_pivot(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        self.matrix_method=partial_Pivoting()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(matrixb_clean[0])!=len(matrix_clean) or verify.verify_length(matrix_clean) or len(matrixb_clean[0])!=len(matrix_clean[0])):
                error+="Wrong Matrix Input"
                show_popWindow("Gaussian Elimination",error)
            else:
                self.matrix_method.partial_pivoting_algorithm(matrix_clean,matrixb_clean)
                self.sol.text=self.matrix_method.get_results()
                columns=self.matrix_method.rows
                if (not self.matrix_method.get_error()):
                    table.draw(self.matrix_method.value_table(),columns)
                    self.rund=True
        else:
            show_popWindow("Partial pivot ",error)
    def steps(self):
        if(self.rund):
            columns=self.matrix_method.get_steps_rows()
            table=Tables()
            table.draw(self.matrix_method.get_steps_table(),columns)
    def aid(self):
        show_popWindow("Partial pivoting",Aids.help_partial_pivot(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class System_of_equations_total_pivot(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        matrix_method=Total_Pivoting()
        table=Tables()
        verify=Verify()
        error=""
        try:
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.total_pivoting_algorithm(matrix_clean,matrixb_clean)
            self.sol.text=matrix_method.get_results()
            columns=matrix_method.rows
            table.draw(matrix_method.value_table(),columns)

        except Exception as e:
            error = "Error: while processing the matrix. This can be generated by infinite or no solutions of the sistem"
            show_popWindow("Total pivot ",error)
    def aid(self):
        show_popWindow("Total pivoting",Aids.help_total_pivot(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class System_of_equations_staggered_pivot(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        matrix_method=staggered_Pivoting()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(matrixb_clean[0])!=len(matrix_clean) or verify.verify_length(matrix_clean) or len(matrixb_clean[0])!=len(matrix_clean[0])):
                error+="Wrong Matrix Input"
                show_popWindow("Gaussian Elimination",error)
            else:
                matrix_method.partial_staggered_algorithm(matrix_clean,matrixb_clean)
                self.sol.text=matrix_method.get_results()
                columns=matrix_method.rows
                table.draw(matrix_method.value_table(),columns)

        else:
            show_popWindow("Staggered pivot ",error)
    def aid(self):
        show_popWindow("Staggered pivoting",Aids.help_staggeredPivoting(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []

class System_of_equations_matrix_Factorization(Screen):
    pass
class Iteratives_System_of_equations_Gauss_Seidel(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    initvals=ObjectProperty(None)
    lamb=ObjectProperty(None)
    iter=ObjectProperty(None)
    tol=ObjectProperty(None)
    def run(self):
        matrix_method=Relaxed_gs()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            initvals_clean=self.clean((self.initvals.text).split("\n"))
            error=verify.verify_seidel_Jacobi(matrix_clean,matrixb_clean,initvals_clean,self.iter.text,self.tol.text,self.lamb.text)
            if(error!=""):
                show_popWindow("Gauss Seidel",error)
            else:
                matrix_method.Relaxed_gs_algorithm(matrix_clean,matrixb_clean,initvals_clean,float(self.lamb.text),float(self.tol.text),int(self.iter.text))
                columns=matrix_method.rows
                table.draw(matrix_method.value_table(),columns)
                self.sol.text=matrix_method.get_sol()

        else:
            show_popWindow("Gauss Seidel",error)
    def aid(self):
        show_popWindow("Gauss Seidel",Aids.help_GaussSeidel(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class Iteratives_System_of_equations_jacobi(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    initvals=ObjectProperty(None)
    lamb=ObjectProperty(None)
    tol=ObjectProperty(None)
    iter=ObjectProperty(None)
    def run(self):
        matrix_method=Relaxed_jacobi()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            initvals_clean=self.clean((self.initvals.text).split("\n"))
            error=verify.verify_seidel_Jacobi(matrix_clean,matrixb_clean,initvals_clean,self.iter.text,self.tol.text,self.lamb.text)
            if(error!=""):
                show_popWindow("Jacobi",error)
            else:
                matrix_method.Relaxed_jacobi_algorithm(matrix_clean,matrixb_clean,initvals_clean,float(self.lamb.text),float(self.tol.text),int(self.iter.text))
                columns=matrix_method.rows
                table.draw(matrix_method.value_table(),columns)
                self.sol.text=matrix_method.get_sol()

        else:
            show_popWindow("Jacobi",error)
    def aid(self):
        show_popWindow("Jacobi",Aids.help_jacobi(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class Interpolation_splines(Screen):
    pass

class Interpolation_newton(Screen):
    functions=ObjectProperty(None)
    numbers=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        matrix_method=NewtonInterpolation()
        table=Tables()
        verify = Verify()
        error=verify.verify_newton_interpolation(self.functions.text,self.numbers.text)
        if (error=="" and self.clean(self.numbers)):
            Function=Functions(self.functions.text)
            Numbers=self.clean((self.numbers.text).split("\n"))
            matrix_method.algorithm_newtonInterpolation(Function,Numbers)
            columns= matrix_method.rows
            table.draw(matrix_method.value_table(),columns)
            self.sol.text=matrix_method.get_sol()
        else:
            error = "Please check your values"
            show_popWindow("Interpolation Newton", error)
    def aid(self):
        show_popWindow("Newton Interpolation", Aids.help_newton_interpolation(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class Interpolation_lagrange(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    
    def run(self):
        verify=Verify()
        error=True
        matrixb_clean=self.clean((self.matrixb.text).split("\n"))
        matrix_clean=self.clean((self.matrix.text).split("\n"))        
        #error=verify.verify_length(matrix_clean)
        #error=verify.verify_length(matrixb_clean)
        if(matrix_clean and matrixb_clean):
            method=Lagrange()
            method.lagrange_interpol_algorithm(matrix_clean[0],matrixb_clean[0])
            response = method.getPolynomial()
            self.sol.text= response
        else:
            show_popWindow("Lagrange ","Invalid fields")
    def aid(self):
        show_popWindow("Lagrange",Aids.help_lagrange(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []

class matrix_Factorization_direct_croult(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    matrix_method=Croult()
    rund=False
    table=Tables()
    def run(self):
        self.matrix_method=Croult()
        verify=Verify()
        error=""
        if(error==""):
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0 or verify.verify_length(matrix_clean) or len(matrix_clean)!=len(matrix_clean[0])):
                error+="Wrong Matrix Input"
                show_popWindow("Croult",error)
            else:
                self.matrix_method.croult_algorithm(matrix_clean)  
                self.sol.text="Matrix LU Ready"
                self.rund=True
        else:
            show_popWindow("Croult",error)
    
    def steps(self):
        if(self.rund):
            columns=self.matrix_method.get_steps_rows()
            table=Tables()
            table.draw(self.matrix_method.get_steps_table(),columns)
    def aid(self):
        show_popWindow("Croult",Aids.help_croult(self))

    def runb(self):
        self.table=Tables()
        verify=Verify()
        matrix_clean=self.clean((self.matrix.text).split("\n")) 
        matrixb_clean=self.clean((self.matrixb.text).split("\n"))
        if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(matrixb_clean[0])!=len(matrix_clean) or verify.verify_length(matrix_clean) or len(matrixb_clean[0])!=len(matrix_clean[0])):
            error="Wrong Matrix Input"
            show_popWindow("Croult",error)
        else:
            if(self.rund):
                self.matrix_method.runb(matrixb_clean)
                self.sol.text=self.matrix_method.get_results()
                if(self.matrix_method.get_noerror()):
                    columns=self.matrix_method.rows
                    self.table.draw(self.matrix_method.get_total(),columns)
            else:
                self.sol.text="First create matrix LU"

    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
class matrix_Factorization_direct_doolitle(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    rund=False
    table=Tables()
    def run(self):
        self.matrix_method=Doolittle()
        verify=Verify()
        error=""
        if(error==""):
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0 or verify.verify_length(matrix_clean) or len(matrix_clean)!=len(matrix_clean[0])):
                error+="Wrong Matrix Input"
                show_popWindow("Doolittle", error)
            else:
                self.matrix_method.doolittle_algorithm(matrix_clean)
                self.sol.text= "Matrix LU ready"
                self.rund=True
        else:
            show_popWindow("Doolittle ",error)
    def steps(self):
        if(self.rund):
            columns=self.matrix_method.get_steps_rows()
            table = Tables()
            table.draw(self.matrix_method.get_steps_table(),columns)
          
    def runb(self):     
        self.table=Tables()
        verify=Verify()
        matrix_clean=self.clean((self.matrix.text).split("\n"))
        matrixb_clean=self.clean((self.matrixb.text).split("\n")) 
        if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(matrixb_clean[0])!=len(matrix_clean) or verify.verify_length(matrix_clean) or len(matrixb_clean[0])!=len(matrix_clean[0])):
            error="Wrong Matrix Input"
            show_popWindow("Doolittle",error)
        else:
            if(self.rund):
                self.matrix_method.runb(matrixb_clean)
                self.sol.text=self.matrix_method.get_results()
                if(self.matrix_method.get_noerror):
                    columns=self.matrix_method.rows
                    self.table.draw(self.matrix_method.value_table(),columns)
            else:
                self.sol.text="First create matrix LU"
    def aid(self):
        show_popWindow("Doolittle",Aids.help_doolittle(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []

class interpolation_quadratic_spline(Screen):
    splineX=ObjectProperty(None)
    splineY=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        spline_method=QuadraticSpline()
        table=Tables()
        verify=Verify()
        splineX_clean=self.clean((self.splineY.text).split("\n"))
        splineY_clean=self.clean((self.splineX.text).split("\n"))
        error=True
        #error=verify.verify_length(splineX_clean)
        #error=verify.verify_length(splineY_clean)   
        if (error):     
            if(spline_method.check_values(splineX_clean,splineY_clean)):
                splineX_clean=self.clean((self.splineY.text).split("\n"))
                splineY_clean=self.clean((self.splineX.text).split("\n"))
                spline_method.algorithm_quadratic_spline(splineX_clean, splineY_clean)
                columns=["Functions"]
                table.draw(spline_method.value_table(),columns)
                self.sol.text=spline_method.get_results()
            else:
                show_popWindow("Quadratic Spline ","No valid values, please check it")
        else:
            show_popWindow("Quadratic spline", "Invalid values")
    def aid(self):
        show_popWindow("Quadratic Spline",Aids.help_quadratic_spline(self))
    def clean(self, x):
        try:
            for i in range(0,len(x)):
                if(len(x[i])==0):
                    x.pop(i)
                else:
                    x[i]=x[i].replace("\n","")
                    x[i]=x[i].strip()
                    x[i]=(x[i].split(","))
                    for j in range(0,len(x[i])):
                        if(j==0):
                            x[i][j]=x[i][j][1:]
                        if(j==len(x[i])-1):
                            x[i][j]=x[i][j][0:-1] 
                        x[i][j]=eval(x[i][j])
            return x
        except:
            return []

class interpolation_cubic_spline(Screen):
    splineX=ObjectProperty(None)
    splineY=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        spline_method=CubicSpline()
        table=Tables()
        verify=Verify()
        splineX_clean=self.clean((self.splineY.text).split("\n"))
        splineY_clean=self.clean((self.splineX.text).split("\n"))
        error=True
        #error=verify.verify_length(splineX_clean)
        #error=verify.verify_length(splineY_clean)
        if(error):        
            if(spline_method.check_values(splineX_clean,splineY_clean)):
                splineX_clean=self.clean((self.splineY.text).split("\n"))
                splineY_clean=self.clean((self.splineX.text).split("\n"))
                spline_method.algorithm_cubic_spline(splineX_clean, splineY_clean)
                columns=["functions"]
                table.draw(spline_method.value_table(),columns)
                self.sol.text=spline_method.get_results()
            else:
                show_popWindow("Cubic Spline ","No valid values, please check it")
        else:
            show_popWindow("Cubic spline", "Invalid function")

    def aid(self):
        show_popWindow("Cubic Spline",Aids.help_cubic_spline(self))
    def clean(self, x):
        try:
            for i in range(0,len(x)):
                if(len(x[i])==0):
                    x.pop(i)
                else:
                    x[i]=x[i].replace("\n","")
                    x[i]=x[i].strip()
                    x[i]=(x[i].split(","))
                    for j in range(0,len(x[i])):
                        if(j==0):
                            x[i][j]=x[i][j][1:]
                        if(j==len(x[i])-1):
                            x[i][j]=x[i][j][0:-1] 
                        x[i][j]=eval(x[i][j])
            return x
        except:
            return []

class interpolation_linear_spline(Screen):
    splineX=ObjectProperty(None)
    splineY=ObjectProperty(None)
    sol=ObjectProperty(None)
    def run(self):
        spline_method=LinearSpline()
        table=Tables()
        verify=Verify()
        splineX_clean=self.clean((self.splineY.text).split("\n"))
        splineY_clean=self.clean((self.splineX.text).split("\n"))
        error=True
        #error=verify.verify_length(splineX_clean)
        #error=verify.verify_length(splineY_clean)
        if (error):
            if(spline_method.check_values(splineX_clean,splineY_clean)):
                spline_method.algorithm_linearSpline(splineX_clean, splineY_clean)
                columns=["P(x)","Interval"]
                table.draw(spline_method.value_table(),columns)
                self.sol.text=spline_method.get_results()
            else:
                show_popWindow("Linear Spline ","No valid values, please check them")
        else:
            show_popWindow("Splines", "Invalid fields")
    def aid(self):
        show_popWindow("Linear Spline",Aids.help_lineal_spline(self))
    def clean(self, x):
        try:
            for i in range(0,len(x)):
                if(len(x[i])==0):
                    x.pop(i)
                else:
                    x[i]=x[i].replace("\n","")
                    x[i]=x[i].strip()
                    x[i]=(x[i].split(","))
                    for j in range(0,len(x[i])):
                        if(j==0):
                            x[i][j]=x[i][j][1:]
                        if(j==len(x[i])-1):
                            x[i][j]=x[i][j][0:-1] 
                        x[i][j]=eval(x[i][j])
            return x
        except:
            return []

class matrix_Factorization_direct_cholesky(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    matrix_method = Cholesky()
    
    def runb(self):
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            if(len(matrixb_clean)!=0):
                self.matrix_method.cholesky_algorithm(matrixb_clean)
                columns=self.matrix_method.rows
                table.draw(self.matrix_method.getSteps(),columns)
                self.sol.text=self.matrix_method.get_results()
            else:
                self.sol.text = 'Error: No B matrix was entered'

        else:
            show_popWindow("Cholesky ",error)
    def aid(self):
        show_popWindow("Cholesky",Aids.help_cholesky(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    matrix[i]=(matrix[i].split(","))
                    for j in range(0,len(matrix[i])):
                        if(j==0):
                            matrix[i][j]=matrix[i][j][1:]
                        if(j==len(matrix[i])-1):
                            matrix[i][j]=matrix[i][j][0:-1] 
                        matrix[i][j]=eval(matrix[i][j])
            return matrix
        except:
            return []
    def run(self):
        error=""
        if(error==""):
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            self.matrix_method.getMatrices(matrix_clean)
            self.sol.text=self.matrix_method.LUOutput

        else:
            show_popWindow("Cholesky ",error)

class PopWindow(FloatLayout):
    contained=ObjectProperty(None)
    boton=ObjectProperty(None)

def show_popWindow(titulo,contained):
    show=PopWindow()
    show.contained.text=contained
    popup = Popup(title=titulo, content=show,auto_dismiss=False,size_hint=(None, None), size=(600, 600))
    popup.open()
    show.boton.on_press=popup.dismiss

class Interface(App):
    def build(self):
        kv=Builder.load_file("interface.kv")
        return kv
