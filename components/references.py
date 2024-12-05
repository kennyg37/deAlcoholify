from dash import html, dcc

def reference_layout():
    datasets = [
        {"title": "Rwanda Public Health Bulletin (RPHB) vol 4", "description": "Lifetime alcohol use statistics in Rwanda.", "link": " https://rbc.gov.rw/publichealthbulletin/img/rphb_issues/RPHB%204%20(1)%20V5.pdf"},
        {"title": "Alcohol Use Disorder research", "description": "Relationship between Alcohol use disorder and different social behaviors.", "link": "https://doi.org/10.35946/arcr.v40.1.01"},
        {"title": "Global Alcohol-Related Deaths", "description": "Data on alcohol-related deaths worldwide.", "link": "https://www.who.int/news/item/25-06-2024-over-3-million-annual-deaths-due-to-alcohol-and-drug-use-majority-among-men"},
        {"title": "Rwanda Demographic and Health Survey 2019-20 by NISR", "description": "Data on health indicators in Rwanda also discusses role of alcohol in gender based violence.", "link": "https://microdata.statistics.gov.rw/index.php/catalog/98"},
        {"title": "Cancer dataset from kaggle", "description": "Dataset on cancer patients and their alcohol consumption patterns.", "link": "https://www.kaggle.com/datasets/rabieelkharoua/cancer-prediction-dataset"},
    ]
    
    additional_links = [
        {"title": "WHO Fact Sheet on Alcohol", "link": "https://www.who.int/news-room/fact-sheets/detail/alcohol#:~:text=Drinking%20alcohol%20is%20associated%20with,anxiety%20and%20alcohol%20use%20disorders."},
        {"title": "World Bank Report on Alcohol Use", "link": "https://documents1.worldbank.org/curated/en/197651468182667049/pdf/536500BRI0ENGL10Box345621B01PUBLIC1.pdf"},
        {"title": "Health Data on Alcohol Use Risks", "link": "https://www.healthdata.org/research-analysis/health-risks-issues/alcohol-use#:~:text=Excessive%20alcohol%20consumption%20can%20lead,disease%2C%20stroke%2C%20and%20some%20cancers"}
    ]

    return html.Div([
        html.Div([
            html.H1("Reference Datasets", className="text-4xl font-bold text-[#005CAB] mb-4"),
            html.P(
                "Below is a list of datasets used in our analysis. You can download them for further study.",
                className="text-[#005CAB] mb-8"
            ),
        ], className="text-center  p-8  pb-8"),
        
        html.Div([
            html.Div([
                html.H3(dataset['title'], className="text-xl font-semibold text-[#005CAB]"),
                html.P(dataset['description'], className="text-black mb-2"),
                html.A("Get data", href=dataset['link'], className="text-blue-400 underline", target="_blank")
            ], className="bg-white p-4 rounded shadow-lg")
            for dataset in datasets
        ], className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-screen-lg mx-auto"),
        
        html.Div([
            html.Div([
                html.H3(link['title'], className="text-xl font-semibold text-[#005CAB]"),
                html.A("Read More", href=link['link'], className="text-blue-400 underline")
            ], className="bg-white p-4 rounded shadow-lg")
            for link in additional_links
        ], className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-screen-lg mx-auto mt-8"),
        
    ], className="p-4 bg-white min-h-screen")