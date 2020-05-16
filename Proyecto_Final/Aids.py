class Aids:

    def help_busqueda(self):
        data=open("Aids\Requisites_is.txt", "r")
        return data.read()
        
    def help_biseccion(self):
        data=open("Aids\Requisites_bisection.txt", "r")
        return data.read()

    def help_regla_falsa(self):
        data=open("Aids\Requisites_regulifalsi.txt", "r")
        return data.read()

    def help_punto_fijo(self):
        data=open("Aids\ExplicacionPuntoFijo.txt", "r")
        return data.read()

    def help_newton(self):
        data=open("Aids\\NewtonMethodExplanation.txt", "r")
        return data.read()

    def help_secante(self):
        data=open("Aids\\SecantMethodExplanation.txt", "r")
        return data.read()

    def help_raices_multiples(self):
        data=open("Aids\\MultipleRootsMethodExplanation.txt", "r")
        return data.read()

    def help_gaussian_elimination(self):
        data=open("Aids\\NonLinearEq\\analyzeGaussianElimination.txt", "r")
        return data.read()

    def help_partial_pivot(self):
        data=open("Aids\\NonLinearEq\\PartialPivotingExplanation.txt", "r")      