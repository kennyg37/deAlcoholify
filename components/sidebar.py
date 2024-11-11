from dash import html

sidebar = html.Div(
    [
        html.Button(
            html.Span("≡", className="text-xl"),  # Hamburger icon
            id="sidebar-toggle-button",
            className="bg-gray-200 hover:bg-gray-300 rounded p-2 mb-4"
        ),
        html.Hr(className="my-4 border-gray-300"),
        html.Nav(
            [
                html.Div([  
                    html.Img(src="/assets/home.svg", className="w-8 mx-auto"),  
                    html.A("Home", href="/", className="block px-4 py-2 text-gray-700 rounded font-semibold"),
                ], className="items-center flex gap-2 justify-center rounded-lg hover:bg-white"),

                html.Div([  
                    html.Img(src="/assets/data.svg", className="w-8 mx-auto"),  
                    html.A("Data", href="/data", className="block px-4 py-2 text-gray-700 hover:bg-gray-100 rounded font-semibold"),
                ], className="space-y-2 flex gap-2 items-center"),

                html.Div([
                    html.Img(src="/assets/models.svg", className="w-8 mx-auto"),
                    html.A("Models", href="/models", className="block px-4 py-2 text-gray-700 hover:bg-gray-100 rounded font-semibold"),
                ], className="space-y-2 flex gap-2 items-center"),
            ],
            className="space-y-2"
        ),
    ],
    className="fixed top-0 left-0 h-full w-40 p-4 bg-gray-100"
)
