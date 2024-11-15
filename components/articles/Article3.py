from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd

def Article3():
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

    # Data for visualizations
    data_death = {
        'categories': ['Global Deaths (2.6 million)', 'Deaths Among Men (Disproportionate)'],
        'values': [2.6, 2.1]  # Example values (adjust based on actual data)
    }

    data_disorder = {
        'categories': ['People Affected by Alcohol Use Disorders (400 million)', 'Untreated Population'],
        'values': [400, 350]  # Example values (adjust based on actual data)
    }

    data_death_reduction = {
        'categories': ['Deaths Decreased (20.2%)', 'Deaths Still Occurring'],
        'values': [20.2, 79.8]  # Example values (adjust based on actual data)
    }

    # Create charts with transparent backgrounds
    death_chart = go.Figure(
        data=[go.Bar(x=data_death['categories'], y=data_death['values'], marker=dict(color='#FF6347'))],
        layout=go.Layout(title="Alcohol-Related Deaths", xaxis=dict(title="Category"), yaxis=dict(title="Millions"))
    ).update_layout(chart_layout)

    disorder_chart = go.Figure(
        data=[go.Pie(labels=data_disorder['categories'], values=data_disorder['values'], hole=0.3)],
        layout=go.Layout(title="Alcohol Use Disorder Prevalence")
    ).update_layout(chart_layout)

    death_reduction_chart = go.Figure(
        data=[go.Pie(labels=data_death_reduction['categories'], values=data_death_reduction['values'], hole=0.3)],
        layout=go.Layout(title="Reduction in Alcohol-Related Deaths (2010–2019)")
    ).update_layout(chart_layout)

    # Layout for charts in rows
    chart_rows = [
        html.Div(
            children=[
                dcc.Graph(figure=death_chart),
                dcc.Graph(figure=disorder_chart),
            ],
            style={"display": "flex", "justifyContent": "space-around", "marginBottom": "20px"}
        ),
        html.Div(
            children=[
                dcc.Graph(figure=death_reduction_chart),
            ],
            style={"display": "flex", "justifyContent": "center", "marginBottom": "20px"}
        )
    ]

    # Article introduction
    article_title = "Global Impact of Alcohol Consumption"
    article_intro = (
        "Alcohol abuse is a major global health and social issue, responsible for a significant burden of "
        "disease, death, and economic disruption worldwide. This article highlights the impact of alcohol on global health, "
        "including alcohol-related deaths, prevalence of alcohol use disorders, and efforts to reduce alcohol-related mortality."
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


