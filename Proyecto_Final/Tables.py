import tkinter
import pandas as pd
from pandastable import Table, TableModel
class Tables:
    def draw(self,search,columnas):
        ventana =tkinter.Tk()
        tabla= tkinter.Frame(ventana)
        ventana.wm_title("Values Table")
        df = pd.DataFrame(search,columns=columnas)
        table = pt = Table(tabla, dataframe=df,showtoolbar=True, showstatusbar=True)
        tabla.pack(fill='both',expand=True)
        pt.show()
        ventana.mainloop()