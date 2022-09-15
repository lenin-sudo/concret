import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import pdread


def centerwindow(ventana, width, higth):
    altura_pantalla = ventana.winfo_screenheight()
    anchura_pantalla = ventana.winfo_screenwidth()

    x = (anchura_pantalla // 2) - (width // 2)
    y = (altura_pantalla // 2) - (higth // 2)
    root.geometry(f"+{x}+{y}")


def abrir_archivo():
    # Abre un archivo y muestra la direccion en un Label
    limpiar_tabla()
    archivo = filedialog.askopenfilename(initialdir='C:\\Users\\lenin\\PycharmProjects\\aceptconcret', title='Seleccionar archivo', filetypes=[('*.xlsx', '*.xlsx'), ('*.xls', '*.xls')])
    criter1 = criterio1.get()
    criter2 = criterio2.get()
    if archivo and criter1 and criter2:
        dir_archivo['text'] = archivo
        df = pdread.showdata(archivo, criter1, criter2)
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tabla.insert("", "end", values=row)
    else:
        dir_archivo['text'] = 'No se ha seleccionado ningun archivo. Criterio 1 y Criterio 2 no deben estar vacios'


def limpiar_tabla():
    tabla.delete(*tabla.get_children())


root = tk.Tk()
ancho = 710
alto = 300
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
cargar_archivo = tk.Button(root, text='CARGAR', command=abrir_archivo)
cargar_archivo.grid(row=0, column=0, padx=5, pady=5)
dir_archivo = tk.Label(root, fg='blue')
dir_archivo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text='Criterio 1:').grid(row=1, column=0)
getentryc1 = tk.Entry(root, textvariable=criterio1)
getentryc1.grid(row=1, column=1, padx=5, pady=5)
tk.Label(root, text='Criterio 2:').grid(row=1, column=2)
getentryc2 = tk.Entry(root, textvariable=criterio2)
getentryc2.grid(row=1, column=3, padx=5, pady=5)

# Tabla
tabla = ttk.Treeview(root, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), selectmode='extended', show='headings')
vsb = ttk.Scrollbar(root, orient='vertical', command=tabla.yview)
vsb.place(x=688, y=70, height=225)
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
tabla.heading('#2', text='Muestra 1', anchor='center')
tabla.heading('#3', text='Muestra 2', anchor='center')
tabla.heading('#4', text='Promedio 1', anchor='center')
tabla.heading('#5', text='Promedio 2', anchor='center')
tabla.heading('#6', text='1er Criterio', anchor='center')
tabla.heading('#7', text='2er Criterio', anchor='center')

tabla.grid(row=2, column=0, columnspan=5, pady=5, padx=5, sticky='nsew')

root.mainloop()
