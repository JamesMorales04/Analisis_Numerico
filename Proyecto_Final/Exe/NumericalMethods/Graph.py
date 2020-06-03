from matplotlib import pyplot
from Functions import Functions
class Graph:
    def draw_functionsa(self,function,posicion_inicial,posicion_final):
        Function=Functions(function)
        x= range(int(posicion_inicial), int(posicion_final))
        pyplot.plot(x, [Function.evaluar(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")

        pyplot.show()

    def draw_functionsb(self,function,gfunction,posicion_inicial,posicion_final):
        Function=Functions(function)
        Gfunction=Functions(gfunction)
        
        x= range(int(posicion_inicial), int(posicion_final))

        pyplot.plot(x, [Function.evaluar(i) for i in x])
        pyplot.plot(x, [Gfunction.evaluar(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        pyplot.show()

    def draw_functionsc(self,function,posicion_inicial,posicion_final):
        Function=Functions(function)
        x= range(int(posicion_inicial), int(posicion_final))
        pyplot.plot(x, [Function.evaluar(i) for i in x])
        pyplot.plot(x, [Function.evaluar_derivada(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")

        pyplot.show()
    
    def draw_functionsd(self,function,posicion_inicial,posicion_final):
        Function=Functions(function)
        x= range(int(posicion_inicial), int(posicion_final))
        pyplot.plot(x, [Function.evaluar(i) for i in x])
        pyplot.plot(x, [Function.evaluar_derivada(i) for i in x])
        pyplot.plot(x, [Function.derivarM(Function,2,i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")

        pyplot.show()