import math

class Incremental_Search:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def Operacion(self, valor_inicial,incremento,item,Functions):
        self.valores.append([valor_inicial,Functions.evaluar(valor_inicial)])
        if self.valores[0][1]==0:
            self.raiz=f"{self.valores[0][0]}"
        else:
            if incremento == 0:
                print("Wrong increment")
            else:
                if item<=0:
                    print("Wrong iterator value")
                else:
                    contador=0
                    valor_nuevo=valor_inicial+incremento
                    while (contador<item):
                        self.valores.append([valor_nuevo,Functions.evaluar(valor_nuevo)]) 
                        valor_evaluado_nuevo=Functions.evaluar(valor_nuevo)
                        
                        if((self.valores[contador][1]*valor_evaluado_nuevo)<=0):
                            break
                        
                        valor_nuevo+=incremento
                        contador+=1
                        
                    if self.valores[contador][1]*valor_evaluado_nuevo<0:
                        self.raiz=f"[{round(self.valores[contador][0],2)},{round(valor_nuevo,2)} is an approximated root]"
                    else:
                        if self.valores[contador][1]==0:
                            self.raiz=f"[{round(self.valores[contador][0],2)} is a root]"
                        else:
                            if(valor_evaluado_nuevo==0):
                                self.raiz="[{valor_nuevo} is a root]"
                            else:
                                self.raiz="Exceeded iterations"
    
    def value_table(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)

