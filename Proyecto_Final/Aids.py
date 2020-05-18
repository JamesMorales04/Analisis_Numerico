class Aids:

    def help_busqueda(self):
        data=open("Aids\\NonLinearEq\\Requisites_is.txt", "r")
        return data.read()
        
    def help_biseccion(self):
        data=open("Aids\\NonLinearEq\\Requisites_bisection.txt", "r")
        return data.read()

    def help_regla_falsa(self):
        data=open("Aids\\NonLinearEq\\Requisites_regulifalsi.txt", "r")
        return data.read()

    def help_punto_fijo(self):
        data=open("Aids\\NonLinearEq\\ExplicacionPuntoFijo.txt", "r")
        return data.read()

    def help_newton(self):
        data=open("Aids\\NonLinearEq\\NewtonMethodExplanation.txt", "r")
        return data.read()

    def help_secante(self):
        data=open("Aids\\NonLinearEq\\SecantMethodExplanation.txt", "r")
        return data.read()

    def help_raices_multiples(self):
        data=open("Aids\\NonLinearEq\\MultipleRootsMethodExplanation.txt", "r")
        return data.read()

    def help_gaussian_elimination(self):
        data=open("Aids\\SystemOfEq\\analyzeGaussianElimination.txt", "r")
        return data.read()

    def help_partial_pivot(self):
<<<<<<< HEAD
        data=open("Aids\\NonLinearEq\\PartialPivotingExplanation.txt", "r")
        return data.read()

    def help_total_pivot(self):
        data=open("Aids\\NonLinearEq\\TotalPivotingExplanation.txt", "r")
        return data.read()     
=======
        data=open("Aids\\SystemOfEq\\PartialPivotingExplanation.txt", "r")
        return data.read()
  
    def help_total_pivot(self):
        data=open("Aids\\SystemOfEq\\PartialPivotingExplanation.txt", "r")     
        return data.read()

    def help_doolittle(self):
        data=open("Aids\\SystemOfEq\\PartialPivotingExplanation.txt", "r")
        return data.read()
>>>>>>> 13e626c87c481c13872e1d8ec55e2252de686d1c
