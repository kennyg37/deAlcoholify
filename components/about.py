from dash import html, dcc

def about_layout():
    # Team members data
    team_members = [
        {"name": "Ken Ganza", "role": "Full-stack Engineer | ALU", "image": "/assets/ken.jpeg"},
        {"name": "Kwihangana Dimitri", "role": "Machine Learning Engineer | ALU", "image": "/assets/dimitri.jpeg"},
        {"name": "Kwizera Alain Bertrand", "role": "Data Analyst | AUCA", "image": "/assets/bertrand.jpeg"}
    ]
    
    return html.Div([
        
        html.Div([
            html.H1("About Us", className="text-4xl font-bold text-[#005CAB] mb-6"),
            html.P(
                "We are a passionate team of engineers and analysts committed to harnessing the power of data and technology "
                "to address the global challenge of alcohol abuse. Through data-driven insights, we aim to inspire informed decision-making "
                "and promote healthier communities.",
                className="text-black text-lg leading-relaxed mb-8"
            ),
        ], className="text-center bg-white p-8 shadow-lg rounded-lg"),
        
        # Meet Our Team Section
        html.Div([
            html.H2("Meet Our Team", className="text-3xl font-bold text-white mb-6 text-center"),
            html.Div([
                html.Div([
                    html.Img(src=member['image'], alt=member['name'], className="rounded-full w-32 h-32 mb-4 mx-auto"),
                    html.H3(member['name'], className="text-black text-xl font-semibold mb-2"),
                    html.P(member['role'], className="text-gray-900 text-sm"),
                ], className="text-center bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transition duration-300")
                for member in team_members
            ], className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8"),
        ], className="max-w-screen-lg mx-auto my-12"),
        
        # Mission and App Explanation Section
        html.Div([
            html.H2("Our Mission", className="text-3xl font-bold text-[#005CAB] mb-6"),
            html.P(
                "Our mission is to empower individuals with knowledge about the risks of alcohol consumption. "
                "We deliver interactive visualizations, statistical insights, and compelling narratives to help users make informed choices, "
                "leading to healthier lives and stronger communities.",
                className="text-black text-lg leading-relaxed mb-8"
            ),
            html.H2("How Our App Works", className="text-3xl font-bold text-[#005CAB] mb-6"),
            html.P(
                "Our app acts as an educational tool, leveraging engaging visualizations to showcase critical statistics on alcohol use and its social consequences. "
                "Users can explore detailed reports, track trends, and gain actionable insights to raise awareness about alcohol-related risks and make better decisions.",
                className="text-black text-lg leading-relaxed"
            ),
        ], className="bg-white p-8 rounded-lg shadow-lg max-w-screen-lg mx-auto my-12"),
    ], className="bg-white min-h-screen p-6")
