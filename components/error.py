from dash import html

def page_notfound():
    return html.Div([
        html.H1("Page Not Found", className="text-4xl font-bold text-white mb-4"),
        html.P(
            "We are currently working on this feature. Please check back later.",
            className="text-gray-400 mb-8"
        ),
    ], className="text-center p-8 shadow-md rounded-lg mb-8")