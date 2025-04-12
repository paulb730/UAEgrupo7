import pandas as pd 
import numpy as np
"""
1. Crear data frame de datos

"""

df=pd.read_csv('./data/public_transportation_statistics_by_zip_code-1-2.csv', sep=",", usecols=['zip_code', 'public_transportation_pct','public_transportation_population'])

Headers=np.array(df.columns)
def filtrarpct(df):
    result=df[df[str(Headers[1])] >= 0]
    return result[str(Headers[1])]
def agregarfilas(df,fila,contenido):
    df[fila]=contenido
    print(df)
    return df
def obtener_maximo(df, columna):
    return df[columna].max()
def obtenerminimo(df,columna):
    return df[columna].min()

def agruparporsentencia(df):
    agrupar=df.groupby(Headers[1]).agg({
        Headers[1]:'max'

    })
    return agrupar

df1=agregarfilas(df,'Porcentaje_filtrado',filtrarpct(df))

dfmax=obtener_maximo(df,'Porcentaje_filtrado')

print(agruparporsentencia(df1))
# Display the headers of the data

#obtener los headers de la tabla 





