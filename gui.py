import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import pdread


def centerwindow(ventana, width, higth):
    # Centra la ventana en la pantalla
    altura_pantalla = ventana.winfo_screenheight()
    anchura_pantalla = ventana.winfo_screenwidth()

    x = (anchura_pantalla // 2) - (width // 2)
    y = (altura_pantalla // 2) - (higth // 2)
    root.geometry(f"+{x}+{y}")


def abrir_archivo():
    # Abre un archivo y muestra la direccion en un Label
    limpiar_tabla()
    archivo = filedialog.askopenfilename(initialdir='C:\\Users\\lenin\\PycharmProjects\\aceptconcret', title='Seleccionar archivo', filetypes=[('*.xlsx', '*.xlsx'), ('*.xls', '*.xls')])

    # Obtiene el valor de las variables limites
    criter1 = criterio1.get()
    criter2 = criterio2.get()

    # Si se cumple con los requisitos se procesa la hoja de calculo
    if archivo and criter1 and criter2:
        dir_archivo['text'] = archivo  # Para vizualizar que se estra procesando un archivo

        # Se envia los datos para el procesamiento
        df = pdread.showdata(archivo, criter1, criter2)  # Devuelve un Data Frame para el TreeView y dos Matrices Numpy para graficar
        df_rows = df.to_numpy().tolist()  # Convierte los elementos del DataFrame en una cadena
        for row in df_rows:
            tabla.insert("", "end", values=row)  # Coloca los elementos del DF en el Treeview

        # Extracion de las columnas de interes para la grafica
        date = list(df.columns)[0:1]
        average1 = list(df.columns)[3:4]
        average2 = list(df.columns)[4:5]

        # Convertir a formato numpy para eliminar el nombre de la columna
        dat = df[date].to_numpy()
        np_aver1 = df[average1].to_numpy()
        np_aver2 = df[average2].to_numpy()
        np_aver2 = np.delete(np_aver2, np.where(np_aver2 == 0), axis=0)  # Elimina las dos primeras filas ya que son cero y no se grafican
        dat_1 = np.delete(dat, [0, 1], axis=0)  # Se elimina las dos primeras filas para que coincida con la dimension de np_aver2

        # https://youtu.be/5OKzCXha4Co
        # Grafico
        plt.cla()
        fig, (axs1, axs2) = plt.subplots(2, 1, dpi=50, figsize=(14, 8.5), facecolor='#f1199c')
        # Primer grafico
        axs1.plot(dat, np_aver1, 'o-')
        axs1.set_xlabel('RESISTENCIA ' + str(criter1) + ' MPa')
        axs1.set_ylabel('RESISTENCIA MPa')
        axs1.grid(axis='y')
        axs1.axhline(criter1, color='r', xmax=1)
        axs1.tick_params(axis='x', labelrotation=45)  # Modifica la presentacion de las etiquetas
        # Segundo grafico
        axs2.plot(dat_1, np_aver2, 'd-')
        axs2.set_xlabel('RESISTENCIA ' + str(criter2) + ' MPa')
        axs2.set_ylabel('RESISTENCIA MPa')
        axs2.grid(axis='y')
        axs2.axhline(criter2, color='g', xmax=1)
        axs2.tick_params(axis='x', labelrotation=45)
        fig.tight_layout()

        # Colocar los graficos Matplolib el Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0, columnspan=3)
    else:
        dir_archivo['text'] = 'No se ha seleccionado ningun archivo. Criterio 1 y Criterio 2 no deben estar vacios'


def limpiar_tabla():
    tabla.delete(*tabla.get_children())


def _salir():
    root.quit()
    root.destroy()
# VENTANA TK


root = tk.Tk()
ancho = 710
alto = 620
root.geometry("%dx%d" % (ancho, alto))
root.title('ACI 328-S')
root.configure(bg='#A2EFFF')
root.resizable(False, False)
root.update()
centerwindow(root, ancho, alto)

# Variables
criterio1 = tkinter.DoubleVar()
criterio1.set(24)
criterio2 = tkinter.DoubleVar()
criterio2.set(20.5)

# Widgets
cargar_archivo = tk.Button(root, text='CARGAR ARCHIVO:', relief='flat', bg='#f9aa31', command=abrir_archivo)
cargar_archivo.place(x=5, y=5)
button_quit = tk.Button(root, text="Quit", relief='flat', bg='#f93155', command=_salir)
button_quit.place(x=670, y=5)
dir_archivo = tk.Label(root, fg='#9c3717', bg='#A2EFFF')
dir_archivo.place(x=130, y=5)

tk.Label(root, text='Criterio 1:', bg='#A2EFFF').place(x=5, y=40)
getentryc1 = tk.Entry(root, textvariable=criterio1)
getentryc1.place(x=65, y=40, width=50)
tk.Label(root, text='Criterio 2:', bg='#A2EFFF').place(x=150, y=40)
getentryc2 = tk.Entry(root, textvariable=criterio2)
getentryc2.place(x=210, y=40, width=50)

# Tabla
tabla = ttk.Treeview(root, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), selectmode='extended', show='headings', height=5)
vsb = ttk.Scrollbar(root, orient='vertical', command=tabla.yview)
vsb.place(x=688, y=65, height=125)
tabla.configure(yscrollcommand=vsb.set)

# Formateo de columnas
tabla.column('#1', width=120, minwidth=100, stretch=False)  # tk.NO
tabla.column('#2', width=100, minwidth=100, stretch=False)
tabla.column('#3', width=100, minwidth=100, stretch=False)
tabla.column('#4', width=100, minwidth=100, stretch=False)
tabla.column('#5', width=100, minwidth=100, stretch=False)
tabla.column('#6', width=80, minwidth=80, stretch=False)
tabla.column('#7', width=80, minwidth=80, stretch=False)

# Crear encabezado
tabla.heading('#1', text='Fecha', anchor='center')
tabla.heading('#2', text='Ensayo 1', anchor='center')
tabla.heading('#3', text='Ensayo 2', anchor='center')
tabla.heading('#4', text='Promedio 1', anchor='center')
tabla.heading('#5', text='Promedio 2', anchor='center')
tabla.heading('#6', text='1er Criterio', anchor='center')
tabla.heading('#7', text='2er Criterio', anchor='center')

tabla.place(x=5, y=65)

# frame para la grafica
frame = tk.Frame(root)
frame.place(x=5, y=194)

root.mainloop()

# http://research.iac.es/sieinvens/python-course/matplotlib.html
# https://pythonguides.com/matplotlib-plot-numpy-array/
# https://www.pythontutorial.net/tkinter/tkinter-matplotlib/
# https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
