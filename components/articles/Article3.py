from dash import html, dcc
import plotly.graph_objs as go

def Article3():
    # Define the page background and text styles
    page_style = {
        "backgroundColor": "white",  # Clean white background
        "color": "black",  # Black text for better readability
        "padding": "20px",
        "boxSizing": "border-box",
    }

    # Common layout for charts
    chart_layout = {
        "plot_bgcolor": "rgba(255, 255, 255, 0)",  # Transparent plot background
        "paper_bgcolor": "rgba(255, 255, 255, 0)",  # Transparent paper background
        "font": {"color": "black"},  # Black text for axes and labels
    }

    # Data for visualizations
    data_death = {
        'categories': ['Global Deaths (2.6M)', 'Deaths Among Men (2.1M)'],
        'values': [2.6, 2.1]
    }

    data_disorder = {
        'categories': ['People with Alcohol Use Disorders (400M)', 'Untreated Cases (350M)'],
        'values': [400, 350]
    }

    data_death_reduction = {
        'categories': ['Deaths Reduced (20.2%)', 'Remaining Deaths (79.8%)'],
        'values': [20.2, 79.8]
    }

    # Create charts with updated layouts
    death_chart = go.Figure(
        data=[go.Bar(
            x=data_death['categories'],
            y=data_death['values'],
            marker=dict(color='#FF6347'),
            text=[f"{v}M" for v in data_death['values']],
            textposition='auto'
        )],
        layout=go.Layout(
            title="Alcohol-Related Deaths",
            xaxis=dict(title="Category"),
            yaxis=dict(title="Millions")
        )
    ).update_layout(chart_layout)

    disorder_chart = go.Figure(
        data=[go.Pie(
            labels=data_disorder['categories'],
            values=data_disorder['values'],
            hole=0.3,
            marker=dict(colors=['#4682B4', '#87CEEB'])
        )],
        layout=go.Layout(title="Alcohol Use Disorder Prevalence")
    ).update_layout(chart_layout)

    death_reduction_chart = go.Figure(
        data=[go.Pie(
            labels=data_death_reduction['categories'],
            values=data_death_reduction['values'],
            hole=0.3,
            marker=dict(colors=['#32CD32', '#FF4500'])
        )],
        layout=go.Layout(title="Reduction in Alcohol-Related Deaths (2010–2019)")
    ).update_layout(chart_layout)

    # Layout for charts
    chart_rows = [
        html.Div(
            children=[
                dcc.Graph(figure=death_chart, style={"width": "48%"}),
                dcc.Graph(figure=disorder_chart, style={"width": "48%"}),
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "marginBottom": "20px",
                "flexWrap": "wrap",
                "gap": "20px"
            }
        ),
        html.Div(
            children=[
                dcc.Graph(figure=death_reduction_chart, style={"width": "50%"})
            ],
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "20px"
            }
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
            # Article header
            html.Div(
                children=[
                    html.H1(
                        article_title,
                        style={
                            "textAlign": "center",
                            "color": "#333333",
                            "marginBottom": "20px",
                            "fontSize": "2rem",
                        }
                    ),
                    html.P(
                        article_intro,
                        style={
                            "textAlign": "justify",
                            "lineHeight": "1.6",
                            "padding": "0 10%",
                            "marginBottom": "40px",
                            "fontSize": "1rem"
                        }
                    )
                ]
            ),
            # Charts
            html.Div(children=chart_rows)
        ]
    )
