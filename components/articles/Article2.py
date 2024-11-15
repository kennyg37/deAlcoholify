from dash import html, dcc
import plotly.express as px
import pandas as pd

def Article2():
    # Define the page background and text styles
    page_style = {
        "backgroundColor": "#1A202C",  # Tailwind's bg-gray-900 equivalent
        "color": "white",  # White text
        "padding": "20px",
    }

    # Common layout for transparent charts
    chart_layout = {
        "plot_bgcolor": "rgba(0, 0, 0, 0)",  
        "paper_bgcolor": "rgba(0, 0, 0, 0)",  # Transparent paper background
        "font": {"color": "white"},  # White text for axes and labels
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

    # Create charts with transparent backgrounds
    charts = [
        dcc.Graph(
            figure=px.bar(
                data_alcohol_harm_africa,
                x="Region",
                y="Mortality Increase per Liter of Alcohol (%)",
                title="Alcohol Consumption and Mortality Increase in Africa"
            ).update_layout(chart_layout)
        ),
        dcc.Graph(
            figure=px.bar(
                data_alcohol_poverty_africa,
                x="Country/Group",
                y="Income Spent on Alcohol (%)",
                title="Income Spent on Alcohol by African Countries"
            ).update_layout(chart_layout)
        ),
        dcc.Graph(
            figure=px.bar(
                data_youth_alcohol_deaths_africa,
                x="Region",
                y="Youth Deaths Due to Alcohol (%)",
                title="Youth Deaths Attributed to Alcohol in Africa"
            ).update_layout(chart_layout)
        )
    ]

    # Layout for charts in rows
    chart_rows = []
    for i in range(0, len(charts), 2):
        chart_rows.append(
            html.Div(
                children=charts[i:i + 2],  # Add two charts per row
                style={"display": "flex", "justifyContent": "space-around", "marginBottom": "20px"}
            )
        )

    # Article introduction with African context
    article_title = "Why is reducing alcohol-related problems a priority in Africa?"
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
            html.Div(
                children=[
                    html.H1(
                        article_title,
                        className="text-center text-4xl font-bold my-4",
                        style={"marginBottom": "20px"}
                    ),
                    html.P(
                        article_intro,
                        className="text-lg",
                        style={"textAlign": "center", "padding": "0 10%", "marginBottom": "40px"}
                    )
                ]
            ),
            html.Div(
                children=chart_rows
            )
        ]
    )


