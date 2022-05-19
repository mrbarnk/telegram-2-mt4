import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, no_update
import json

with open('../config/default.json') as f:
  config = json.load(f)


mt5_server = html.Div(
    [
        dbc.Label("MT5 server", html_for="mt5_server"),
        dbc.Input(type="text", id="mt5_server", placeholder="Enter MT5 server", value=config['mt5']['server']),
        # dbc.FormText(
        #     "Are you on email? You simply have to be these days",
        #     color="secondary",
        # ),
    ],
    className="mb-3",
)

mt5_username = html.Div(
    [
        dbc.Label("MT5 username", html_for="mt5_username"),
        dbc.Input(type="text", id="mt5_username", placeholder="Enter MT5 username", value=config['mt5']['username']),
        # dbc.FormText(
        #     "Are you on email? You simply have to be these days",
        #     color="secondary",
        # ),
    ],
    className="mb-3",
)

mt5_password = html.Div(
    [
        dbc.Label("MT5 password", html_for="mt5_password"),
        dbc.Input(
            type="password",
            id="mt5_password",
            placeholder="MT5 password",
            value=config['mt5']['password']
        ),
        # dbc.FormText(
        #     "A password stops mean people taking your stuff", color="secondary"
        # ),
    ],
    className="mb-3",
)

form = dbc.Form([mt5_server, mt5_username, mt5_password, dbc.Button(
    "Save", id="save_tg", color="primary", className="d-grid gap-2 col-12")])


table_header = [
    html.Thead(
        html.Tr([html.Th("Username"), html.Th("Type"), html.Th("Action")]))
]
rows = []
for channel in config['channels']:
    channel = config['channels'][channel]
    badge = dbc.Button(
        [
            "CONNECTED" if channel['status'] == "connected" else "CONNECT",
        ],
        color="success" if channel['status'] == "connected" else "danger",
        outline=True,
        className="position-relative btn-success",
        n_clicks=channel
    )

    rows.append(
        html.Tr([html.Td(channel['url']), html.Td(channel['trading']), badge]))
    # print(channel)


row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody(rows)]

table = dbc.Table(table_header + table_body, bordered=True)


channel_page = html.Div(
    [
        dbc.Toast(
            [html.P("Sorry, you cannot use this feature", className="mb-0")],
            id="simple-toast",
            header="Error",
            icon="danger",
            dismissable=True,
            is_open=False,
        ),
        dbc.Row(
            [
                dbc.Col(table, md=6),
                dbc.Col(form, md=6),
            ]
        ),

    ]
)


# @app.callback(
#     Output("simple-toast", "is_open"),
#     [Input("connect-button", "n_clicks")],
# )
# def open_toast(n):
#     if n == 0:
#         return no_update
#     return True

# return channels_page
