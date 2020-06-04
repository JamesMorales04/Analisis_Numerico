class Aids:
    def help_search(self):
        data=open("Aids\\NonLinearEq\\Requisites_is.txt", "r")
        return data.read()

    def help_bisection(self):
        data=open("Aids\\NonLinearEq\\Requisites_bisection.txt", "r")
        return data.read()

    def help_regla_falsa(self):
        data=open("Aids\\NonLinearEq\\Requisites_regulifalsi.txt", "r")
        return data.read()

    def help_fixed_point(self):
        data=open("Aids\\NonLinearEq\\ExplanationFixedPoint.txt", "r")
        return data.read()

    def help_newton(self):
        data=open("Aids\\NonLinearEq\\NewtonMethodExplanation.txt", "r")
        return data.read()

    def help_secant(self):
        data=open("Aids\\NonLinearEq\\SecantMethodExplanation.txt", "r")
        return data.read()

    def help_raices_multiples(self):
        data=open("Aids\\NonLinearEq\\MultipleRootsMethodExplanation.txt", "r")
        return data.read()

    def help_gaussian_elimination(self):
        data=open("Aids\\SystemOfEq\\analyzeGaussianElimination.txt", "r")
        return data.read()

    def help_partial_pivot(self):
        data=open("Aids\\SystemOfEq\\PartialPivotingExplanation.txt", "r")
        return data.read()

    def help_total_pivot(self):
        data=open("Aids\\SystemOfEq\\TotalPivotingExplanation.txt", "r")     
        return data.read()

    def help_doolittle(self):
        data=open("Aids\\SystemOfEq\\DoolittleExplanation.txt", "r")
        return data.read()

    def help_croult(self):
        data=open("Aids\\SystemOfEq\\CroultExplanation.txt", "r")
        return data.read()

    def help_GaussSeidel(self):
        data=open("Aids\\SystemOfEq\\GaussSeidelExplanation.txt", "r")
        return data.read()

    def help_jacobi(self):
        data=open("Aids\\SystemOfEq\\JacobiExplanation.txt", "r")
        return data.read()

    def help_staggeredPivoting(self):
        data=open("Aids\\SystemOfEq\\StaggeredPivotingExplanation.txt", "r")
        return data.read()

    def help_lagrange(self):
        data=open("Aids\\InterporlationHelp\\lagrangeHelp.txt", "r")
        return data.read()       

    def help_newton_interpolation(self):
        data=open("Aids\\InterporlationHelp\\newtonHelp.txt", "r")
        return data.read()

    def help_lineal_spline(self):
        data=open("Aids\\InterporlationHelp\\linealSplineHelp.txt", "r")
        return data.read()

    def help_quadratic_spline(self):
        data=open("Aids\\InterporlationHelp\\quadraticSplineHelp.txt", "r")
        return data.read()

    def help_cubic_spline(self):
        data=open("Aids\\InterporlationHelp\\cubicSplineHelp.txt", "r")
        return data.read()
