import tkinter as tk
from tkinter import filedialog


def centerwindow(ventana, width, higth):
    altura_pantalla = ventana.winfo_screenheight()
    anchura_pantalla = ventana.winfo_screenwidth()

    x = (anchura_pantalla // 2) - (width // 2)
    y = (altura_pantalla // 2) - (higth // 2)
    root.geometry(f"+{x}+{y}")


def abrir_archivo():
    # Abre un archivo y muestra la direccion en un Label
    archivo = filedialog.askopenfilename(initialdir='C://Users//', title='Seleccionar archivo', filetypes=[('*.xlsx', '*.xlsx'), ('*.xls', '*.xls')])
    dir_archivotxt.set(archivo)


root = tk.Tk()
ancho = 600
alto = 400
root.geometry("%dx%d" % (ancho, alto))
root.title('ACI 328-S')
root.resizable(False, False)
root.update()
centerwindow(root, ancho, alto)

# Variables
dir_archivotxt = tk.StringVar()

# Widgets
cargar_archivo = tk.Button(root, text='CARGAR', command=abrir_archivo)
cargar_archivo.grid(row=0, column=0, padx=5, pady=5)
dir_archivo = tk.Label(root, textvariable=dir_archivotxt, fg='blue')
dir_archivo.grid(row=0, column=1, padx=5, pady=5)
root.mainloop()
