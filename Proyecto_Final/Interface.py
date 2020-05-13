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
from Verificar import Verificar
from Funciones import Funciones
from Graficar import Graficar
from Tabla import Tabla
from Ayudas import Ayudas
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
class Diferenciacion_numerica(Screen):
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
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_busqueda(self.funciones.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            busqueda.Operacion(float(self.initial_position.text),float(self.increment.text),float(self.iterations.text),Funcion)
            self.sol.text=busqueda.get_sol()
            columnas=['Posicion','Valor']
            tabla.dibujar(busqueda.tabla_valores(),columnas)
        else:
            show_popup("Error Incremental Search",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_busqueda(self.funciones.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            grafica.dibujar_funcionesa(self.funciones.text,float(self.initial_position.text),math.fabs(float(self.initial_position.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph Incremental Search",error)
    
    def ayuda(self):
        show_popup("Incremental Search Aids",Ayudas.help_busqueda(self))
class Non_linear_equations_biseccion(Screen):
    xi=ObjectProperty(None)
    xs=ObjectProperty(None)
    iterations=ObjectProperty(None)
    tolerance=ObjectProperty(None)
    sol=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        biseccion=Biseccion()
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            biseccion.algoritmo_biseccion(float(self.xi.text),float(self.xs.text),Funcion,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=biseccion.get_sol()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            tabla.dibujar(biseccion.tabla_valores(),columnas)
        else:
            show_popup("Error Bisection",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funcionesa(self.funciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph Bisection",error)
    
    def ayuda(self):
        show_popup("Bisection Aids",Ayudas.help_biseccion(self))

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
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            regla_falsa.algoritmo_regla_falsa(float(self.xi.text),float(self.xs.text),Funcion,float(self.tolerance.text),float(self.iterations.text),self.tipo_error)
            self.sol.text=regla_falsa.get_sol()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            tabla.dibujar(regla_falsa.tabla_valores(),columnas)
        else:
            show_popup("Error Reguli false",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funcionesa(self.funciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph Reguli false",error)

    def ayuda(self):
        show_popup("Reguli false Aids",Ayudas.help_regla_falsa(self))

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
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            GFuncion=Funciones(self.gfunciones.text)
            puntoFijo.algoritmo_puntoFijo(float(self.xi.text),Funcion,GFuncion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=puntoFijo.get_sol()
            columnas=['Iteracion','Xi','F(xm)','Error']
            tabla.dibujar(puntoFijo.tabla_valores(),columnas)

        else:
            show_popup("Error Fixed Point",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funcionesb(self.funciones.text,self.gfunciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph Fixed Point",error)

    def ayuda(self):
        show_popup("Fixed Point Aids",Ayudas.help_punto_fijo(self))

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
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_newton(self.funciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            newton.algoritmo_newton(float(self.xi.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=newton.get_sol()
            columnas=['Iteracion','Xi','F(xm)',"f'(x)",'Error']
            tabla.dibujar(newton.tabla_valores(),columnas)

        else:
            show_popup("Error newton",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_newton(self.funciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funcionesc(self.funciones.text,float(self.xi.text),math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph newton",error)

    def ayuda(self):
        show_popup("Newton Aids",Ayudas.help_newton(self))

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
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_secante(self.x1.text,self.x0.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            secante.algoritmo_secante(float(self.x1.text)-float(self.x1.text)*0.2,float(self.x0.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=secante.get_sol()
            columnas=['Iteration','Xi','F(Xi)','F(xi)-F(Xi_1)','Error']
            tabla.dibujar(secante.tabla_valores(),columnas)
        else:
            show_popup("Secant Error",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_secante(self.x1.text,self.x0.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funcionesa(self.funciones.text,float(self.x0.text),math.fabs(float(self.x0.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph Secant",error)
    
    def ayuda(self):
        show_popup("Secant Aids",Ayudas.help_secante(self))

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
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_raices_mult(self.xi.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            raices_m.algoritmo_raices_mult(float(self.xi.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=raices_m.get_sol()
            columnas=['Iteracion','Xi','F(xm)',"F'(x)","F''(X)",'Error']
            tabla.dibujar(raices_m.tabla_valores(),columnas)

        else:
            show_popup("Error Multiple Roots",error)

    def graficar(self):
        
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_raices_mult(self.xi.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funcionesd(self.funciones.text,float(self.xi.text) - float(self.xi.text)*0.2,math.fabs(float(self.xi.text))+(float(self.iterations.text)))
        else:
            show_popup("Error Graph Multiple Roots",error)

    def ayuda(self):
        show_popup("Multiple Roots Aids",Ayudas.help_raices_multiples(self))

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class System_of_equations_gaussian_elimination(Screen):

    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    def buscar(self):
        matrix_method=Gaussian_Elimination()
        tabla=Tabla()
        verificar=Verificar()
        #error=verificar.verificar_raices_mult(self.xi.text,self.funciones.text,self.iterations.text,self.tolerance.text)
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.gaussian_elimination_algorithm(matrix_clean,matrixb_clean)
            self.sol.text=matrix_method.get_results()
            columnas=matrix_method.rows
            tabla.dibujar(matrix_method.tabla_valores(),columnas)

        else:
            show_popup("Gaussian Elimination",error)
    def ayuda(self):
        show_popup("Gaussian elimination",Ayudas.help_gaussian_elimination(self))
    def clean(self, matrix):
        for i in range(0,len(matrix)):
            matrix[i]=(matrix[i].split(","))
            for j in range(0,len(matrix[i])):
                if(j==0):
                    matrix[i][j]=matrix[i][j][1:]
                if(j==len(matrix[i])-1):
                    matrix[i][j]=matrix[i][j][0:-1] 
                matrix[i][j]=eval(matrix[i][j])
        return matrix
class System_of_equations_partial_pivot(Screen):
    matrix=ObjectProperty(None)
    matrixb=ObjectProperty(None)
    sol=ObjectProperty(None)
    def buscar(self):
        matrix_method=partial_Pivoting()
        tabla=Tabla()
        verificar=Verificar()
        error=""
        if(error==""):
            matrixb_clean=self.clean((self.matrixb.text).split("\n"))
            matrix_clean=self.clean((self.matrix.text).split("\n"))
            matrix_method.gaussian_elimination_algorithm(matrix_clean,matrixb_clean)
            self.sol.text=matrix_method.get_results()
            columnas=matrix_method.rows
            tabla.dibujar(matrix_method.tabla_valores(),columnas)

        else:
            show_popup("Partial pivot ",error)
    def ayuda(self):
        show_popup("Partial pivoting",Ayudas.help_partial_pivot(self))
    def clean(self, matrix):
        for i in range(0,len(matrix)):
            matrix[i]=(matrix[i].split(","))
            for j in range(0,len(matrix[i])):
                if(j==0):
                    matrix[i][j]=matrix[i][j][1:]
                if(j==len(matrix[i])-1):
                    matrix[i][j]=matrix[i][j][0:-1] 
                matrix[i][j]=eval(matrix[i][j])
        return matrix
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
class Diferenciacion_numerica_diferenciacion(Screen):
    pass
class PopUp(FloatLayout):
    content=ObjectProperty(None)
    boton=ObjectProperty(None)

def show_popup(titulo,content):
    show=PopUp
    show.content.text=content
    popup = Popup(title=titulo, content=show,auto_dismiss=False,size_hint=(None, None), size=(600, 600))
    popup.open()
    show.boton.on_press=popup.dismiss

class Interfaz(App):
    def build(self):
        kv=Builder.load_file("interfaz.kv")
        return kv
