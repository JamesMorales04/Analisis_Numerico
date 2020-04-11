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
class Menu_Inicial(Screen):
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
    posicion_inicial=ObjectProperty(None)
    incremento=ObjectProperty(None)
    iteraciones=ObjectProperty(None)
    posicion_inicial=ObjectProperty(None)
    raiz=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        busqueda=Busqueda_incremental()
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_busqueda(self.funciones.text,self.posicion_inicial.text,self.incremento.text,self.iteraciones.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            busqueda.Operacion(float(self.posicion_inicial.text),float(self.incremento.text),float(self.iteraciones.text),Funcion)
            self.raiz.text=busqueda.get_raiz()
            columnas=['Posicion','Valor']
            tabla.dibujar(busqueda.tabla_valores(),columnas)
        else:
            show_popup("Error Busqueda Incremental",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_busqueda(self.funciones.text,self.posicion_inicial.text,self.incremento.text,self.iteraciones.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text,float(self.posicion_inicial.text),math.fabs(float(self.posicion_inicial.text))+(float(self.incremento.text)*float(self.iteraciones.text)),float(self.incremento.text))
        else:
            show_popup("Error Graficar Busqueda Incremental",error)
    
    def ayuda(self):
        ayudar=Ayudas()
        print(ayudar.ayudas_busqueda())
        show_popup("Ayudas Busqueda Incremental",ayudar.ayudas_busqueda())
class Ecuaciones_no_lineales_biseccion(Screen):
    xi=ObjectProperty(None)
    xs=ObjectProperty(None)
    iteraciones=ObjectProperty(None)
    tolerancia=ObjectProperty(None)
    raiz=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        biseccion=Biseccion()
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iteraciones.text,self.tolerancia.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            biseccion.algorimo_biseccion(float(self.xi.text),float(self.xs.text),Funcion,float(self.tolerancia.text),float(self.iteraciones.text),self.tipo_error)
            self.raiz.text=biseccion.get_raiz()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            tabla.dibujar(biseccion.tabla_valores(),columnas)
        else:
            show_popup("Error Biseccion",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iteraciones.text,self.tolerancia.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text,float(self.xi.text),float(self.xs.text),float(self.tolerancia.text))
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
    iteraciones=ObjectProperty(None)
    tolerancia=ObjectProperty(None)
    raiz=ObjectProperty(None)
    funciones=ObjectProperty(None)

    def buscar(self):
        regla_falsa=Regla_falsa()
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iteraciones.text,self.tolerancia.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            regla_falsa.algorimo_regla_falsa(float(self.xi.text),float(self.xs.text),Funcion,float(self.tolerancia.text),float(self.iteraciones.text),self.tipo_error)
            self.raiz.text=regla_falsa.get_raiz()
            columnas=['Iteracion','Xi','Xu','Xm','F(xm)','Error']
            tabla.dibujar(regla_falsa.tabla_valores(),columnas)
        else:
            show_popup("Error Regla_falsa",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_biseccion(self.funciones.text,self.xi.text,self.xs.text,self.iteraciones.text,self.tolerancia.text)
        if(error==""):
            grafica.dibujar_funciones(self.funciones.text,float(self.xi.text),float(self.xs.text),float(self.tolerancia.text))
        else:
            show_popup("Error Graficar Regla Falsa",error)

    def ayuda(self):
        ayudar=Ayudas()
        show_popup("Ayudas Regla Falsa",ayudar.ayudas_regla_falsa())

    def tipo_de_error(self,tipo):
        self.tipo_error=tipo
class Ecuaciones_no_lineales_punto_fijo(Screen):
    xi=ObjectProperty(None)
    iteraciones=ObjectProperty(None)
    tolerancia=ObjectProperty(None)
    raiz=ObjectProperty(None)
    funciones=ObjectProperty(None)
    gfunciones=ObjectProperty(None)
    def buscar(self):
        puntoFijo = PuntoFijo()
        tabla=Tabla()
        verificar=Verificar()
        error=verificar.verificar_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iteraciones.text,self.tolerancia.text)
        if(error==""):
            Funcion=Funciones(self.funciones.text)
            GFuncion=Funciones(self.gfunciones.text)
            puntoFijo.algorimo_puntoFijo(float(self.xi.text),Funcion,GFuncion,float(self.iteraciones.text),float(self.tolerancia.text),self.tipo_error)
            self.raiz.text=puntoFijo.get_raiz()
            columnas=['Iteracion','Xi','F(xm)','Error']
            tabla.dibujar(puntoFijo.tabla_valores(),columnas)

        else:
            show_popup("Error Biseccion",error)

    def graficar(self):
        grafica=Graficar()
        verificar=Verificar()
        error=verificar.verificar_punto_fijo(self.funciones.text,self.gfunciones.text, self.xi.text,self.iteraciones.text,self.tolerancia.text)
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
    pass
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
