from components.data import data_layout
from components.models import models_layout
from components.navbar import navbar
from components.home import home_layout
from components.sidebar import sidebar
from components.chatbot import create_chatbot, register_callbacks
from dash import dcc, html
import dash

external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]

external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css"]

app = dash.Dash(__name__, 
           external_scripts=external_scripts,
           external_stylesheets=external_stylesheets
           )

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar(),
    html.Div([
        sidebar,
        html.Div(id="page-content", className="ml-40 pt-16 p-5 flex-1") 
    ], className="flex"),
    create_chatbot()
])

@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/data":
        return data_layout()  
    elif pathname == "/models":
        return models_layout()
    else:
        return home_layout()  # Your home page layout

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
