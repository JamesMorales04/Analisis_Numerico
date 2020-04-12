import tkinter
import pandas as pd
from pandastable import Table, TableModel
class Tabla:
    def dibujar(self,busqueda,columnas):
        ventana =tkinter.Tk()
        tabla= tkinter.Frame(ventana)
        ventana.wm_title("Tabla de valores")
        df = pd.DataFrame(busqueda,columns=columnas)
        table = pt = Table(tabla, dataframe=df,showtoolbar=True, showstatusbar=True)
        tabla.pack(fill='both',expand=True)
        pt.show()
        ventana.mainloop()