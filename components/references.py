from dash import html, dcc

def reference_layout():
    datasets = [
        {"title": "Alcohol Use in Adolescents", "description": "Lifetime alcohol use statistics.", "location": " https://rbc.gov.rw/publichealthbulletin/img/rphb_issues/RPHB%204%20(1)%20V5.pdf", "link": "/assets/alcohol_use.pdf"},
        {"title": "Binge Drinking Rates", "description": "Binge drinking rates by gender.", "location": "", "link": "/assets/binge_drinking.pdf"},
        {"title": "Global Alcohol-Related Deaths", "description": "Data on alcohol-related deaths worldwide.","location": "", "link": "/assets/global_deaths.pdf"}
    ]
    return html.Div([
        html.Div([
            html.H1("Reference Datasets", className="text-4xl font-bold text-white mb-4"),
            html.P(
                "Below is a list of datasets used in our analysis. You can download them for further study.",
                className="text-gray-400 mb-8"
            ),
        ], className="text-center bg-gray-900 p-8 shadow-md rounded-lg"),
        
        html.Div([
            html.Div([
                html.H3(dataset['title'], className="text-xl font-semibold text-white"),
                html.P(dataset['description'], className="text-gray-400 mb-2"),
                html.A("Download PDF", href=dataset['link'], className="text-blue-400 underline")
            ], className="bg-gray-800 p-4 rounded shadow-lg")
            for dataset in datasets
        ], className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-screen-lg mx-auto"),
    ], className="p-4 bg-gray-900 min-h-screen")
