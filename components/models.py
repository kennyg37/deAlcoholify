from dash import html

def models_layout():
    return html.Div([
        html.H1(["Models"], className="text-3xl font-semibold"),
        html.P(["This is the models page choose a model you want to use"], className="mb-4"),
        html.Div([
            html.Div([
                html.H2("Cancer Model"),
                html.P("This is a cancer model that predicts the likelihood of a person having cancer based on alcohol consumption"),
                html.A("Cancer Model", href="/models/cancer", className="bg-blue-500 text-white p-2 rounded shadow hover:bg-blue-600")
            ], className="mb-4 p-4 bg-white rounded shadow"),
        ])
    ])