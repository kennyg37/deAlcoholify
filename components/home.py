from dash import html, dcc, callback, Input, Output
import plotly.express as px
import plotly.graph_objs as go
from components.breakdown import create_dashboard_component, gender_alcohol_stats

alcohol_use = [56.1, 43.9]  
binge_drinking_male = [13.7, 2.7]  

fig_alcohol = px.pie(
    names=["Have Tried Alcohol", "Abstinent"],
    values=alcohol_use,
    title="Lifetime Alcohol Use among Adolescents",
    color_discrete_sequence=["#005CAB", "#336622"]
)
fig_alcohol.update_traces(textinfo='percent+label', textfont_size=15)
fig_alcohol.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="black")

fig_binge_drinking = go.Figure()
fig_binge_drinking.add_trace(go.Bar(
    x=["Male", "Female"],
    y=binge_drinking_male,
    name="Binge Drinking Rate",
    marker_color=["#005CAB", "#336622"]
))
fig_binge_drinking.update_layout(
    title="Binge Drinking by Gender",
    xaxis=dict(title="Gender"),
    yaxis=dict(title="Percentage"),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="black"
)
def home_layout():
    return html.Div([
        html.Nav([
            html.Div([
                html.H1("deAlcoholify", className="text-xl font-bold text-[#005CAB]")
            ], className="flex items-center space-x-2"),

            html.Div([
                dcc.Input(
                    type="text",
                    placeholder="Search...",
                    className="px-3 py-2 rounded-lg border border-gray-700 bg-white text-[#005CAB] focus:outline-none focus:ring-2 focus:ring-blue-500"
                )
            ], className="hidden md:block w-1/3"),

            html.Div([
                html.Button(
                    "Register for our newsletter", 
                    id="newsletter-button",  
                    className="text-white px-4 py-2 bg-blue-500 rounded-lg hover:bg-blue-600"
                ),
                dcc.Location(id="redirect-location", refresh=True) 
            ])
        ], className="flex items-center p-4 top-0 z-10 justify-between bg-white"),

        
        html.Div([
            html.Div([
                html.Div([
                    html.H2("Alcohol induced deaths (global)", className="font-semibold text-white text-sm"),
                    html.P("3 million", className="text-white text-xl font-bold"),
                    dcc.Link("View Study ➜", href="https://www.who.int/news/item/25-06-2024-over-3-million-annual-deaths-due-to-alcohol-and-drug-use-majority-among-men", className="text-white underline text-sm italic")
                ], className="bg-gradient-to-r from-[#005CAB] to-[#b7dcfc] p-6 rounded-lg shadow-md text-center"),
                
                html.Div([
                    html.H2("Alcohol Use in Lifetime (Rwanda)", className="font-semibold text-white text-sm"),
                    html.P("56.1%", className="text-white text-xl font-bold"),
                    dcc.Link("View Study ➜", href="https://www.rbc.gov.rw", className="text-white underline text-sm italic")
                ], className="bg-gradient-to-r from-[#005CAB] to-[#b7dcfc] p-6 rounded-lg shadow-md text-center"),
                
                html.Div([
                    html.H2("Binge Drinking in Males (Rwanda)", className="font-semibold text-white text-sm"),
                    html.P("13.7%", className="text-white text-xl font-bold"),
                    dcc.Link("View Study ➜", href="#", className="text-white underline text-sm italic")
                ], className="bg-gradient-to-r from-[#005CAB] to-[#b7dcfc] p-6 rounded-lg shadow-md text-center"),
                
                html.Div([
                    html.H2("Binge Drinking in Females (Rwanda)", className="font-semibold text-white text-sm"),
                    html.P("2.7%", className="text-white text-xl font-bold"),
                    dcc.Link("View Study ➜", href="#", className="text-white underline text-sm italic")
                ], className="bg-gradient-to-r from-[#005CAB] to-[#b7dcfc] p-6 rounded-lg shadow-md text-center"),
            ], className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2 mb-2 w-full"),
            
            html.Div([
                html.H2("Summary", className="text-[#005CAB] text-2xl font-semibold mb-4"),
                html.P(
                    "Recent studies in Rwanda highlight significant levels of substance abuse among adolescents. "
                    "In a sample of 3,301 respondents aged 13-24, over 56% reported having tried alcohol, and 13.7% of males "
                    "reported binge drinking in the last 30 days. Cannabis use is also prevalent, with a lifetime use rate of 9.3%. "
                    "These statistics underscore the importance of targeted interventions and public health education to address "
                    "substance abuse among Rwanda's youth.",
                    className="text-black"
                ),
            ], className=" p-6 rounded-lg shadow-md w-full mb-8"),
            
            html.Div([
                html.Div([
                    dcc.Graph(figure=fig_alcohol, config={'displayModeBar': False})
                ], className="w-full lg:w-1/2 p-4"),
                
                html.Div([
                    dcc.Graph(figure=fig_binge_drinking, config={'displayModeBar': False})
                ], className="w-full lg:w-1/2 p-4"),
            ], className="flex flex-col lg:flex-row w-full gap-4"),
            
            html.Div([
                html.H2("Alcohol effects on the body", className="text-[#005CAB] text-2xl font-semibold mb-4"),
                html.P(
                    "Alcohol is a depressant that affects the brain and central nervous system. It can impair judgment, coordination, and motor skills, "
                    "and in large quantities, it can lead to alcohol poisoning and death. Long-term alcohol use can also lead to liver disease, heart disease, "
                    "and an increased risk of certain cancers. It is important to drink responsibly and seek help if you or someone you know is struggling with alcohol use.",
                    className="text-black"
                ),
                html.Div([
                    html.H3("Alcohol and mental health", className="text-[#005CAB] text-lg font-semibold mb-4"),
                    html.P(
                        "Alcohol use can exacerbate mental health conditions such as depression and anxiety. It can also lead to memory loss, "
                        "cognitive impairment, and an increased risk to develop mental health disorders. Seeking help from a mental health professional "
                        "is essential if you are struggling with alcohol use and its effects on your mental health. If you or someone you know is in crisis, please contact a mental health hotline or emergency services immediately.",
                        className="text-black"
                    ),
                    create_dashboard_component()
                ], className="bg-white p-6 rounded-lg shadow-md w-full mb-8"),
                html.Div([
                    html.H3("Alcohol and social impact", className="text-white text-lg font-semibold mb-4"),
                    html.P(
                        "Alcohol use can have a significant impact on relationships, work, and social life. It can lead to conflict, violence, and legal problems, "
                        "and can also contribute to financial difficulties and job loss. It is important to be aware of the social impact of alcohol use and seek help if you are experiencing negative consequences as a result of your drinking.",
                        className="text-black"
                    ),
                    html.P("Below is a simple overview of how alcohol consumption affects relationships and facilitate violence", className="text-gray-400"),
                    gender_alcohol_stats()
                ], className="bg-white p-6 rounded-lg shadow-md w-full mb-8"),
            ], className=" bg-white min-h-screen pt-16"),
            
        ], className=" bg-white min-h-screen w-full px-4"), 
    ])

