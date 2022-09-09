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
    archivo = filedialog.askopenfilename(initialdir='C:\\Users\\lenin\\PycharmProjects\\aceptconcret', title='Seleccionar archivo', filetypes=[('*.xlsx', '*.xlsx'), ('*.xls', '*.xls')])
    if archivo:
        dir_archivo['text'] = archivo
        pdread.showdata(archivo)
    else:
        dir_archivo['text'] = 'No se ha seleccionado ningun archivo'


def limpiar_tabla():
    tabla.delete(*tabla.get_children())


root = tk.Tk()
ancho = 600
alto = 400
root.geometry("%dx%d" % (ancho, alto))
root.title('ACI 328-S')
root.resizable(False, False)
root.update()
centerwindow(root, ancho, alto)

# Widgets
cargar_archivo = tk.Button(root, text='CARGAR', command=abrir_archivo)
cargar_archivo.grid(row=0, column=0, padx=5, pady=5)
dir_archivo = tk.Label(root, fg='blue')
dir_archivo.grid(row=0, column=1, padx=5, pady=5)

# Tabla
tabla = ttk.Treeview(root, columns=('#1', '#2', '#3', '#4', '#5'), selectmode='extended', show='headings')

# Formateo de columnas
tabla.column('#1', width=100, minwidth=100, stretch=False)  # tk.NO
tabla.column('#2', width=100, minwidth=100, stretch=False)
tabla.column('#3', width=100, minwidth=100, stretch=False)
tabla.column('#4', width=100, minwidth=100, stretch=False)
tabla.column('#5', width=100, minwidth=100, stretch=False)
# Crear encabezado
tabla.heading('#1', text='Fecha', anchor='center')
tabla.heading('#2', text='Muestra 1', anchor='center')
tabla.heading('#3', text='Muestra 2', anchor='center')
tabla.heading('#4', text='Promedio 1', anchor='center')
tabla.heading('#5', text='Promedio 2', anchor='center')
# tabla.insert("", 'end', values=("11:15","Fulanito","¡Hola!"))
tabla.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky='nsew')

root.mainloop()
