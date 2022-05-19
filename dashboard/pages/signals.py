import json
import dash_bootstrap_components as dbc
from dash import html

def Reverse(lst):
    return [ele for ele in reversed(lst)]

with(open('../config/signals.json')) as f:
  signal_datas = json.load(f)

signal_datas = Reverse(signal_datas)

table_header = [
    html.Thead(html.Tr([html.Th("Pair"), html.Th("Channel"), html.Th("Type"),
               html.Th("Entry"), html.Th("Sl"), html.Th("Tps"), html.Th("Time")]))
]

rows = []
for signal in signal_datas:
    rows.append(html.Tr([html.Td(signal['pair']), html.Td(signal['channel']), html.Td(
        signal['type']), html.Td(signal['entry']), html.Td(signal['sl']), html.Td(signal['tps']), html.Td(signal['time'])]))


table_body = [html.Tbody(rows)]

signals = dbc.Table(table_header + table_body, bordered=True)
