from dash import html, dcc
import plotly.express as px
import pandas as pd

def Article2():
    # Define the page background and text styles
    page_style = {
        "backgroundColor": "white",  # White background for a clean look
        "color": "black",  # Black text for contrast
        "padding": "20px",
        "boxSizing": "border-box",  # Ensure padding doesn't affect width
        "overflowX": "hidden",  # Prevent horizontal scrolling
    }

    # Common layout for transparent charts
    chart_layout = {
        "plot_bgcolor": "rgba(255, 255, 255, 0)",  # Transparent plot background
        "paper_bgcolor": "rgba(255, 255, 255, 0)",  # Transparent paper background
        "font": {"color": "black"},  # Black text for axes and labels
    }

    # African data for charts
    data_alcohol_harm_africa = pd.DataFrame({
        "Region": ["East Africa", "West Africa", "Southern Africa", "North Africa"],
        "Mortality Increase per Liter of Alcohol (%)": [1.1, 2.0, 3.4, 1.8]
    })

    data_alcohol_poverty_africa = pd.DataFrame({
        "Country/Group": ["Kenya (2005)", "Nigeria (2000)", "South Africa (2015)", "Tanzania (2008)"],
        "Income Spent on Alcohol (%)": [8, 6, 12, 14]
    })

    data_youth_alcohol_deaths_africa = pd.DataFrame({
        "Region": ["Sub-Saharan Africa", "North Africa"],
        "Youth Deaths Due to Alcohol (%)": [28, 18]
    })

    # Create charts with updated background and text colors
    charts = [
        dcc.Graph(
            figure=px.bar(
                data_alcohol_harm_africa,
                x="Region",
                y="Mortality Increase per Liter of Alcohol (%)",
                title="Alcohol Consumption and Mortality Increase in Africa"
            ).update_layout(chart_layout),
            style={"maxWidth": "100%", "height": "400px"}  # Responsive chart dimensions
        ),
        dcc.Graph(
            figure=px.bar(
                data_alcohol_poverty_africa,
                x="Country/Group",
                y="Income Spent on Alcohol (%)",
                title="Income Spent on Alcohol by African Countries"
            ).update_layout(chart_layout),
            style={"maxWidth": "100%", "height": "400px"}  # Responsive chart dimensions
        ),
        dcc.Graph(
            figure=px.bar(
                data_youth_alcohol_deaths_africa,
                x="Region",
                y="Youth Deaths Due to Alcohol (%)",
                title="Youth Deaths Attributed to Alcohol in Africa"
            ).update_layout(chart_layout),
            style={"maxWidth": "100%", "height": "400px"}  # Responsive chart dimensions
        )
    ]

    # Layout for charts in rows
    chart_rows = []
    for i in range(0, len(charts), 2):
        chart_rows.append(
            html.Div(
                children=charts[i:i + 2],  # Add up to two charts per row
                style={
                    "display": "flex", 
                    "justifyContent": "space-around", 
                    "flexWrap": "wrap", 
                    "marginBottom": "20px", 
                    "gap": "20px"
                }
            )
        )

    # Article introduction with African context
    article_title = "Why is Reducing Alcohol-Related Problems a Priority in Africa?"
    article_intro = (
        "Alcohol abuse is increasingly becoming a significant public health issue across Africa, contributing to "
        "various health complications, social problems, and economic disruption. The burden of alcohol-related harm "
        "is felt most acutely by youth, those living in poverty, and individuals suffering from alcohol-related diseases. "
        "This article explores the impact of alcohol on health, economic conditions, and youth mortality across different "
        "regions of Africa, highlighting the urgent need for stronger policies to tackle alcohol-related issues. "
        "Through better regulation, education, and intervention strategies, African countries can mitigate alcohol-related harms."
    )

    return html.Div(
        style=page_style,
        children=[
            # Article header
            html.Div(
                children=[
                    html.H1(
                        article_title,
                        style={
                            "textAlign": "center", 
                            "color": "#005CAB",  # Blue highlight
                            "marginBottom": "20px"
                        }
                    ),
                    html.P(
                        article_intro,
                        style={
                            "textAlign": "justify", 
                            "lineHeight": "1.6", 
                            "padding": "0 10%", 
                            "marginBottom": "40px"
                        }
                    )
                ]
            ),
            # Charts
            html.Div(
                children=chart_rows
            )
        ]
    )
