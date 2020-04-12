from kivy import Config
Config.set('graphics','multisamples','0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
import math
from kivy.app import App
from kivy.uix.label import Label
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
from Verificar import Verificar
from Funciones import Funciones
from Graficar import Graficar
from Tabla import Tabla
from Ayudas import Ayudas
funcion=StringProperty('')

class WindowManager(ScreenManager):
    global funcion
    funcion_global=funcion
class Ayudasw(Screen):
    ayuda=ObjectProperty(None)
    ayudaf=ObjectProperty(None)
class Menu_Initial(Screen):
    pass
class Ecuaciones_no_lineales(Screen):
    pass
class Sistemas_de_ecuaciones(Screen):
    pass
class Interpolacion(Screen):
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
            show_popup("Error Busqueda Incremental",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_busqueda(self.funciones.text,self.initial_position.text,self.increment.text,self.iterations.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text,float(self.initial_position.text),math.fabs(float(self.initial_position.text))+(float(self.increment.text)*float(self.iterations.text)),float(self.increment.text))
        else:
            show_popup("Error Graficar Busqueda Incremental",error)
    
    def ayuda(self):
        ayudar=Ayudas()
        print(ayudar.ayudas_busqueda())
        show_popup("Ayudas Busqueda Incremental",ayudar.ayudas_busqueda())
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
            show_popup("Error Biseccion",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text,float(self.xi.text),float(self.xs.text),float(self.tolerance.text))
        else:
            show_popup("Error Graficar Biseccion",error)
    
    def ayuda(self):
        ayudar=Ayudas()
        show_popup("Ayudas Biseccion",ayudar.ayudas_biseccion())

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
            show_popup("Error Regla_falsa",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text,float(self.xi.text),float(self.xs.text),float(self.tolerance.text))
        else:
            show_popup("Error Graficar Regla Falsa",error)

    def ayuda(self):
        ayudar=Ayudas()
        show_popup("Ayudas Regla Falsa",ayudar.ayudas_regla_falsa())

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
            show_popup("Error punto fijo",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text, self.gfunciones.text)
        else:
            show_popup("Error Graficar Punto Fijo",error)

    def ayuda(self):
        ayudar=Ayudas()
        show_popup("Ayudas Punto Fijo",ayudar.ayudas_punto_fijo())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Ecuaciones_no_lineales_secantes(Screen):
    pass
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
        print("aquì debe llegar y luego muere?")
        error=verificar.verificar_newton(self.funciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        print("que pvtas es error"+str(error))
        error=""
        if(error==""):
            print("aqui no entra.")
            Funcion=Funciones(self.funciones.text)
            newton.algoritmo_newton(float(self.xi.text),Funcion,float(self.iterations.text),float(self.tolerance.text),self.tipo_error)
            self.sol.text=newton.get_sol()
            columnas=['Iteracion','Xi','F(xm)','Error']
            tabla.dibujar(newton.tabla_valores(),columnas)

        else:
            show_popup("Error newton",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_newton(self.funciones.text, self.xi.text,self.iterations.text,self.tolerance.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text)
        else:
            show_popup("Error Graficar newton",error)

    def ayuda(self):
        ayudar=Ayudas()
        show_popup("help newton",ayudar.ayudas_newton())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo

class Ecuaciones_no_lineales_raices_multiples(Screen):
    pass
class Sistemas_de_ecuaciones_eliminacion_gaussiana(Screen):
    pass
class Sistemas_de_ecuaciones_pivoteo(Screen):
    pass
class Sistemas_de_ecuaciones_Factorizacion_lu(Screen):
    pass
class Sistemas_de_ecuaciones_Factorizacion_matrices(Screen):
    pass
class Sistemas_de_ecuaciones_iterativos(Screen):
    pass
class Interpolacion_newton(Screen):
    pass
class Interpolacion_lagrange(Screen):
    pass
class Interpolacion_splines(Screen):
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
