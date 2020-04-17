from matplotlib import pyplot
from Funciones import Funciones
class Graficar:
    def dibujar_funcionesa(self,funcion,posicion_inicial,posicion_final):
        Funcion=Funciones(funcion)
        x= range(int(posicion_inicial), int(posicion_final))
        pyplot.plot(x, [Funcion.evaluar(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")

        pyplot.show()

    def dibujar_funcionesb(self,funcion,gfuncion,posicion_inicial,posicion_final):
        Funcion=Funciones(funcion)
        Gfuncion=Funciones(gfuncion)
        
        x= range(int(posicion_inicial), int(posicion_final))

        pyplot.plot(x, [Funcion.evaluar(i) for i in x])
        pyplot.plot(x, [Gfuncion.evaluar(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        pyplot.show()

    def dibujar_funcionesc(self,funcion,posicion_inicial,posicion_final):
        Funcion=Funciones(funcion)
        x= range(int(posicion_inicial), int(posicion_final))
        pyplot.plot(x, [Funcion.evaluar(i) for i in x])
        pyplot.plot(x, [Funcion.evaluar_derivada(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")

        pyplot.show()