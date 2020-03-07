import tkinter
import tkinter.ttk as tk
import math
import numpy
from pandastable import Table, TableModel
import pandas as pd
from matplotlib import pyplot
from Funciones import Funciones
from Busqueda_incremental import Busqueda_incremental


class Graficador:

    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("Metodos Numericos")
        self.root.config(width=600, height=600)
        self.menu = tkinter.Frame(self.root)
        self.valido=False
    
    def clear(self):
        for widget in self.menu.winfo_children():
            widget.destroy()

    def menu_capitulos(self):
        self.menu.grid()
        self.clear()
        ecuaciones_no_lineales=tkinter.Button(self.menu,width=80,height=7,text="Capitulo 1: Ecuaciones no Lineales", command=self.menu_capitulo1).pack()
        sistemas_de_ecuaciones=tkinter.Button(self.menu,width=80,height=7, text="Capitulo 2: Sistemas de Ecuaciones", command=self.ejecutar_seccion2).pack()
        interpolacion=tkinter.Button(self.menu,width=80,height=7, text="Capitulo 3: Interpolacion", command=self.ejecutar_seccion3).pack()
        diferenciacion_integracion=tkinter.Button(self.menu,width=80,height=7, text="Capitulo 4: Diferenciacion e integracion", command=self.ejecutar_seccion4).pack()

    def menu_capitulo1(self):
        self.clear()
        Busqueda_incremental_boton=tkinter.Button(self.menu,width=80,height=7,text="Algoritmo 1: Busqueda Incremental", command=self.ejecutar_seccion1_busqueda).pack()
        biseccion_boton=tkinter.Button(self.menu,width=80,height=7, text="Algoritmo 2: Biseccion", command=self.ejecutar_seccion1_biseccion).pack()
        regla_falsa_boton=tkinter.Button(self.menu,width=80,height=7, text="Algoritmo 3: Regla Falsa", command=self.ejecutar_seccion1_regla_falsa).pack()
        punto_fijo_boton=tkinter.Button(self.menu,width=80,height=7, text="Algoritmo 4: Punto Fijo", command=self.ejecutar_seccion1_punto_fijo).pack()
        volver=tkinter.Button(self.menu,width=80,height=3, text="Volver", command=self.menu_capitulos).pack()
    
    def ejecutar_seccion1_busqueda(self):
        self.clear()

        funcion=tkinter.StringVar()
        valor_inicial=tkinter.DoubleVar()
        incremento=tkinter.DoubleVar()
        iteraciones=tkinter.DoubleVar()

        texto_funcion=tk.Label(self.menu, text="Funcion f(x)").place(x=40,y=20)
        texto_valor_inicial=tk.Label(self.menu, text="Valor Inicial").place(x=40,y=60)
        texto_incremento=tk.Label(self.menu, text="Incremento").place(x=210,y=60)
        texto_iteraciones=tk.Label(self.menu, text="Iteraciones").place(x=370,y=60)

        entrada_funcion = tk.Entry(self.menu,textvariable=funcion,justify=tkinter.CENTER,width=70).place(x=120,y=20)
        entrada_valor_inicial = tk.Entry(self.menu,textvariable =valor_inicial,justify=tkinter.CENTER,width=10).place(x=120,y=60)
        entrada_incremento = tk.Entry(self.menu,textvariable =incremento,justify=tkinter.CENTER,width=10).place(x=280,y=60)
        entrada_iteraciones = tk.Entry(self.menu,textvariable =iteraciones,justify=tkinter.CENTER,width=10).place(x=440,y=60)

        
        confirmar = tk.Button(self.menu, text="Confirmar",command=lambda: self.verificar(funcion.get(),valor_inicial.get(),incremento.get(),iteraciones.get())).place(x=200,y=100)
        Volver = tk.Button(self.menu, text="Volver",command=self.menu_capitulo1).place(x=300,y=100)
        
        graficar = tkinter.Button(self.menu,width=70,height=4, text="Graficar",command=lambda: self.dibujar_funciones(funcion.get(),valor_inicial.get(),math.fabs(valor_inicial.get())+math.fabs((incremento.get()*iteraciones.get())),incremento.get())).place(x=40,y=220)
        buscar=tkinter.Button(self.menu,width=70,height=4, text="Ejecutar Busqueda",command=lambda: self.ejecutar_busqueda_incremental(funcion.get(),valor_inicial.get(),incremento.get(),iteraciones.get())).place(x=40,y=320)

    def ejecutar_seccion1_biseccion(self):
        pass

    def ejecutar_seccion1_regla_falsa(self):
        pass

    def ejecutar_seccion1_punto_fijo(self):
        pass
    
    def ejecutar_busqueda_incremental(self,funcion,valor_inicial,incremento,iteraciones):
        self.verificar(funcion,valor_inicial,incremento,iteraciones)
        if(self.valido):
            busqueda=Busqueda_incremental()
            funcion_convertida=Funciones(funcion)
            busqueda.Operacion(valor_inicial,incremento,iteraciones,funcion_convertida)
            self.tabla_valores(busqueda.tabla_valores())
            self.mostrar_raiz(busqueda.get_raiz())
    
    def ejecutar_seccion2(self):
        pass
    
    def ejecutar_seccion3(self):
        pass

    def ejecutar_seccion4(self):
        pass


    def verificar_funcion(self,funcion,valor_inicial):
        if(funcion==''):
            return True
        else: 
            try:
                prueba_funcion=Funciones(funcion)
                prueba_funcion.evaluar(valor_inicial)
                return False
            except:
                return True
                
    
    def verificar(self,funcion,valor_inicial,incremento,iteraciones):
        error=""
        if(self.verificar_funcion(funcion,valor_inicial)):
            error+="La funcion es invalida, \n Los comandos son: Potencia x**2 \n Raiz= sqrt(x) \n Logaritmo natura= log(x) \n pi= pi \n seno,cose,tangente= sen(x),cos(x),tan(x)"
        if(incremento==0):
            error+="\nEl incremento ingresado es invalido "
        if(iteraciones==0):
            error+="\nLas iteraciones ingresadas son invalidas "
        if error!="":
            self.error_window(error)
        else:
            self.valido=True

    def error_window(self,error):
        self.valido=False
        ventana = tkinter.Toplevel()
        ventana.wm_title("Error")
        texto= tk.Label(ventana, text=error)
        texto.grid(row=0, column=0)
        cerrar = tk.Button(ventana, text="Okay", command=ventana.destroy)
        cerrar.grid(row=1, column=0)


    def dibujar_funciones(self,funcion,posicion_inicial,posicion_final,incremento):
        self.verificar(funcion,posicion_inicial,posicion_final,posicion_final)
        if(self.valido):
            Funcion=Funciones(funcion)
            
            x = numpy.arange(posicion_inicial, posicion_final,incremento)
            pyplot.plot(x, [Funcion.evaluar(i) for i in x])

            pyplot.axhline(0, color="black")
            pyplot.axvline(0, color="black")


            pyplot.show()

    def mostrar_raiz(self,raiz):
        texto_raiz=tk.Label(self.menu, text="La raiz esta en: ").place(x=40,y=160)
        texto_raiz_resultado=tkinter.Label(self.menu,width=20,bg='white',relief="sunken",borderwidth=2,text=raiz).place(x=150,y=160)

    def tabla_valores(self,busqueda):
        ventana = tkinter.Toplevel()
        ventana.wm_title("Tabla de valores")
        df = pd.DataFrame(busqueda,columns=['Posicion','Valor'])
        table = pt = Table(ventana, dataframe=df,showtoolbar=True, showstatusbar=True)
        pt.show()

    

 
