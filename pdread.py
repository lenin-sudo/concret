import pandas as pd
import xlrd
import numpy as np


def showdata(file):
    # https://decodigo.com/python-leer-archivo-de-excel-con-pandas
    # https://youtu.be/Bn1n1diGv_0
    archivo_excel = pd.read_excel(file)
    # print('head:\n', archivo_excel.info())
    get_columns = list(archivo_excel.columns)
    # print(get_columns)
    # value = archivo_excel['fecha'].values
    # columnas = ['fecha', 'muestra 1 Mpa', 'muestra 2 Mpa']
    columnas = get_columns  # obtiene nombre de cada columna
    show_data = archivo_excel[columnas]  # busca los datos de cada columna
    print(show_data)


# if __name__ == '__main__':
# showdata()

