from dash import html

sidebar = html.Div(
    [
        html.H2("Menu", className="text-2xl font-bold mb-4"),
        html.Hr(className="my-4 border-gray-300"),
        html.Nav(
            [
                html.A("Home", href="/", className="block px-4 py-2 text-gray-700 hover:bg-gray-100 rounded"),


                html.A("Page 1", href="/page-1", className="block px-4 py-2 text-gray-700 hover:bg-gray-100 rounded"),

                html.A("Page 2", href="/page-2", className="block px-4 py-2 text-gray-700 hover:bg-gray-100 rounded"),
            ],
            className="space-y-2"
        ),
    ],
    className="fixed top-0 left-0 h-full w-64 p-4 bg-gray-100"
)
