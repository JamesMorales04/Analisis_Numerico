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
from Ecuaciones_no_lineales.Busqueda_incremental import Busqueda_incremental
from Ecuaciones_no_lineales.Biseccion import Biseccion
from Ecuaciones_no_lineales.PuntoFijo import PuntoFijo
from Ecuaciones_no_lineales.Regla_falsa import Regla_falsa
from Ecuaciones_no_lineales.Newton import Newton
from Ecuaciones_no_lineales.Secante import Secante
from Ecuaciones_no_lineales.Raices_Multiples import Raices_Multiples
from Sistemas_de_Ecuaciones.Gaussian_Elimination import Gaussian_Elimination
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
class Ayudasw(Screen):
    ayuda=ObjectProperty(None)
    ayudaf=ObjectProperty(None)
class Menu_Initial(Screen):
    pass
class Ecuaciones_no_lineales(Screen):
    pass
class Sistemas_de_ecuaciones(Screen):
    pass
class Interpolation(Screen):
    pass
class Diferenciacion_numerica(Screen):
    pass
class Ecuaciones_no_lineales_busqueda(Screen):
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
        ayudar=Ayudas()
        print(ayudar.ayudas_busqueda())
        show_popup("Incremental Search Aids",ayudar.ayudas_busqueda())
class Ecuaciones_no_lineales_biseccion(Screen):
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
        ayudar=Ayudas()
        show_popup("Bisection Aids",ayudar.ayudas_biseccion())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Ecuaciones_no_lineales_regla_falsa(Screen):
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
        ayudar=Ayudas()
        show_popup("Reguli false Aids",ayudar.ayudas_regla_falsa())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Ecuaciones_no_lineales_punto_fijo(Screen):
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
        ayudar=Ayudas()
        show_popup("Fixed Point Aids",ayudar.ayudas_punto_fijo())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Ecuaciones_no_lineales_newton(Screen):
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
        ayudar=Ayudas()
        show_popup("Newton Aids",ayudar.ayudas_newton())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo

class Ecuaciones_no_lineales_secantes(Screen):
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
        ayudar=Ayudas()
        show_popup("Secant Aids",ayudar.ayudas_secante())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Ecuaciones_no_lineales_raices_multiples(Screen):

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
        ayudar=Ayudas()
        show_popup("Multiple Roots Aids",ayudar.ayudas_raices_multiples())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo


class Sistemas_de_ecuaciones_eliminacion_gaussiana(Screen):

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
        ayudar=Ayudas()
        show_popup("Gaussian Elimination",ayudar.ayudas_raices_multiples())
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
    pass
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
class Ventana_emergente(FloatLayout):
    contenido=ObjectProperty(None)
    boton=ObjectProperty(None)

def show_popup(titulo,contenido):
    show=Ventana_emergente()
    show.contenido.text=contenido
    popup = Popup(title=titulo, content=show,auto_dismiss=False,size_hint=(None, None), size=(600, 600))
    popup.open()
    show.boton.on_press=popup.dismiss

class Interfaz(App):
    def build(self):
        kv=Builder.load_file("interfaz.kv")
        return kv
