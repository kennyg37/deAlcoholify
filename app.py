import dash
from dash import dcc, html
from components.sidebar import sidebar
from components.chatbot import create_chatbot, register_callbacks

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
    html.Div([
        sidebar,
        html.Div(id="page-content", className="ml-64 p-5 flex-1")
    ], className="flex"),
    create_chatbot()  # Add the chatbot component here
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

# Register chatbot callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
