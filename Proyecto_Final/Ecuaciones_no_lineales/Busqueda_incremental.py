import math

class Busqueda_incremental:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def Operacion(self, valor_inicial,incremento,item,Funciones):
        self.valores.append([valor_inicial,Funciones.evaluar(valor_inicial)])
        if self.valores[0][1]==0:
            self.raiz=f"{self.valores[0][0]}"
        else:
            if incremento == 0:
                print("El valor asignado al incremento es incorrecto")
            else:
                if item<=0:
                    print("El valor del iterador es incorrecto")
                else:
                    contador=0
                    valor_nuevo=valor_inicial+incremento
                    while (contador<item):
                        self.valores.append([valor_nuevo,Funciones.evaluar(valor_nuevo)]) 
                        valor_evaluado_nuevo=Funciones.evaluar(valor_nuevo)
                        
                        if((self.valores[contador][1]*valor_evaluado_nuevo)<=0):
                            break
                        
                        valor_nuevo+=incremento
                        contador+=1
                        
                    if self.valores[contador][1]*valor_evaluado_nuevo<0:
                        self.raiz=f"[{round(self.valores[contador][0],2)},{round(valor_nuevo,2)}]"
                    else:
                        if self.valores[contador][1]==0:
                            self.raiz=round(self.valores[contador][0],2)
                        else:
                            if(valor_evaluado_nuevo==0):
                                self.raiz=round(valor_nuevo,2)
                            else:
                                self.raiz="fracaso en las iteraciones"
    
    def tabla_valores(self):
        return self.valores
    def get_raiz(self):
        return str(self.raiz)

