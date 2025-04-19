
from dash import  html,dash_table,dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm


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
            style_cell={'textAlign': 'left','fontSize': '12px', 'height': '8px'},
            style_header={'background': '#ba1926','color': '#fff','fontWeight':'500' },
            style_data={'whiteSpace': 'normal'},
            page_current=0,
            page_size=10,
        )
    
def figure(fig,id):
    return html.Div(
        className="figure-container",
        children=[
                   dcc.Graph(
                       id=id,
                       figure=fig

                   )
                    ],
               )

def barsfig(df,col,row):
        
    return(px.bar(df,x=col,y=row,log_y=True))

def histogram(df,column):
    return(
    
        go.Histogram(
            x=df[column],
             name='Data',
             nbinsx=30,
             opacity=1,             

        )
    ) 

def scatter_chart(df, x_col, y_col):
    return(px.scatter(
                df,
                x=x_col,
                y=y_col,
                title="Scatter Chart",
               
                template="plotly"
            ))
            
      
def gaussian_curve(df,column):
    return(
        go.Scatter(
            x=df[column],
            y=norm.pdf(df[column],loc=0,scale=1),
            mode='lines',
            name='Gaussian Curve',
            line=dict(color='red')
        )

    )

def merge_figure(figs):
    fig=go.Figure(data=figs)
    fig.update_layout(title="Histograma del porcentaje de personas que usan Transporte Publico")
    return (fig)


