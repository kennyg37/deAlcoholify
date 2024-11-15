from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def AlcoholStatistics():
    # Define the style for the page
    page_style = {
        "backgroundColor": "#1A202C",  # Dark background
        "color": "white",  # White text
        "padding": "20px",
    }

    # Define the cards for the statistics with 3D effect, dark blue shadow, and padding
    cards = [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("1.34B", className="card-title", style={"fontSize": "1.2rem", "fontWeight": "bold"}),  # Reduced font size
                    html.H5("Harmful Alcohol Use (2020)", className="card-subtitle", style={"fontSize": "1rem","fontWeight": "bold"}),  # Reduced font size
                    html.P("Over a billion engaged in harmful drinking.", className="card-text", style={"fontSize": "0.9rem"}),  # Reduced font size
                ],
                style={"padding": "15px"}  # Reduced padding
            ),
            style={"width": "18rem", "margin": "5px", "boxShadow": "0 8px 16px rgba(0, 0, 139, 0.5)", "borderRadius": "10px", "backgroundColor": "#2D3748", "height": "150px"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("38%", className="card-title", style={"fontSize": "1.2rem", "fontWeight": "bold"}),  # Reduced font size
                    html.H5("Alcohol-related Deaths", className="card-subtitle", style={"fontSize": "1rem"}),  # Reduced font size
                    html.P("Nearly 40% of cirrhosis deaths.", className="card-text", style={"fontSize": "0.9rem"}),  # Reduced font size
                ],
                style={"padding": "15px"}  # Reduced padding
            ),
            style={"width": "18rem", "margin": "5px", "boxShadow": "0 8px 16px rgba(0, 0, 139, 0.5)", "borderRadius": "10px", "backgroundColor": "#2D3748", "height": "150px"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("1.8M", className="card-title", style={"fontSize": "1.8rem", "fontWeight": "bold"}),  # Reduced font size
                    html.H5("Alcohol-related Deaths (2021)", className="card-subtitle", style={"fontSize": "1rem"}),  # Reduced font size
                    html.P("Millions die due to alcohol each year.", className="card-text", style={"fontSize": "0.9rem"}),  # Reduced font size
                ],
                style={"padding": "15px"}  # Reduced padding
            ),
            style={"width": "18rem", "margin": "5px", "boxShadow": "0 8px 16px rgba(0, 0, 139, 0.5)", "borderRadius": "10px", "backgroundColor": "#2D3748", "height": "150px"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("77.6%", className="card-title", style={"fontSize": "1.8rem", "fontWeight": "bold"}),  # Reduced font size
                    html.H5("Male Alcohol Consumption", className="card-subtitle", style={"fontSize": "1rem"}),  # Reduced font size
                    html.P("Higher alcohol consumption among men.", className="card-text", style={"fontSize": "0.9rem"}),  # Reduced font size
                ],
                style={"padding": "15px"}  # Reduced padding
            ),
            style={"width": "18rem", "margin": "5px", "boxShadow": "0 8px 16px rgba(0, 0, 139, 0.5)", "borderRadius": "10px", "backgroundColor": "#2D3748", "height": "150px"},
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
                paper_bgcolor="#1A202C",
                plot_bgcolor="#1A202C",
                font=dict(color="white"),
            )
        )
    )

    deaths_attributable_chart = dcc.Graph(
        figure=go.Figure(
            data=[  
                go.Pie(
                    labels=["Deaths Attributable to Alcohol Use", "Other Deaths"],
                    values=[1.8, 58.2],  # 1.8 million out of 60 million total deaths
                    hole=0.4,
                    marker=dict(colors=["#FF6347", "#4CAF50"]),
                )
            ],
            layout=go.Layout(
                title="Deaths Attributable to High Alcohol Use (2021)",
                paper_bgcolor="#1A202C",
                plot_bgcolor="#1A202C",
                font=dict(color="white"),
            )
        )
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
                style={"padding": "0 10%", "marginBottom": "40px"}
            ),
            # Display the cards and charts
            html.Div(
                children=cards,
                style={
                    "display": "flex",
                    "justifyContent": "space-around",
                    "flexWrap": "wrap",
                    "marginBottom": "40px",
                }
            ),
            html.Div(
                children=[gender_consumption_chart, deaths_attributable_chart],
                style={
                    "display": "flex",
                    
                }
            ),
        ]
    )
