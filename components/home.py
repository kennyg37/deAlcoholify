from dash import html, dcc
import plotly.express as px
import plotly.graph_objs as go

# Sample data for charts
sample_bar_data = {
    'years': ['2010', '2012', '2013', '2016', '2019'],
    'values': [80, 90, 70, 150, 100]
}

sample_line_data = {
    'years': ['2010', '2012', '2013', '2016', '2019'],
    'values': [100, 150, 130, 170, 190]
}

# Bar chart
bar_chart = px.bar(x=sample_bar_data['years'], y=sample_bar_data['values'], labels={'x': 'Year', 'y': 'Value'})

# Gauge chart
gauge_chart = go.Figure(go.Indicator(
    mode="gauge+number",
    value=45,
    title={'text': "Stock"},
    gauge={'axis': {'range': [0, 100]}}
))

# Line chart
line_chart = px.line(x=sample_line_data['years'], y=sample_line_data['values'], labels={'x': 'Year', 'y': 'Revenue'})

def home_layout():
    return html.Div([
        # Top Row Cards
        html.Div([
            html.Div([
                html.H2("Global Annual alcohol-related deaths", className="text-lg font-semibold"),
                html.P("~ 3,000,000", className="text-3xl font-bold"),
                dcc.Link("View data ➜", href="https://www.who.int/news/item/25-06-2024-over-3-million-annual-deaths-due-to-alcohol-and-drug-use-majority-among-men", className="text-blue-500 underline")
            ], className="bg-white p-4 rounded shadow text-center"),
            
            html.Div([
                html.H2("Revenue", className="text-lg font-semibold"),
                html.P("$7564", className="text-3xl font-bold"),
                dcc.Link("View data ➜", href="#", className="text-blue-500 underline")
            ], className="bg-white p-4 rounded shadow text-center"),
            
            html.Div([
                html.H2("Orders", className="text-lg font-semibold"),
                html.P("7891+", className="text-3xl font-bold"),
                dcc.Link("View data ➜", href="#", className="text-blue-500 underline")
            ], className="bg-white p-4 rounded shadow text-center"),
            
            html.Div([
                html.H2("Items", className="text-lg font-semibold"),
                html.P("486", className="text-3xl font-bold"),
                dcc.Link("View data ➜", href="#", className="text-blue-500 underline")
            ], className="bg-white p-4 rounded shadow text-center"),
            
        ], className="grid grid-cols-4 gap-4 mb-8"),
        
        # Bottom Row with Charts
        html.Div([
            # Statistics Bar Chart
            html.Div([
                html.H2("Statistics", className="text-lg font-semibold mb-2"),
                dcc.Graph(figure=bar_chart)
            ], className="bg-white p-4 rounded shadow"),
            
            # Stock Gauge Chart
            html.Div([
                html.H2("Stock", className="text-lg font-semibold mb-2"),
                dcc.Graph(figure=gauge_chart),
                html.P("Target: $7.8k | Last week: $1.4k", className="text-sm text-gray-500 text-center mt-2")
            ], className="bg-white p-4 rounded shadow"),
            
            # Total Revenue Line Chart
            html.Div([
                html.H2("Total Revenue", className="text-lg font-semibold mb-2"),
                dcc.Graph(figure=line_chart),
                html.P("$7841.12 Total Revenue | 17 Open Campaigns", className="text-sm text-gray-500 text-center mt-2")
            ], className="bg-white p-4 rounded shadow"),
            
        ], className="grid grid-cols-3 gap-4")
        
    ], className="min-h-screen p-5")
