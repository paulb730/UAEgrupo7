import pandas as pd 
import numpy as np


df=pd.read_csv('./data/public_transportation_statistics_by_zip_code-1-2.csv', sep=",", usecols=['zip_code', 'public_transportation_pct','public_transportation_population'])
Headers=np.array(df.columns)
def filtrarpct(df):
    result=df[df[str(Headers[1])] >= 0]
    return result[str(Headers[1])]
def agregarfilas(df,fila,contenido):
    df[fila]=contenido
    
    return df
def agruparporsentencia(df):
    agrupar=df.groupby(Headers[1]).agg({
        'Porcentaje_filtrado':'max'

    })
    return agrupar
def getmaxminvalue(df,textcol,flag):
    #agrupar valores 
    grouped_counts = df.groupby('Porcentaje_filtrado').size()
    grouped_counts=pd.DataFrame(grouped_counts)
    # Reset the index of grouped_counts to transform it into a DataFrame
    grouped_counts = grouped_counts.reset_index()
    # Rename the columns for better readability
    grouped_counts.columns = [textcol, 'Count']
    maxvalue=grouped_counts[textcol].max()
    minvalue=grouped_counts[textcol].min()
    # Filter rows where 'Porcentaje_filtrado' equals the maximum value
    row_with_max = grouped_counts[grouped_counts['Porcentaje_filtrado'] == maxvalue]
    # Filter rows where 'Porcentaje_filtrado' equals the minimum value
    row_with_min = grouped_counts[grouped_counts['Porcentaje_filtrado'] == minvalue]
    # Create DataFrames for rows with max and min values
    df_row_with_max = pd.DataFrame(row_with_max)
    df_row_with_min = pd.DataFrame(row_with_min)
    # Merge the DataFrames for rows with max and min values
    merged_df = pd.concat([df_row_with_max, df_row_with_min], ignore_index=True)
    
    #normalize count
    if flag:
        merged_df['Count'] = (merged_df['Count'] ) / (10000)
    return(merged_df)
def ventaspotenciales(df,pct):
    #calculo de cuantas personas pueden comprar el producto que usan el transporte publico al 10%
    ventas=df["public_transportation_population"][df["public_transportation_pct"]>=pct].sum()
    #calculo de ventas para 
    ventas_l10=df[(df["public_transportation_pct"]<10)&(df["public_transportation_pct"]>0)]["public_transportation_population"].sum()
    dict={
        "Ventas mayor al 10'%": [ventas],
        "Ventas menor al 10%": [ventas_l10]
    }
    
    return create_dataframe_from_dict(dict)
# Create a DataFrame from a dictionary
def create_dataframe_from_dict(data_dict):
    return pd.DataFrame(data_dict)
df1=agregarfilas(df,'Porcentaje_filtrado',filtrarpct(df))
dic=getmaxminvalue(df1,'Porcentaje_filtrado',True)
dic2=getmaxminvalue(df1,'Porcentaje_filtrado',False)
dic3=ventaspotenciales(df,10)
zonadebajouso=df[(df['public_transportation_pct']<2) &(df['public_transportation_pct']>0)]
contador=zonadebajouso['public_transportation_population'].sum()
#6 AGRUPAR CLIENTES POR % DE USO, PROMEDIO DE VENTAS, DIAGRAMA DE DISPORSION, EXPORTAR A EXCEL
sumap=df1["public_transportation_population"].sum()
#print(f"la suma de la poblacion es: {sumap}")
str1=f"El promedio de ventas por código postal es: {df1["public_transportation_population"].mean()}"
df_group=df1.groupby("Porcentaje_filtrado")["public_transportation_population"].sum().reset_index()
df_group.columns=["Porcentaje","population"]
df_group['zip_code']=df1['zip_code']
suma_fix=df_group.sum()
agrupar=df_group
#df_group.columns["population"]









    







