import pandas as pd
import numpy as np


def showdata(file, valor1, valor2):
    # https://decodigo.com/python-leer-archivo-de-excel-con-pandas
    # https://youtu.be/Bn1n1diGv_0
    archivo_excel = pd.read_excel(file)
    # print('head:\n', archivo_excel.info())
    get_columns = list(archivo_excel.columns)
    # print(get_columns)
    # value = archivo_excel['fecha'].values
    # columnas = ['fecha', 'muestra 1 Mpa', 'muestra 2 Mpa']
    columnas = get_columns  # obtiene nombre de todas las columna
    columnas1 = get_columns[1:3]  # obtiene el nombre de ciertas columnas
    show_data = archivo_excel[columnas]  # busca los datos de cada columna
    # print(show_data)
    arreglo = show_data[columnas1].to_numpy()

    mat1 = np.zeros((len(arreglo), 1))
    for i in range(len(arreglo)):
        suma1 = arreglo[i][0] + arreglo[i][1]
        promedio1 = suma1/2
        mat1[i] = promedio1

    mat1 = np.round(mat1, decimals=2)
    # print('promedio 1:\n', mat1)

    crit1 = np.empty([len(mat1), 1], dtype=str, order='C')
    for i in range(len(mat1)):
        if mat1[i] > valor1:
            crit1[i] = "S"
        else:
            crit1[i] = "N"

    # print('crit1:\n', crit1)

    a = 0
    b = 1
    c = 2
    mat2 = np.zeros((len(mat1), 1))
    while c < len(mat1):
        suma2 = (mat1[a] + mat1[b] + mat1[c])
        promedio2 = suma2/3
        mat2[c] = promedio2
        a += 1
        b += 1
        c += 1

    mat2 = np.round(mat2, decimals=2)
    # print('promedio 2:\n', mat2)

    crit2 = np.empty([len(mat2), 1], dtype=str, order='C')
    for i in range(len(mat2)):
        if mat2[i] > valor2:
            crit2[i] = "S"
        elif mat2[i] == 0:
            crit2[i] = "-"
        else:
            crit2[i] = "N"

    # Borro los elementos que tienen cero para que puedan ser graficados
    mat3 = np.delete(mat2, np.where(mat2 == 0), axis=0)
    # print('crit2:\n', crit2)
    # print('mat3:\n', mat3)

    show_data = show_data.assign(prom_1=mat1, prom_2=mat2, crit_1=crit1, crit_2=crit2)  # agrega nuevas columnas
    return show_data  # , mat1, mat3


if __name__ == '__main__':
    data1 = 24
    data2 = 20.5
    showdata('C:\\Users\\lenin\\PycharmProjects\\aceptconcret\\Libro1.xlsx', data1, data2)

