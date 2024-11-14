from dash import html, dcc
import plotly.express as px
import plotly.graph_objs as go

from components.chatbot import chatbot_button, create_chatbot

# Data for graphs
alcohol_use = [56.1, 43.9]  # % who have tried alcohol vs. abstinent
binge_drinking_male = [13.7, 2.7]  # Male vs. Female binge drinking rates

# Pie Chart for Alcohol Use
fig_alcohol = px.pie(
    names=["Have Tried Alcohol", "Abstinent"],
    values=alcohol_use,
    title="Lifetime Alcohol Use among Adolescents",
    color_discrete_sequence=["#1f77b4", "#d62728"]
)
fig_alcohol.update_traces(textinfo='percent+label', textfont_size=15)
fig_alcohol.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")

# Bar Chart for Binge Drinking Rates
fig_binge_drinking = go.Figure()
fig_binge_drinking.add_trace(go.Bar(
    x=["Male", "Female"],
    y=binge_drinking_male,
    name="Binge Drinking Rate",
    marker_color=['#1f77b4', '#d62728']
))
fig_binge_drinking.update_layout(
    title="Binge Drinking by Gender",
    xaxis=dict(title="Gender"),
    yaxis=dict(title="Percentage"),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

def home_layout():
    return html.Div([
        html.Nav([
            html.Div([
                html.H1("deAlcoholify", className="text-xl font-bold text-white")
            ], className="flex items-center space-x-2"),

            html.Div([
                dcc.Input(
                    type="text",
                    placeholder="Search...",
                    className="px-3 py-2 rounded-lg border border-gray-700 bg-gray-900 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                )
            ], className="hidden md:block w-1/3"),

            html.Div([
                html.Button("Register for our newsletter", className="text-white px-4 py-2 bg-blue-500 rounded-lg hover:bg-blue-600"),
            ])
        ], className="flex items-center p-4 top-0 z-10 justify-between bg-gray-900"),
        
        html.Div([
            html.Div([
                html.Div([
                    html.H2("Alcohol induced deaths(global)", className="font-semibold text-white text-sm"),
                    html.P("3 million", className="text-gray-400"),
                    dcc.Link("View Study ➜", href="https://www.who.int/news/item/25-06-2024-over-3-million-annual-deaths-due-to-alcohol-and-drug-use-majority-am", className="text-blue-400 underline text-sm italic")
                ], className="bg-gray-800 p-4 rounded shadow text-center"),
                html.Div([
                    html.H2("Alcohol Use in Lifetime (Rwanda)", className="font-semibold text-white text-sm"),
                    html.P("56.1%", className="text-gray-400"),
                    dcc.Link("View Study ➜", href="https://www.who.int/news/item/25-06-2024-over-3-million-annual-deaths-due-to-alcohol-and-drug-use-majority-among-men", className="text-blue-400 underline text-sm italic")
                ], className="bg-gray-800 p-4 rounded shadow text-center"),
                
                html.Div([
                    html.H2("Binge Drinking in Males (Rwanda)", className="font-semibold text-white text-sm"),
                    html.P("13.7%", className="text-gray-400"),
                    dcc.Link("View Study ➜", href="#", className="text-blue-400 underline")
                ], className="bg-gray-800 p-4 rounded shadow text-center"),
                
                html.Div([
                    html.H2("Binge Drinking in Females (Rwanda)", className="font-semibold text-white text-sm"),
                    html.P("2.7%", className="text-gray-400"),
                    dcc.Link("View Study ➜", href="#", className="text-blue-400 underline")
                ], className="bg-gray-800 p-4 rounded shadow text-center"),
                
                
            ], className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8 max-w-screen-lg mx-auto"),
            
            html.Div([
                html.H2("Summary", className="text-white text-2xl font-semibold mb-4"),
                html.P(
                    "Recent studies in Rwanda highlight significant levels of substance abuse among adolescents. "
                    "In a sample of 3,301 respondents aged 13-24, over 56% reported having tried alcohol, and 13.7% of males "
                    "reported binge drinking in the last 30 days. Cannabis use is also prevalent, with a lifetime use rate of 9.3%. "
                    "These statistics underscore the importance of targeted interventions and public health education to address "
                    "substance abuse among Rwanda's youth.",
                    className="text-gray-400"
                ),
            ], className="bg-gray-900 p-6 rounded-lg shadow-md max-w-screen-lg mx-auto mb-8"),
            
            html.Div([
                html.Div([
                    dcc.Graph(figure=fig_alcohol, config={'displayModeBar': False})
                ], className="w-full lg:w-1/2 p-4"),
                
                html.Div([
                    dcc.Graph(figure=fig_binge_drinking, config={'displayModeBar': False})
                ], className="w-full lg:w-1/2 p-4"),
                
            ], className="flex flex-col lg:flex-row max-w-screen-lg mx-auto gap-4"),
            
        ], className="p-4 bg-gray-900 min-h-screen pt-16"), 
    ])
