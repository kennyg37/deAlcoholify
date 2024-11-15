from dash import html

def create_model_card(title, description, link, link_text):
    """Reusable component for creating a styled model card."""
    return html.Div([
        html.H2(title, className="text-lg font-semibold text-white mb-2"),
        html.P(description, className="text-gray-400 mb-4"),
        html.A(link_text, href=link, className="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600")
    ], className="bg-gray-800 p-6 rounded shadow-lg")

def models_layout():
    """Layout for the Models page."""
    return html.Div([
        # Header Section
        html.Div([
            html.H1("Models", className="text-4xl font-bold text-white mb-4"),
            html.P(
                "Explore various predictive models to analyze data and gain insights about the impact of alcohol consumption.",
                className="text-gray-400 mb-8"
            ),
        ], className="text-center bg-gray-900 p-8 shadow-md rounded-lg mb-8"),
        
        # Model Cards Section
        html.Div([
            html.H2("Choose a Model", className="text-2xl font-bold text-white mb-6 text-center"),
            html.Div([
                create_model_card(
                    title="Cancer Model",
                    description="This model predicts the likelihood of a person having cancer based on alcohol consumption patterns.",
                    link="/models/cancer",
                    link_text="Explore Cancer Model"
                ),
                create_model_card(
                    title="Liver Disease Model",
                    description="This model estimates the risk of liver disease linked to alcohol consumption behavior.",
                    link="/models/liver",
                    link_text="Explore Liver Disease Model"
                ),
                create_model_card(
                    title="Mental Health Impact Model",
                    description="This model analyzes the impact of alcohol on mental health, including depression and anxiety.",
                    link="/models/mental-health",
                    link_text="Explore Mental Health Model"
                ),
            ], className="grid grid-cols-1 md:grid-cols-3 gap-8"),
        ], className="max-w-screen-lg mx-auto mb-8"),
    ], className="p-4 bg-gray-900 min-h-screen")
