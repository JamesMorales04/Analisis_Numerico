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
from Verify import Verify
from Functions import Functions
from Graph import Graph
from Tables import Tables
from Aids import Aids
function=StringProperty('')
gfunction=StringProperty('')
matrix=StringProperty('')
matrixb=StringProperty('')
interpolationValues=StringProperty('')

class WindowManager(ScreenManager):
    global function
    global gfunction
    global matrix
    global matrixb
    global interpolationValues
    function_global=function
    gfunction_global=gfunction
    matrix_global=matrix
    matrixb_global=matrixb
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
    pass
class Non_linear_equations_search(Screen):
    initial_position=ObjectProperty(None)
    increment=ObjectProperty(None)
    iterations=ObjectProperty(None)
    initial_position=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def searching(self):
        search=Incremental_Search()
        table=Tables()
        verify=Verify()
        error=verify.verify_search(self.functions.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            Function=Functions(self.functions.text)
            search.Operacion(float(self.initial_position.text),float(self.increment.text),float(self.iterations.text),Function)
            self.sol.text=search.get_sol()
            columnas=['Posicion','Valor']
            table.draw(search.value_table(),columnas)
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
        show_popWindow("Incremental Search Aids",Aids.NonLinearEq.help_search(self))

class Non_linear_equations_bisection(Screen):
    xi=ObjectProperty(None)
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def searching(self):
        bisection=Bisection()
        table=Tables()
        verify=Verify()
        error=verify.verify_bisection(self.functions.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            bisection.algorithm_bisection(float(self.xi.text),float(self.xs.text),Function,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=bisection.get_sol()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            table.draw(bisection.value_table(),columnas)
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
        show_popWindow("Bisection Aids",Aids.NonLinearEq.help_bisection(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Non_linear_equations_regla_falsa(Screen):
    xi=ObjectProperty(None) 
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def searching(self):
        regla_falsa=Regla_falsa()
        table=Tables()
        verify=Verify()
        error=verify.verify_bisection(self.functions.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            regla_falsa.algorithm_regla_falsa(float(self.xi.text),float(self.xs.text),Function,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=regla_falsa.get_sol()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            table.draw(regla_falsa.value_table(),columnas)
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
        show_popWindow("Reguli false Aids",Aids.NonLinearEq.help_regla_falsa(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Non_linear_equations_fixed_point(Screen):
    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)
    gfunctions=ObjectProperty(None)
    def searching(self):
        fixedPoint = FixedPoint()
        table=Tables()
        verify=Verify()
        error=verify.verify_fixed_point(self.functions.text,self.gfunctions.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            GFunction=Functions(self.gfunctions.text)
            fixedPoint.algorithm_fixedPoint(float(self.xi.text),Function,GFunction,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=fixedPoint.get_sol()
            columnas=['Iteracion','Xi','F(xm)','Error']
            table.draw(fixedPoint.value_table(),columnas)

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
        show_popWindow("Fixed Point Aids",Aids.NonLinearEq.help_fixed_point(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Non_linear_equations_newton(Screen):
    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)
    def searching(self):
        newton = Newton()
        table=Tables()
        verify=Verify()
        error=verify.verify_newton(self.functions.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            newton.algorithm_newton(float(self.xi.text),Function,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=newton.get_sol()
            columnas=['Iteracion','Xi','F(xm)',"f'(x)",'Error']
            table.draw(newton.value_table(),columnas)

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
        show_popWindow("Newton Aids",Aids.NonLinearEq.help_newton(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo

class Non_linear_equations_secants(Screen):
    x0=ObjectProperty(None)
    x1=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)

    def searching(self):
        secant=Secant()
        table=Tables()
        verify=Verify()
        error=verify.verify_secant(self.x1.text,self.x0.text,self.functions.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            secant.algorithm_secant(float(self.x1.text)-float(self.x1.text)*0.2,float(self.x0.text),Function,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=secant.get_sol()
            columnas=['Iteration','Xi','F(Xi)','F(xi)-F(Xi_1)','Error']
            table.draw(secant.value_table(),columnas)
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
        show_popWindow("Secant Aids",Aids.NonLinearEq.help_secant(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Non_linear_equations_raices_multiples(Screen):

    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    functions=ObjectProperty(None)
    def searching(self):
        raices_m = Raices_Multiples()
        table=Tables()
        verify=Verify()
        error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Function=Functions(self.functions.text)
            raices_m.algorithm_raices_mult(float(self.xi.text),Function,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=raices_m.get_sol()
            columnas=['Iteracion','Xi','F(xm)',"F'(x)","F''(X)",'Error']
            table.draw(raices_m.value_table(),columnas)

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
        show_popWindow("Multiple Roots Aids",Aids.NonLinearEq.help_raices_multiples(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class System_of_equations_gaussian_elimination(Screen):

    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    def searching(self):
        matrix_method=Gaussian_Elimination()
        table=Tables()
        verify=Verify()
        #error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0 or len(matrixb_clean)==0 ):
                error+="Wrong Matrix Input"
                show_popWindow("Gaussian Elimination",error)
            else:
                matrix_method.gaussian_elimination_algorithm(matrix_clean,matrixb_clean)
                self.sol.text=matrix_method.get_results()
                if(matrix_method.get_noerror()):
                    columnas=matrix_method.rows
                    table.draw(matrix_method.value_table(),columnas)

        else:
            show_popWindow("Gaussian Elimination",error)
    def aid(self):
        show_popWindow("Gaussian elimination",Aids.SystemOfEq.help_gaussian_elimination(self))
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
    def searching(self):
        matrix_method=partial_Pivoting()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.partial_pivoting_algorithm(matrix_clean,matrixb_clean)
            self.sol.text=matrix_method.get_results()
            columnas=matrix_method.rows
            table.draw(matrix_method.value_table(),columnas)

        else:
            show_popWindow("Partial pivot ",error)
    def aid(self):
        show_popWindow("Partial pivoting",Aids.SystemOfEq.help_partial_pivot(self))
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
    def searching(self):
        matrix_method=Total_Pivoting()
        table=Tables()
        verify=Verify()
        error=""
        try:
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.total_pivoting_algorithm(matrix_clean,matrixb_clean)
            self.sol.text=matrix_method.get_results()
            columnas=matrix_method.rows
            table.draw(matrix_method.value_table(),columnas)

        except Exception as e:
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
    def searching(self):
        matrix_method=staggered_Pivoting()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.partial_staggered_algorithm(matrix_clean,matrixb_clean)
            self.sol.text=matrix_method.get_results()
            columnas=matrix_method.rows
            table.draw(matrix_method.value_table(),columnas)

        else:
            show_popWindow("Staggered pivot ",error)
    def aid(self):
        show_popWindow("Staggered pivoting",Aids.SystemOfEq.help_partial_pivot(self))
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

class System_of_equations_lu_Factorization(Screen):
    pass
class System_of_equations_matrix_Factorization(Screen):
    pass
class Iteratives_System_of_equations_Gauss_Seidel(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    initvals=ObjectProperty(None)
    lamb=ObjectProperty(None)
    tol=ObjectProperty(None)
    def searching(self):
        matrix_method=Relaxed_gs()
        table=Tables()
        verify=Verify()
        #error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            initvals_clean=self.clean((self.initvals.text).split("\n"))
            if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(initvals_clean)==0 ):
                error+="Wrong Matrix Input"
                show_popWindow("Gauss Seidel",error)
            else:
                matrix_method.Relaxed_gs_algorithm(matrix_clean,matrixb_clean,initvals_clean,float(self.lamb.text),float(self.tol.text))
                columnas=matrix_method.rows
                table.draw(matrix_method.value_table(),columnas)
                self.sol.text=matrix_method.get_sol()

        else:
            show_popWindow("Gauss Seidel",error)
    def aid(self):
        show_popWindow("Gauss Seidel",Aids.help_gaussian_elimination(self))
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
    def searching(self):
        matrix_method=Relaxed_jacobi()
        table=Tables()
        verify=Verify()
        #error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            initvals_clean=self.clean((self.initvals.text).split("\n"))
            if(len(matrix_clean)==0 or len(matrixb_clean)==0 or len(initvals_clean)==0 ):
                error+="Wrong Matrix Input"
                show_popWindow("Jacobi",error)
            else:
                matrix_method.Relaxed_jacobi_algorithm(matrix_clean,matrixb_clean,initvals_clean,float(self.lamb.text),float(self.tol.text))
                columnas=matrix_method.rows
                table.draw(matrix_method.value_table(),columnas)
                self.sol.text=matrix_method.get_sol()

        else:
            show_popWindow("Jacobi",error)
    def aid(self):
        show_popWindow("Jacobi",Aids.help_gaussian_elimination(self))
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
class Interpolation_newton(Screen):
    tolerance=ObjectProperty(None)
    functions=ObjectProperty(None)
    sol=ObjectProperty(None)
    pass
class Interpolation_lagrange(Screen):
    pass
class Interpolation_splines(Screen):
    pass
class Numeric_differentiation_differentiation(Screen):
    pass
class matrix_Factorization_based_gaussian_simple(Screen):
    pass
class matrix_Factorization_based_gaussian_pivoting(Screen):
    pass
class matrix_Factorization_direct_croult(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    matrix_method=Croult()
    rund=False
    table=Tables()
    def searching(self):
        self.matrix_method=Croult()
        verify=Verify()
        #error=verify.verify_raices_mult(self.xi.text,self.functions.text,self.iterations.text,self.tolerance.text)
        error=""
        if(error==""):
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            if(len(matrix_clean)==0):
                error+="Wrong Matrix Input"
                show_popWindow("Croult",error)
            else:
                self.matrix_method.croult_algorithm(matrix_clean)  
                self.sol.text="Matrix LU Ready"
                self.rund=True
        else:
            show_popWindow("Croult",error)


    def aid(self):
        show_popWindow("Croult",Aids.help_gaussian_elimination(self))

    def runb(self):
        self.table=Tables()
        matrixb_clean=self.clean((self.matrixb.text).split("\n"))
        if(len(matrixb_clean)==0):
            error="Wrong Matrix Input"
            show_popWindow("Croult",error)
        else:
            if(self.rund):
                self.matrix_method.runb(matrixb_clean)
                self.sol.text=self.matrix_method.get_results()
                if(self.matrix_method.get_noerror()):
                    columnas=self.matrix_method.rows
                    self.table.draw(self.matrix_method.get_total(),columnas)
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
    def searching(self):
        matrix_method=Doolittle()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.doolittle_algorithm(matrix_clean,matrixb_clean)
            columnas=matrix_method.rows
            table.draw(matrix_method.value_table(),columnas)
            self.sol.text=matrix_method.get_results()


        else:
            show_popWindow("Doolittle ",error)
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
class matrix_Factorization_direct_cholesky(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    
    def searching(self):
        matrix_method=Cholesky()
        table=Tables()
        verify=Verify()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.cholesky_algorithm(matrix_clean,matrixb_clean)
            columnas=matrix_method.rows
            table.draw(matrix_method.value_table(),columnas)
            self.sol.text=matrix_method.get_results()

        else:
            show_popWindow("Cholesky ",error)
    def aid(self):
        show_popWindow("Cholesky",Aids.help_doolittle(self))
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

class matrix_Factorization_direct_diagonal_matrix(Screen):
    pass

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
