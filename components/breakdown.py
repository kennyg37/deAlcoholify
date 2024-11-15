from dash import html, dcc
import plotly.graph_objects as go
import plotly.express as px

def create_dashboard_component():
    conditions = ["Major Depressive Disorder (AUD)", "Major Depressive Disorder (Dependence)",
                  "Dysthymia (AUD)", "Dysthymia (Dependence)"]
    likelihoods = [2.3, 3.7, 1.7, 2.8]

    treatment_disorders = ["Major Depressive Disorder", "Dysthymia"]
    treatment_percentages = [33, 11]

    weeks = [0, 1, 2, 3, 4]
    depression_scores = [8.5, 7.2, 5.8, 4.1, 3.0] 

    genders = ["Women - Depression before AUD", "Men - AUD before Depression"]
    percentages = [65, 70]

    fig_co_occurrence = go.Figure()
    fig_co_occurrence.add_trace(go.Bar(
        x=conditions,
        y=likelihoods,
        name="Likelihood of Co-occurrence",
        marker_color=["#1f77b4", "#d62728", "#2ca02c", "#ff7f0e"]
    ))
    fig_co_occurrence.update_layout(
        title="Likelihood of Co-occurrence of Depression and AUD",
        xaxis=dict(title="Condition"),
        yaxis=dict(title="Likelihood (Times More Likely)"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    fig_treatment_population = px.pie(
        names=treatment_disorders,
        values=treatment_percentages,
        title="Depressive Disorders in AUD Treatment Population",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    fig_treatment_population.update_traces(textinfo='percent+label', textfont_size=15)
    fig_treatment_population.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")

    fig_abstinence = go.Figure()
    fig_abstinence.add_trace(go.Scatter(
        x=weeks,
        y=depression_scores,
        mode="lines+markers",
        line=dict(color="#d62728", width=2),
        name="Depression Score"
    ))
    fig_abstinence.update_layout(
        title="Improvement in Depression Symptoms After Abstinence",
        xaxis=dict(title="Weeks of Abstinence"),
        yaxis=dict(title="Depression Score"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    fig_gender = go.Figure(
        data=go.Heatmap(
            z=[[65, 70]],
            x=genders,
            y=["Likelihood (%)"],
            colorscale="Viridis"
        )
    )
    fig_gender.update_layout(
        title="Gender Differences in AUD and Depression Co-occurrence",
        xaxis=dict(title="Gender"),
        yaxis=dict(showticklabels=False),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    return html.Div(style={"backgroundColor": "#111", "color": "white"}, children=[
        html.H1("Alcohol Use Disorder and Depression Dashboard", style={"textAlign": "center"}),

        html.Div([
            dcc.Graph(figure=fig_co_occurrence)
        ], style={"marginBottom": "50px"}),

        html.Div([
            dcc.Graph(figure=fig_treatment_population)
        ], style={"marginBottom": "50px"}),

        html.Div([
            dcc.Graph(figure=fig_abstinence)
        ], style={"marginBottom": "50px"}),

        html.Div([
            dcc.Graph(figure=fig_gender)
        ])
    ])


def gender_alcohol_stats():
    alcohol_status = ["Often Drunk", "Sometimes Drunk", "Drinks but Never Drunk", "Does Not Drink"]
    violence_percentages = [75.7, 42.2, 21.9, 17.7]

    fig_violence_vs_drinking = go.Figure()
    fig_violence_vs_drinking.add_trace(go.Bar(
        x=alcohol_status,
        y=violence_percentages,
        name="Physical/Sexual Violence",
        marker_color=["#d62728", "#ff7f0e", "#1f77b4", "#2ca02c"]
    ))
    fig_violence_vs_drinking.update_layout(
        title="Physical/Sexual Violence vs. Partner's Alcohol Consumption",
        xaxis=dict(title="Partner's Alcohol Consumption"),
        yaxis=dict(title="Percentage (%)"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    alcohol_consumption_men = ["Wife Drinks Occasionally", "Wife Drinks Often", "Wife Does Not Drink"]
    self_reported_violence = [25.4, 42.8, 16.7] 
    
    fig_men_violence = go.Figure()
    fig_men_violence.add_trace(go.Bar(
        x=alcohol_consumption_men,
        y=self_reported_violence,
        name="Men's Self-Reported Violence",
        marker_color=["#1f77b4", "#d62728", "#2ca02c"]
    ))
    fig_men_violence.update_layout(
        title="Men's Self-Reported Violence vs. Wife's Alcohol Consumption",
        xaxis=dict(title="Wife/Partner's Alcohol Consumption"),
        yaxis=dict(title="Percentage (%)"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    return html.Div(style={"backgroundColor": "#111", "color": "white"}, children=[
        html.H2("Alcohol-Related Insights from Rwanda Demographic and Health Survey", style={"textAlign": "center"}),

        html.Div([
            dcc.Graph(figure=fig_violence_vs_drinking)
        ], style={"marginBottom": "50px"}),

        html.Div([
            dcc.Graph(figure=fig_men_violence)
        ])
    ])
