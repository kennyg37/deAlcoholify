from dash import html, dcc

def about_layout():
    team_members = [
        {"name": "Ken Ganza", "role": "Full-stack Engineer/ALU", "image": "/assets/ken.jpeg"},
        {"name": "Kwihangana Dimitri", "role": "Machine Learning Engineer/ALU", "image": "/assets/dimitri.jpeg"},
        {"name": "Kwizera Alain Bertrand", "role": "Data Analyst/AUCA", "image": "/assets/bertrand.jpeg"}
    ]
    return html.Div([
        html.Div([
            html.H1("About Us", className="text-4xl font-bold text-white mb-4"),
            html.P(
                "We are a passionate team of engineers and analysts committed to harnessing the power of data and technology "
                "to fight the global challenge of alcohol abuse. Our goal is to inspire better decision-making through data-driven insights.",
                className="text-gray-400 mb-8"
            ),
        ], className="text-center bg-gray-900 p-8 shadow-md rounded-lg"),
        
        html.Div([
            html.H2("Meet Our Team", className="text-2xl font-bold text-white mb-6 text-center"),
            html.Div([
                html.Div([
                    html.Img(src=member['image'], alt=member['name'], className="rounded w-24 h-24 mb-4"),
                    html.H3(member['name'], className="text-white text-xl font-semibold"),
                    html.P(member['role'], className="text-gray-400"),
                ], className="text-center bg-gray-800 p-4 rounded shadow-lg")
                for member in team_members
            ], className="grid grid-cols-1 md:grid-cols-3 gap-8"),
        ], className="max-w-screen-lg mx-auto my-8"),
        
        html.Div([
            html.H2("Our Mission", className="text-2xl font-bold text-white mb-4"),
            html.P(
                "Our mission is to empower individuals with knowledge about the risks of alcohol consumption through "
                "interactive visualizations, statistical insights, and compelling data narratives. We believe informed "
                "choices can lead to healthier lives and stronger communities.",
                className="text-gray-400"
            ),
            html.H2("How Our App Works", className="text-2xl font-bold text-white mt-8 mb-4"),
            html.P(
                "The app serves as an educational tool, leveraging powerful visualizations to present key statistics on "
                "alcohol use and its social consequences. Users can explore detailed reports, track trends, and gain valuable "
                "insights to make informed decisions and contribute to raising awareness about alcohol-related risks.",
                className="text-gray-400"
            ),
        ], className="bg-gray-900 p-6 rounded-lg shadow-md max-w-screen-lg mx-auto mb-8"),
    ], className="p-4 bg-gray-900 min-h-screen")
