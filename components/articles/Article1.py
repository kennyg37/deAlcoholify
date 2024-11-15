from dash import html, dcc
import plotly.express as px
import pandas as pd

def Article1():
    # Define the page background and text styles
    page_style = {
        "backgroundColor": "#1A202C",  # Tailwind's bg-gray-900 equivalent
        "color": "white",  # White text
        "padding": "20px",
    }

    # Common layout for transparent charts
    chart_layout = {
        "plot_bgcolor": "rgba(0, 0, 0, 0)",  # Transparent plot background
        "paper_bgcolor": "rgba(0, 0, 0, 0)",  # Transparent paper background
        "font": {"color": "white"}  # White text for axes and labels
    }

    # Data for each pattern
    data_patterns = {
        "Spouse's Alcohol Consumption and Violence": pd.DataFrame({
            "Spouse's Drinking Frequency": ["Often Drunk", "Does Not Drink"],
            "Women Experiencing Violence (%)": [85, 26],
            "Men Experiencing Violence (%)": [44, 13]
        }),
        "Husband's Education Level and Violence": pd.DataFrame({
            "Husband's Education Level": ["No Education", "More Than Secondary Education"],
            "Women Experiencing Violence (%)": [50, 13]
        }),
        "Parental Violence and Spousal Violence": pd.DataFrame({
            "Father Beat Mother": ["Yes", "No"],
            "Women Experiencing Violence (%)": [54, 39],
            "Men Experiencing Violence (%)": [22, 15]
        }),
        "Fear of Spouse and Violence (Women)": pd.DataFrame({
            "Fear of Husband": ["Most of the Time", "Never"],
            "Women Experiencing Violence (%)": [95, 30]
        }),
        "Fear of Spouse and Violence (Men)": pd.DataFrame({
            "Fear of Wife": ["Sometimes", "Never"],
            "Men Experiencing Violence (%)": [41, 15]
        })
    }

    # Create charts with transparent backgrounds
    charts = [
        dcc.Graph(
            figure=px.bar(
                data_patterns["Spouse's Alcohol Consumption and Violence"], 
                x="Spouse's Drinking Frequency", 
                y=["Women Experiencing Violence (%)", "Men Experiencing Violence (%)"],
                title="Alcohol Consumption and Violence Risk"
            ).update_layout(chart_layout)
        ),
        dcc.Graph(
            figure=px.bar(
                data_patterns["Husband's Education Level and Violence"], 
                x="Husband's Education Level", 
                y="Women Experiencing Violence (%)",
                title="Education Level and Violence Risk (Women)"
            ).update_layout(chart_layout)
        ),
        dcc.Graph(
            figure=px.bar(
                data_patterns["Parental Violence and Spousal Violence"], 
                x="Father Beat Mother", 
                y=["Women Experiencing Violence (%)", "Men Experiencing Violence (%)"],
                title="Parental Violence and Spousal Abuse Risk"
            ).update_layout(chart_layout)
        ),
        dcc.Graph(
            figure=px.bar(
                data_patterns["Fear of Spouse and Violence (Women)"], 
                x="Fear of Husband", 
                y="Women Experiencing Violence (%)",
                title="Fear of Husband and Violence Risk (Women)"
            ).update_layout(chart_layout)
        ),
        dcc.Graph(
            figure=px.bar(
                data_patterns["Fear of Spouse and Violence (Men)"], 
                x="Fear of Wife", 
                y="Men Experiencing Violence (%)",
                title="Fear of Wife and Violence Risk (Men)"
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

    return html.Div(
        style=page_style,
        children=[
            html.Div(
                children=[
                    html.H2(
                        "Alcohol and Gender-Based Violence: Key Findings",
                        className="text-center text-3xl font-bold my-4",
                        style={"marginBottom": "20px"}
                    ),
                    html.P(
                        """
                        Alcohol consumption, particularly frequent drinking, is strongly linked to increased rates of violence. 
                        Women with alcoholic partners face higher risks of physical and emotional abuse. Other factors such as 
                        education levels and past family violence also play significant roles in exacerbating the likelihood of 
                        violence. This analysis underscores the need to address alcohol-related violence as a critical public 
                        health issue.
                        """,
                        className="text-lg",
                        style={"textAlign": "center", "padding": "0 10%"}
                    )
                ],
                style={"marginBottom": "40px"}
            ),
            html.H2(
                "Patterns by Spouse’s Characteristics and Violence Risk",
                className="text-center text-2xl font-bold my-4",
                style={"marginBottom": "20px"}
            ),
            html.Div(
                children=chart_rows
            )
        ]
    )
