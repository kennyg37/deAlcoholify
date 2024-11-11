from dash import html, dcc

def navbar():
    return html.Nav([
        html.Div([
            html.H1("deAlcoholify", className="text-xl font-bold")
        ], className="flex items-center space-x-2"),

        html.Div([
            dcc.Input(
                type="text",
                placeholder="Search...",
                className="px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            )
        ], className="hidden md:block w-1/3"),

        html.Div([
            html.A("Home", href="/", className="text-gray-700 hover:text-blue-500"),
            html.A("Mission", href="/mission", className="text-gray-700 hover:text-blue-500"),
            html.A("About", href="/about", className="text-gray-700 hover:text-blue-500"),
            html.A("contact", href="/contact", className="text-gray-700 hover:text-blue-500"),
        ], className="flex space-x-4")
    ], className="flex justify-between items-center p-4 bg-white shadow-lg fixed top-0 z-10 ml-40 w-[calc(100%-160px)]")
