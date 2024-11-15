from dash import html, dcc

def about_layout():
    team_members = [
        {"name": "Ken Ganza", "role": "Backend engineer", "image": "/assets/ken.jpg"},
        {"name": "Kwihangana Dimitri", "role": "Frontend engineer", "image": "/assets/alice.jpg"},
        {"name": "Kwizera Alain Bertrand", "role": "Data scientist", "image": "/assets/john.jpg"}
    ]
    return html.Div([
        html.Div([
            html.H1("About Us", className="text-4xl font-bold text-white mb-4"),
            html.P(
                "We are a dedicated team of professionals aiming to educate people about the risks of alcohol abuse "
                "through data visualization and analysis.",
                className="text-gray-400 mb-8"
            ),
        ], className="text-center bg-gray-900 p-8 shadow-md rounded-lg"),
        
        html.Div([
            html.H2("Meet Our Team", className="text-2xl font-bold text-white mb-6 text-center"),
            html.Div([
                html.Div([
                    html.Img(src=member['image'], alt=member['name'], className="rounded-full w-24 h-24 mb-4"),
                    html.H3(member['name'], className="text-white text-xl font-semibold"),
                    html.P(member['role'], className="text-gray-400"),
                ], className="text-center bg-gray-800 p-4 rounded shadow-lg")
                for member in team_members
            ], className="grid grid-cols-1 md:grid-cols-3 gap-8"),
        ], className="max-w-screen-lg mx-auto my-8"),
        
        html.Div([
            html.H2("Our Mission", className="text-2xl font-bold text-white mb-4"),
            html.P(
                "Our mission is to raise awareness and educate individuals about the impact of alcohol consumption, "
                "using data-driven insights to inspire healthier choices.",
                className="text-gray-400"
            ),
            html.H2("Use Case", className="text-2xl font-bold text-white mt-8 mb-4"),
            html.P(
                "The app is designed to be an educational tool, providing statistics and visualizations that highlight "
                "the consequences of alcohol use and promote informed decision-making.",
                className="text-gray-400"
            ),
        ], className="bg-gray-900 p-6 rounded-lg shadow-md max-w-screen-lg mx-auto mb-8"),
    ], className="p-4 bg-gray-900 min-h-screen")
