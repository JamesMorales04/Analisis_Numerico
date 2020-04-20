class Ayudas:

    def ayudas_busqueda(self):
        data=open("Ayudas\Requisites_is.txt", "r")
        return data.read()
        
    def ayudas_biseccion(self):
        data=open("Ayudas\Requisites_bisection.txt", "r")
        return data.read()

    def ayudas_regla_falsa(self):
        data=open("Ayudas\Requisites_regulifalsi.txt", "r")
        return data.read()

    def ayudas_punto_fijo(self):
        data=open("Ayudas\ExplicacionPuntoFijo.txt", "r")
        return data.read()

    def ayudas_newton(self):
        data=open("Ayudas\\NewtonMethodExplanation.txt", "r")
        return data.read()

    def ayudas_secante(self):
        data=open("Ayudas\Requisites_secant.txt", "r")
        pass  
    def ayudas_raices_multiples(self):
        data=open("Ayudas\\Requisites_multipleroot.txt", "r")
        pass
      