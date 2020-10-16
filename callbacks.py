#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output
from app import app
from layouts import figure


@app.callback(
    Output('id_plot', 'figure'),
    [Input('id_slider', 'value')])
def refresh_figure(value):
    return figure(value)
