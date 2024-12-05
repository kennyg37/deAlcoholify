from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def AlcoholStatistics():
    # Define the style for the page
    page_style = {
        "backgroundColor": "#121212",  # Darker background for a modern feel
        "color": "#E0E0E0",  # Light text for contrast
        "padding": "20px",
        "boxSizing": "border-box",
    }

    # Define the cards for the statistics
    cards = [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("1.34B", className="card-title", style={"fontSize": "1.4rem", "fontWeight": "bold"}),  
                    html.P("Harmful Alcohol Use (2020)", className="card-subtitle", style={"fontSize": "1rem", "fontWeight": "500"}),  
                    html.P("Over a billion people engaged in harmful drinking.", className="card-text", style={"fontSize": "0.9rem"}),  
                ]
            ),
            style={"width": "22%", "margin": "10px", "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)", 
                   "borderRadius": "10px", "backgroundColor": "#2C2C2C"}
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("38%", className="card-title", style={"fontSize": "1.4rem", "fontWeight": "bold"}),  
                    html.P("Alcohol-Related Deaths", className="card-subtitle", style={"fontSize": "1rem", "fontWeight": "500"}),  
                    html.P("Nearly 40% of cirrhosis deaths.", className="card-text", style={"fontSize": "0.9rem"}),  
                ]
            ),
            style={"width": "22%", "margin": "10px", "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)", 
                   "borderRadius": "10px", "backgroundColor": "#2C2C2C"}
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("1.8M", className="card-title", style={"fontSize": "1.4rem", "fontWeight": "bold"}),  
                    html.P("Alcohol-Related Deaths (2021)", className="card-subtitle", style={"fontSize": "1rem", "fontWeight": "500"}),  
                    html.P("Millions die due to alcohol each year.", className="card-text", style={"fontSize": "0.9rem"}),  
                ]
            ),
            style={"width": "22%", "margin": "10px", "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)", 
                   "borderRadius": "10px", "backgroundColor": "#2C2C2C"}
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("77.6%", className="card-title", style={"fontSize": "1.4rem", "fontWeight": "bold"}),  
                    html.P("Male Alcohol Consumption", className="card-subtitle", style={"fontSize": "1rem", "fontWeight": "500"}),  
                    html.P("Higher alcohol consumption among men.", className="card-text", style={"fontSize": "0.9rem"}),  
                ]
            ),
            style={"width": "22%", "margin": "10px", "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)", 
                   "borderRadius": "10px", "backgroundColor": "#2C2C2C"}
        ),
    ]
    
    # Charts for visualizing the data
    gender_consumption_chart = dcc.Graph(
        figure=go.Figure(
            data=[  
                go.Bar(
                    x=["Male", "Female"],
                    y=[77.6, 22.4],
                    marker=dict(color=["#1E90FF", "#FF6347"]),
                    text=["77.6%", "22.4%"],
                    textposition="inside",
                )
            ],
            layout=go.Layout(
                title="Harmful Alcohol Consumption by Gender (2020)",
                xaxis=dict(title="Gender"),
                yaxis=dict(title="Percentage (%)"),
                paper_bgcolor="#121212",
                plot_bgcolor="#121212",
                font=dict(color="#E0E0E0"),
            )
        ),
        style={"width": "48%"}
    )

    deaths_attributable_chart = dcc.Graph(
        figure=go.Figure(
            data=[  
                go.Pie(
                    labels=["Deaths Attributable to Alcohol Use", "Other Deaths"],
                    values=[1.8, 58.2],
                    hole=0.4,
                    marker=dict(colors=["#FF6347", "#4CAF50"]),
                )
            ],
            layout=go.Layout(
                title="Deaths Attributable to High Alcohol Use (2021)",
                paper_bgcolor="#121212",
                plot_bgcolor="#121212",
                font=dict(color="#E0E0E0"),
            )
        ),
        style={"width": "48%"}
    )
    
    # Layout for displaying the cards and charts
    return html.Div(
        style=page_style,
        children=[
            html.H1(
                "Alcohol Use Statistics",
                className="text-center text-4xl font-bold my-4",
                style={"marginBottom": "20px"}
            ),
            html.P(
                "The following charts provide an overview of the harmful impact of alcohol use globally. The first chart highlights the disproportionate consumption of alcohol by gender, with males accounting for the majority of harmful drinking. The second chart illustrates the alarming number of deaths attributable to alcohol use, shedding light on its contribution to global mortality.",
                className="text-center text-lg",
                style={"padding": "0 10%", "marginBottom": "40px", "lineHeight": "1.6"}
            ),
            # Cards section
            html.Div(
                children=cards,
                style={
                    "display": "flex",
                    "justifyContent": "space-around",
                    "flexWrap": "wrap",
                    "marginBottom": "40px",
                }
            ),
            # Charts section
            html.Div(
                children=[gender_consumption_chart, deaths_attributable_chart],
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                    "flexWrap": "wrap",
                }
            ),
        ]
    )
