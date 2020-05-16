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
from Non_linear_equations.Busqueda_incremental import Busqueda_incremental
from Non_linear_equations.Biseccion import Biseccion
from Non_linear_equations.PuntoFijo import PuntoFijo
from Non_linear_equations.Regla_falsa import Regla_falsa
from Non_linear_equations.Newton import Newton
from Non_linear_equations.Secante import Secante
from Non_linear_equations.Raices_Multiples import Raices_Multiples
from Systems_of_equations.Gaussian_Elimination import Gaussian_Elimination
from Systems_of_equations.partial_Pivoting import partial_Pivoting
from Verify import Verify
from Funciones import Funciones
from Graph import Graph
from Tables import Tables
from Aids import Aids
funcion=StringProperty('')
gfuncion=StringProperty('')
matrix=StringProperty('')
matrixb=StringProperty('')

class WindowManager(ScreenManager):
    global funcion
    global gfuncion
    global matrix
    global matrixb
    funcion_global=funcion
    gfuncion_global=gfuncion
    matrix_global=matrix
    matrixb_global=matrixb

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
class Non_linear_equations_busqueda(Screen):
    initial_position=ObjectProperty(None)
    increment=ObjectProperty(None)
    iterations=ObjectProperty(None)
    initial_position=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        busqueda=Busqueda_incremental()
        table=Tables()
        verify=Verify()
        error=verify.verify_busqueda(self.funciones.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            busqueda.Operacion(float(self.initial_position.text),float(self.increment.text),float(self.iterations.text),Funcion)
            self.sol.text=busqueda.get_sol()
            columnas=['Posicion','Valor']
            table.draw(busqueda.value_table(),columnas)
        else:
            show_popWindow("Error Incremental Search",error)

    def graficar(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_busqueda(self.funciones.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            graph.draw_funcionesa(self.funciones.text,float(self.initial_position.text),math.fabs(float(self.initial_position.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Incremental Search",error)
    
    def aid(self):
        show_popWindow("Incremental Search Aids",Aids.help_busqueda(self))

class Non_linear_equations_biseccion(Screen):
    xi=ObjectProperty(None)
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        biseccion=Biseccion()
        table=Tables()
        verify=Verify()
        error=verify.verify_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            biseccion.algoritmo_biseccion(float(self.xi.text),float(self.xs.text),Funcion,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=biseccion.get_sol()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            table.draw(biseccion.value_table(),columnas)
        else:
            show_popWindow("Error Bisection",error)

    def graficar(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_funcionesa(self.funciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Bisection",error)
    
    def aid(self):
        show_popWindow("Bisection Aids",Aids.help_biseccion(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Non_linear_equations_regla_falsa(Screen):
    xi=ObjectProperty(None) 
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        regla_falsa=Regla_falsa()
        table=Tables()
        verify=Verify()
        error=verify.verify_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            regla_falsa.algoritmo_regla_falsa(float(self.xi.text),float(self.xs.text),Funcion,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=regla_falsa.get_sol()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            table.draw(regla_falsa.value_table(),columnas)
        else:
            show_popWindow("Error Reguli false",error)

    def graficar(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_funcionesa(self.funciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Reguli false",error)

    def aid(self):
        show_popWindow("Reguli false Aids",Aids.help_regla_falsa(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Non_linear_equations_punto_fijo(Screen):
    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)
    gfunciones=ObjectProperty(None)
    def buscar(self):
        puntoFijo = PuntoFijo()
        table=Tables()
        verify=Verify()
        error=verify.verify_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            GFuncion=Funciones(self.gfunciones.text)
            puntoFijo.algoritmo_puntoFijo(float(self.xi.text),Funcion,GFuncion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=puntoFijo.get_sol()
            columnas=['Iteracion','Xi','F(xm)','Error']
            table.draw(puntoFijo.value_table(),columnas)

        else:
            show_popWindow("Error Fixed Point",error)

    def graficar(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_funcionesb(self.funciones.text,self.gfunciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Fixed Point",error)

    def aid(self):
        show_popWindow("Fixed Point Aids",Aids.help_punto_fijo(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Non_linear_equations_newton(Screen):
    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)
    def buscar(self):
        newton = Newton()
        table=Tables()
        verify=Verify()
        error=verify.verify_newton(self.funciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            newton.algoritmo_newton(float(self.xi.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=newton.get_sol()
            columnas=['Iteracion','Xi','F(xm)',"f'(x)",'Error']
            table.draw(newton.value_table(),columnas)

        else:
            show_popWindow("Error newton",error)

    def graficar(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_newton(self.funciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_funcionesc(self.funciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph newton",error)

    def aid(self):
        show_popWindow("Newton Aids",Aids.help_newton(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo

class Non_linear_equations_secantes(Screen):
    x0=ObjectProperty(None)
    x1=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        secante=Secante()
        table=Tables()
        verify=Verify()
        error=verify.verify_secante(self.x1.text,self.x0.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            secante.algoritmo_secante(float(self.x1.text)-float(self.x1.text)*0.2,float(self.x0.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=secante.get_sol()
            columnas=['Iteration','Xi','F(Xi)','F(xi)-F(Xi_1)','Error']
            table.draw(secante.value_table(),columnas)
        else:
            show_popWindow("Secant Error",error)

    def graficar(self):
        graph=Graph()
        verify=Verify()
        error=verify.verify_secante(self.x1.text,self.x0.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_funcionesa(self.funciones.text,float(self.x0.text),math.fabs(float(self.x0.text))+(float(self.iterations.text)))
        else:
            show_popWindow("Error Graph Secant",error)
    
    def aid(self):
        show_popWindow("Secant Aids",Aids.help_secante(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Non_linear_equations_raices_multiples(Screen):

    xi=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)
    def buscar(self):
        raices_m = Raices_Multiples()
        table=Tables()
        verify=Verify()
        error=verify.verify_raices_mult(self.xi.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            raices_m.algoritmo_raices_mult(float(self.xi.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=raices_m.get_sol()
            columnas=['Iteracion','Xi','F(xm)',"F'(x)","F''(X)",'Error']
            table.draw(raices_m.value_table(),columnas)

        else:
            show_popWindow("Error Multiple Roots",error)

    def graficar(self):
        
        graph=Graph()
        verify=Verify()
        error=verify.verify_raices_mult(self.xi.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            graph.draw_funcionesd(self.funciones.text,float(self.xi.text) - float(self.xi.text)*0.2,math.fabs(float(self.xi.text))+(float(self.iterations.text)))
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
    def buscar(self):
        matrix_method=Gaussian_Elimination()
        table=Tables()
        verify=Verify()
        #error=verify.verify_raices_mult(self.xi.text,self.funciones.text,self.iterations.text,self.tolerance.text)
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
                columnas=matrix_method.rows
                table.draw(matrix_method.value_table(),columnas)

        else:
            show_popWindow("Gaussian Elimination",error)
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
                    print(matrix[i])
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
    def buscar(self):
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
        show_popWindow("Partial pivoting",Aids.help_partial_pivot(self))
    def clean(self, matrix):
        try:
            for i in range(0,len(matrix)):
                if(len(matrix[i])==0):
                    matrix.pop(i)
                else:
                    matrix[i]=matrix[i].replace("\n","")
                    matrix[i]=matrix[i].strip()
                    print(matrix[i])
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
    pass
class System_of_equations_lu_Factorization(Screen):
    pass
class System_of_equations_matrix_Factorization(Screen):
    pass
class Iteratives_System_of_equations(Screen):
    pass
class Interpolation_newton(Screen):
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
    pass
class matrix_Factorization_direct_doolitle(Screen):
    pass
class matrix_Factorization_direct_cholesky(Screen):
    pass
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
