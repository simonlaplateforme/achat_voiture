#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output

from app import app, server
from layouts import *
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app':
        return layout()
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
