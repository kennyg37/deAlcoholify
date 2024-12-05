from dash import html

sidebar = html.Div(
    [
       html.Img(
            src="/assets/logo.png",  
            id="sidebar-toggle-button",
            className="cursor-pointer   p-2 mb-4"
        ),
        html.Hr(className="my-4 border-gray-600"),
        html.Nav(
            [
                html.Div([  
                    html.Img(src="/assets/home.svg", className="w-8 text-[#005CAB]"),
                    html.A("Home", href="/", className="px-4 py-2 text-[#005CAB] font-semibold hover:bg-[#005CAB] hover:text-blue-400 w-full rounded flex items-center space-x-2  pl-6"),
                ], className="flex items-center space-x-2 "),

                html.Div([  
                    html.Img(src="/assets/data.svg", className="w-8 text-[#005CAB] "),
                    html.A("Data", href="/data", className="px-4 py-2 text-[#005CAB] font-semibold hover:bg-[#005CAB] hover:text-blue-400 w-full rounded flex items-center space-x-2  pl-6 "),
                ], className="flex items-center space-x-2 "),

                html.Div([  
                    html.Img(src="/assets/models.svg", className="w-8 text-[#005CAB] font-size-16 "),
                    html.A("Models", href="/models", className="px-4 py-2 text-[#005CAB] font-semibold hover:bg-[#005CAB] hover:text-blue-400 w-full rounded flex items-center space-x-2  pl-4"),
                ], className="flex items-center space-x-2 "),
                html.Div([
                    html.Img(src="/assets/about.svg", className="w-8 text-[#005CAB] "),
                    html.A("About", href="/about", className="px-4 py-2 text-[#005CAB] font-semibold hover:bg-[#005CAB] hover:text-blue-400 w-full rounded flex items-center space-x-2 "),
                ], className="flex items-center space-x-2 "),
                html.Div([
                    html.Img(src="/assets/references.svg", className="w-8 text-[#005CAB] "),
                    html.A("Refs", href="/references", className="px-4 py-2 text-[#005CAB] font-semibold hover:bg-[#005CAB] hover:text-blue-400 w-full rounded flex items-center space-x-2 "),
                ], className="flex items-center space-x-2"),
            ],
            className="space-y-2"
        ),
    ],
    className="fixed top-0 left-0 h-full w-40 p-4 bg-[#fdffff] shadow-lg z-index-1000 "
)
