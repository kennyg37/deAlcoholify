import os
from dash import html, dcc, Input, Output, State
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def subscribe_layout():
    """
    Layout for the subscribe component.
    """
    return html.Div(
        className="p-6 bg-gray-100 min-h-screen",
        children=[
            html.H1("Subscribe to Our Newsletter", className="text-4xl font-bold mb-6 text-center"),
            html.Div(
                className="bg-white rounded-lg shadow-lg w-full max-w-md mx-auto p-6 space-y-4",
                children=[
                    html.Label("Email", className="block text-gray-700 font-bold mb-2"),
                    dcc.Input(
                        id="email-input",
                        type="email",
                        placeholder="Enter your email",
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-4 leading-tight",
                    ),
                    html.Label("Topics", className="block text-gray-700 font-bold mb-2"),
                    dcc.Checklist(
                        id="topics-checklist",
                        options=[
                            {"label": "Alcohol Prevention", "value": "Prevention"},
                            {"label": "Mental Health", "value": "Mental"},
                            {"label": "Volunteering", "value": "Volunteering"},
                        ],
                        className="space-y-2",
                    ),
                    html.Button(
                        "Subscribe",
                        id="submit-btn",
                        className="bg-[#005CAB] hover:bg-blue-500 text-white font-bold py-2 px-4 rounded",
                    ),
                    html.Div(
                        id="status-message",
                        className="mt-4 text-center text-lg font-semibold",
                    ),
                ],
            )
        ],
    )

def register_subscribe_callbacks(app):
    """
    Register callbacks for the subscribe component.
    """
    @app.callback(
        Output("status-message", "children"),
        [Input("submit-btn", "n_clicks")],
        [State("email-input", "value"), State("topics-checklist", "value")],
    )
    def send_email(n_clicks, email, topics):
        if n_clicks and email:
            try:
                # Configure SendGrid
                sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
                message = Mail(
                    from_email="kalisaken8@gmail.com",
                    to_emails=email,
                    subject="Subscription Confirmation",
                    html_content=f"<p>Thank you for subscribing to {', '.join(topics)}!</p>",
                )
                sg.send(message)
                return "Subscription Successful!"
            except Exception as e:
                return "Error Sending Email"
        elif n_clicks:
            return "Please enter a valid email."
        return ""
