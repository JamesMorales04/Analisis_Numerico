class Ayudas:

    def ayudas_busqueda(self):
        datos=open("Proyecto_Final\Ayudas\Requisites_is.txt", "r")
        return datos.read()
        
    def ayudas_biseccion(self):
        datos=open("Proyecto_Final\Ayudas\Requisites_bisection.txt", "r")
        return datos.read()

    def ayudas_regla_falsa(self):
        datos=open("Proyecto_Final\Ayudas\Requisites_regulifalsi.txt", "r")
        return datos.read()

    def ayudas_punto_fijo(self):
        datos=open("Proyecto_Final\Ayudas\ExplicacionPuntoFijo.txt", "r")
        return datos.read()

    def ayudas_newton(self):
        pass

    def ayudas_secante(self):
        pass  
    def ayudas_raices_multiples(self):
        pass  
      