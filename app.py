import dash
from dash import dcc, html
import components as cpt
import analysis as anl
from dash.dependencies import Input, Output
import pandas as pd
import io
import base64
"""
    El gerente en “Electromobility Plus” les dice que el área de marketing ha decidido que
quiere hacer una serie de campañas para ayudar a promover las ventas de scooters. Ustedes
como equipo de análisis de datos deben utilizar los datos del Censo de los Estados Unidos
sobre el uso del transporte público por código postal. El propósito es analizar si el nivel de
uso del transporte público tiene alguna correlación con las ventas de la empresa de scooter
mencionada anteriormente, en una zona postal determinada, de tal manera que el equipo
de marketing pueda realizar una campaña focalizada por zona postal.
"""
"""
Objetivo de la APP 
Ayudar a promover las ventas de scooters    
"""
"""
Como:
Mediante los datos del Censo de USA
Uso del transporte publico por codigo postal 
"""
"""
Proposito:
Nivel de uso del transporte publico tiene alguna correlación con las ventas de 
la empresa de scooter en una zona postal determinada 
"""
#Aqui estaran componentes como tablas y figuras 
dic1=anl.dic
dic2=anl.zonadebajouso
cont=anl.contador
agrupar=anl.agrupar
# Inicializar app DASH
app = dash.Dash(__name__)
# En el layout va todos los componentes web 
app.layout = html.Div([
    cpt.header("Analisis de Electromobility Plus"),
    html.Div([
        cpt.card("1. Data Frame Principal",cpt.table(anl.df)),
        cpt.card("2. Encuentre los porcentajes máximo y mínimo ",[
            cpt.table(anl.dic2),
            cpt.figure(
                cpt.barsfig(dic1,dic1['Porcentaje_filtrado'],dic1['Count']),
                'MAX')]),
        cpt.card("3. Ventas potenciales promedio para clientes que viven en zonas de alto\
                    transporte público ",
                    cpt.table(anl.dic3)),
        cpt.card("4. Zona de Bajo Uso de Transporte Publico",
                 ["Se define que las personas que consumen menor transporte publico estan en el rando del 0 al 2 %",
                    cpt.table(dic2),
                    f"La cantidad de personas que consumen menor transporte publico son: {cont}",]),
        cpt.card("5. Histograma de los datos",
                    cpt.figure(cpt.merge_figure([
                              cpt.histogram(dic2,'public_transportation_pct'),]),
                               "ZONA")),
        cpt.card("6. Agrupe a los potenciales clientes en función del uso del transporte público por\
                    código postal",
                    [cpt.table(agrupar), f"la suma de la poblacion agrupada es: {anl.suma_fix}"]),
        cpt.card("7. Estimación Número promedio de ventas",
                 [anl.str1]),
        cpt.card("8. Gráfico de Dispersión para comprender la relación entre el uso del transporte\
                 publico y las potenciales ventas. Exportación de datos en excel",
                 [cpt.figure(                     
                    cpt.scatter_chart(agrupar,agrupar['Porcentaje'],agrupar['population']),
                    "dispersion"),
                 html.Button(id="exportar",n_clicks=0,children="Exportar a CSV EXCEL",className='card-button'),
                 dcc.Download(id="download-excel")]),
        cpt.card("9. Recomendaciones para el equipo de marketing",[
            html.Button(id="recomendacion",n_clicks=0,
                        children=[html.A("Recomendaciones",
                                        href='https://docs.google.com/document/d/1LJjeBoscP0YKzDgOAQyRWc5p96D_2PtGcuQYec5vncg/edit?usp=sharing', 
                                        target="_blank")],className='card-button'),]) ])])

#callbacks para funciones que ejecuta el usuario 
@app.callback(
        Output("download-excel", "data"),
        Input('exportar', 'n_clicks'),
        prevent_initial_call=True,
    )
def gen_excel(n_clicks):
    return dcc.send_data_frame(agrupar.to_excel, "data.xlsx", sheet_name="Sheet_name_1")
    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)





