from dash import html

sidebar = html.Div(
    [
        html.Button(
            html.Span("≡", className="text-xl text-white"),  # Hamburger icon
            id="sidebar-toggle-button",
            className="bg-gray-800 hover:bg-gray-700 rounded p-2 mb-4"
        ),
        html.Hr(className="my-4 border-gray-600"),
        html.Nav(
            [
                html.Div([  
                    html.Img(src="/assets/home.svg", className="w-8 text-gray-300"),
                    html.A("Home", href="/", className="px-4 py-2 text-gray-300 font-semibold hover:bg-gray-700 hover:text-blue-400 w-full rounded flex items-center space-x-2  pl-6"),
                ], className="flex items-center space-x-2 "),
                
                html.Div([  
                    html.Img(src="/assets/data.svg", className="w-8 text-gray-300 "),
                    html.A("Data", href="/data", className="px-4 py-2 text-gray-300 font-semibold hover:bg-gray-700 hover:text-blue-400 w-full rounded flex items-center space-x-2  pl-6 "),
                ], className="flex items-center space-x-2 "),
                
                html.Div([  
                    html.Img(src="/assets/models.svg", className="w-8 text-gray-300 font-size-16 "),
                    html.A("Models", href="/models", className="px-4 py-2 text-gray-300 font-semibold hover:bg-gray-700 hover:text-blue-400 w-full rounded flex items-center space-x-2  pl-4"),
                ], className="flex items-center space-x-2 "),
                html.Div([
                    html.Img(src="/assets/about.svg", className="w-8 text-gray-300 "),
                    html.A("About", href="/about", className="px-4 py-2 text-gray-300 font-semibold hover:bg-gray-700 hover:text-blue-400 w-full rounded flex items-center space-x-2 "),
                ], className="flex items-center space-x-2 "),
                html.Div([
                    html.Img(src="/assets/references.svg", className="w-8 text-gray-300 "),
                    html.A("Refs", href="/references", className="px-4 py-2 text-gray-300 font-semibold hover:bg-gray-700 hover:text-blue-400 w-full rounded flex items-center space-x-2 "),
                ], className="flex items-center space-x-2"),
            ],
            className="space-y-2"
        ),
    ],
    className="fixed top-0 left-0 h-full w-40 p-4 bg-gray-800 shadow-lg"
)
