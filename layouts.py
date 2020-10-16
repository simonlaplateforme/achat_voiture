#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

car_data = pd.read_csv("carData.csv")


def layout(year=2010):
    la = html.Div([
        dcc.Graph(
            id='id_plot',
            figure=figure(year)
        ),
        html.P("Choix de l'année :"),
        dcc.Slider(
            id="id_slider",
            min=2003,
            max=2018,
            step=1,
            value=2011,
            marks={i: '{}' . format(i) for i in range(2003, 2019)},
        ),
    ])
    return la


def figure(year):
    x_reg = car_data[car_data.Year == year]["Kms_Driven"]
    fit = np.polyfit(car_data[car_data.Year == year]["Kms_Driven"], car_data[car_data.Year == year]["Selling_Price"], 1)
    y_reg = [fit[0] * x + fit[1] for x in x_reg]
    fig = {
        'data': [
            go.Scatter(
                name="Données de l'année {}" . format(year),
                x=x_reg,
                y=car_data[car_data.Year == year]["Selling_Price"],
                mode='markers',
                opacity=0.8,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
            ),
            go.Scatter(
                name="regression linéaire",
                x=x_reg,
                y=y_reg,
                mode="lines+markers",
            )
        ],
        'layout': go.Layout(
            xaxis={'title': 'Kms Driven'},
            yaxis={'title': 'Selling Price'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0.0, 'y': 1},
            hovermode='closest'
        )
    }
    return fig
