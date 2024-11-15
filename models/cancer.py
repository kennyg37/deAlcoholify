from dash import html, dcc, Input, Output, callback, State
from joblib import load
import numpy as np

try:
    model = load("models/cancer_model.joblib")
except FileNotFoundError:
    model = None

def cancer_model():
    return html.Div([
        html.Div([
            html.H1("Cancer Prediction Model", className="text-2xl font-bold text-white mb-2"),
            html.P(
                "Provide the following information to assess your likelihood of having cancer. "
                "This model is for educational purposes only and should not replace medical advice.",
                className="text-gray-400 mb-6"
            ),
        ], className="text-center bg-gray-900 p-6 rounded shadow-md mb-6"),
        
        # Form inputs
        html.Div([
            html.Div([
                html.Div([
                    html.Label("Age", className="text-gray-700"),
                    dcc.Input(type="number", id="age", placeholder="Enter your age", className="w-full p-2 border rounded"),
                ], className="mb-4"),

                html.Div([
                    html.Label("Gender", className="text-gray-700"),
                    dcc.Dropdown(
                        id="gender",
                        options=[
                            {"label": "Male", "value": 0},
                            {"label": "Female", "value": 1}
                        ],
                        placeholder="Select your gender",
                        className="w-full"
                    ),
                ], className="mb-4"),
            ], className="w-1/2 p-2"),

            html.Div([
                html.Div([
                    html.Label("BMI", className="text-gray-700"),
                    dcc.Input(type="number", id="bmi", placeholder="Enter your BMI", className="w-full p-2 border rounded"),
                ], className="mb-4"),

                html.Div([
                    html.Label("Smoking", className="text-gray-700"),
                    dcc.Dropdown(
                        id="smoking",
                        options=[
                            {"label": "No", "value": 0},
                            {"label": "Yes", "value": 1}
                        ],
                        placeholder="Do you smoke?",
                        className="w-full"
                    ),
                ], className="mb-4"),
            ], className="w-1/2 p-2"),
        ], className="flex flex-wrap mb-4"),
        
        html.Div([
            html.Div([
                html.Div([
                    html.Label("Genetic Risk", className="text-gray-700"),
                    dcc.Dropdown(
                        id="genetic_risk",
                        options=[
                            {"label": "Low", "value": 0},
                            {"label": "Medium", "value": 1},
                            {"label": "High", "value": 2}
                        ],
                        placeholder="Select genetic risk level",
                        className="w-full"
                    ),
                ], className="mb-4"),

                html.Div([
                    html.Label("Physical Activity (hours/week)", className="text-gray-700"),
                    dcc.Input(type="number", id="physical_activity", placeholder="Enter hours per week", className="w-full p-2 border rounded"),
                ], className="mb-4"),
            ], className="w-1/2 p-2"),

            html.Div([
                html.Div([
                    html.Label("Alcohol Intake Scale 1-5", className="text-gray-700"),
                    dcc.Input(type="number", id="alcohol_intake", placeholder="Enter intake scale", className="w-full p-2 border rounded"),
                ], className="mb-4"),

                html.Div([
                    html.Label("Cancer History", className="text-gray-700"),
                    dcc.Dropdown(
                        id="cancer_history",
                        options=[
                            {"label": "No", "value": 0},
                            {"label": "Yes", "value": 1}
                        ],
                        placeholder="History of cancer?",
                        className="w-full"
                    ),
                ], className="mb-4"),
            ], className="w-1/2 p-2"),
        ], className="flex flex-wrap"),

        # Submit button and prediction output
        html.Div([
            html.Button("Submit", id="submit-button", n_clicks=0, className="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600 w-full"),
            html.Div(id="prediction-output", className="mt-4 text-lg font-semibold text-center text-gray-900 bg-white rounded shadow p-4"),
        ], className="max-w-md mx-auto p-4"),
    ], className="bg-gray-900 min-h-screen p-4")

@callback(
    Output("prediction-output", "children"),
    Input("submit-button", "n_clicks"),
    State("age", "value"),
    State("gender", "value"),
    State("bmi", "value"),
    State("smoking", "value"),
    State("genetic_risk", "value"),
    State("physical_activity", "value"),
    State("alcohol_intake", "value"),
    State("cancer_history", "value"),
)
def predict_cancer_diagnosis(n_clicks, age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history):
    if n_clicks > 0:
        # Check if the model is loaded
        if model is None:
            return "Error: Prediction model not found. Please contact the administrator."
        
        # Check for missing values
        if None in [age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history]:
            return "Please fill out all fields before submitting."
        
        # Prepare input data
        input_data = np.array([[age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history]])
        
        try:
            prediction = model.predict(input_data)
            probability = model.predict_proba(input_data) if hasattr(model, "predict_proba") else None

            if probability is not None:
                prob_text = f" (Probability: {probability[0][1]:.2f})"
            else:
                prob_text = ""

            result = (
                f"Your chances of having cancer are slightly higher. try to mantain a healthy lifestyle"
                if prediction[0] == 1 else
                f"You are not likely to have cancer. Maintain healthy habits."
            )
        except Exception as e:
            result = f"Error during prediction: {str(e)}"
        
        return result
