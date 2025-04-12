import dash
from dash import dcc, html
import components as cpt
import analysis as anl
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

# Inicializar app DASH
app = dash.Dash(__name__)
# En el layout va todos los componentes web 
app.layout = html.Div([
    cpt.header("Analisis de Electromobility Plus"),
    html.Div([
        cpt.card("1. Data Frame Principal",cpt.table(anl.df)),
        cpt.card("2. Encuentre los porcentajes máximo y mínimo ",["TABLA","FIGURA"]),
        cpt.card("3. Ventas potenciales promedio para clientes que viven en zonas de alto\
                    transporte público ","TABLA"),
        cpt.card("4. Zona de Bajo Uso de Transporte Publico",["TABLA","FIGURA"]),
        cpt.card("5. Histograma de los datos","FIGURA"),
        cpt.card("6. Agrupe a los potenciales clientes en función del uso del transporte público por\
                    código postal",["Tabla","Figura"]),
        cpt.card("7. Estimación Número promedio de ventas",["Tabla","Figura"]),
        cpt.card("8. Gráfico de Dispersión para comprender la relación entre el uso del transporte\
                 publico y las potenciales ventas. Exportación de datos en excel",["FIGURA","BOTON DE EXPORTAR"]),
        cpt.card("9. Recomendaciones para el equipo de marketing",["TABLA","FIGURA"])         




    ])
             ])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)



