import numpy
from matplotlib import pyplot
from Funciones import Funciones
class Graficar:
    def dibujar_funciones(self,funcion,posicion_inicial=-100,posicion_final=100,incremento=1):
        Funcion=Funciones(funcion)
        x = numpy.arange(posicion_inicial, posicion_final,incremento)
        pyplot.plot(x, [Funcion.evaluar(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")


        pyplot.show()

    def dibujar_funciones(self,funcion,gfuncion):
        posicion_inicial=-100
        posicion_final=100
        incremento=1
        Funcion=Funciones(funcion)
        gfuncion=Funcion(gfuncion)
        x = numpy.arange(posicion_inicial, posicion_final,incremento)
        pyplot.plot(x, [Funcion.evaluar(i) for i in x],color=tab.red)
        pyplot.plot(x, [gfuncion.evaluar(i) for i in x],color=tab.blue)

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")


        pyplot.show()