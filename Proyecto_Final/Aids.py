class Ayudas:

    def help_busqueda(self):
        data=open("Ayudas\Requisites_is.txt", "r")
        return data.read()
        
    def help_biseccion(self):
        data=open("Ayudas\Requisites_bisection.txt", "r")
        return data.read()

    def help_regla_falsa(self):
        data=open("Ayudas\Requisites_regulifalsi.txt", "r")
        return data.read()

    def help_punto_fijo(self):
        data=open("Ayudas\ExplicacionPuntoFijo.txt", "r")
        return data.read()

    def help_newton(self):
        data=open("Ayudas\\NewtonMethodExplanation.txt", "r")
        return data.read()

    def help_secante(self):
        data=open("Ayudas\\SecantMethodExplanation.txt", "r")
        return data.read()

    def help_raices_multiples(self):
        data=open("Ayudas\\MultipleRootsMethodExplanation.txt", "r")
        return data.read()

    def help_gaussian_elimination():
        data=open("Ayudas\\NonLinearEq\\GaussianEliminationMethodExplanation.txt", "r")

    def help_partial_pivot():
        data=open("Ayudas\\NonLinearEq\\partialPivotMethodExplanation.txt", "r")      