import dash
from dash import dcc, html
from components.sidebar import sidebar
from components.navbar import navbar

external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]
app = dash.Dash(__name__, 
           external_scripts=external_scripts
           )

app.layout = html.Div([
    dcc.Location(id="url"),  
    navbar, 
    html.Div([
        sidebar,
        html.Div(id="page-content", className="ml-64 p-5")
    ], className="flex")
])

@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/page-1":
        return html.H1("Page 1 Content", className="text-2xl font-bold")
    elif pathname == "/page-2":
        return html.H1("Page 2 Content", className="text-2xl font-bold")
    else:
        return html.H1("Home Page Content", className="text-2xl font-bold")

if __name__ == "__main__":
    app.run_server(debug=True)
