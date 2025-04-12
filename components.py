
from dash import  html,dash_table
import pandas as pd


"""
Este script define los componentes web del analisis de datos planteado 

"""
def header(txt:str):
    return html.Header(
        children=[
            html.H1(txt, style={"textAlign": "center"}),
            ],
       )

def card(title, content):
    return html.Div(
        className="card",
        children=[
                html.H3(title, className="card-title"),
                html.Div(content, className="card-body"),
            ],
       
        )


def table(data):
    # Read the CSV file into a pandas DataFrame
    df = data
    # Create a Dash DataTable component
    return dash_table.DataTable(
           columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict('records'),
            style_cell={'textAlign': 'left','fontSize': '8px', 'height': '8px'},
            style_header={'background': '#ba1926','color': '#fff','fontWeight':'500' },
            style_data={'whiteSpace': 'normal'},
            page_current=0,
            page_size=10,
        )
    
def figure(fig):
    return html.Div(
        className="figure-container",
        children=[
                   fig
                    ],
               )
