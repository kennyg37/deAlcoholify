from dash import html, dcc

def data_layout():
    return html.Div([
        
        html.Div(
            html.H1(
                "Data Dive: Alcohol Consumption and Other Health Sectors",
                className="text-3xl font-bold text-center mb-8",
                style={"color": "#005CAB"}
            )
        ),
        
        
        html.Div([
            html.H2("A Report on Alcohol Consumption in Relation to Gender-Based Violence by ", style={"color": "black"}), 
            html.A("NISR and other sources", href="https://www.statistics.gov.rw/", target="_blank", style={"color": "#005CAB"}),
            html.P(
                "Explore the data on alcohol consumption and its relationship to gender-based violence. "
                "Click on each card to dive deeper into specific aspects of the data.",
                style={"color": "black"}
            ),
        ], className="p-5 bg-white text-center"),
        
        html.Div([
            # Card 1
            html.Div([
                html.Div([
                    html.Img(src="https://www.sdlaw.co.za/admin/wp-content/uploads/2019/10/Webp.net-resizeimage-16-2.jpg", className="w-full h-48 object-cover"),
                    html.H3("Alcohol and Gender-Based Violence: Key Findings", className="text-xl font-bold mt-4", style={"color": "black"}),
                    html.P("An analysis of how alcohol consumption correlates with incidents of violence.", className="text-gray-700"),
                    dcc.Link("Read More", href="/data/impact-alcohol-violence", className="text-blue-400 mt-3")
                ], className="p-5 bg-gray-100 rounded-lg hover:shadow-lg")
            ], className="w-1/4 p-4"),
            
            
            html.Div([
                html.Div([
                    html.Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxtDhcV27yreRV8nWZw1JeB781hC83jWAcpg&s", className="w-full h-48 object-cover"),
                    html.H3("Why is Reducing Alcohol-Related Problems a Priority?", className="text-xl font-bold mt-4", style={"color": "black"}),
                    html.P("Alcohol abuse is increasingly becoming a significant public health issue across Africa, contributing.", className="text-gray-700"),
                    dcc.Link("Read More", href="/data/whyreducing", className="text-blue-400 mt-3")
                ], className="p-5 bg-gray-100 rounded-lg hover:shadow-lg")
            ], className="w-1/4 p-4"),
            
            
            html.Div([
                html.Div([
                    html.Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8s8j0xefi1AkRX9l02rTdGaPletTVss_1rw&s", className="w-full h-48 object-cover"),
                    html.H3("Global Impact of Alcohol Consumption", className="text-xl font-bold mt-4", style={"color": "black"}),
                    html.P("Alcohol abuse is a major global health and social issue, responsible for a significant burden of.", className="text-gray-700"),
                    dcc.Link("Read More", href="data/globalimpact", className="text-blue-400 mt-3")
                ], className="p-5 bg-gray-100 rounded-lg hover:shadow-lg")
            ], className="w-1/4 p-4"),
            
            # Card 4
            html.Div([
                html.Div([
                    html.Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCDLR7_k95mdQWKe6I9chTsNV8Z9bRTw5R6w&s", className="w-full h-48 object-cover"),
                    html.H3("Alcohol Use: A Leading Global Risk Factor", className="text-xl font-bold mt-4", style={"color": "black"}),
                    html.P("This page highlights key statistics about the harmful impact of alcohol use on global health.", className="text-gray-700"),
                    dcc.Link("Read More", href="data/statistics", className="text-blue-400 mt-3")
                ], className="p-5 bg-gray-100 rounded-lg hover:shadow-lg")
            ], className="w-1/4 p-4"),

        ], className="flex flex-wrap justify-between mt-8"),  # Ensuring cards are flexed in a row
        
    ], className="p-5 bg-white text-black min-h-screen")
