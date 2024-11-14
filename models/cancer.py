from dash import html, dcc, Input, Output, callback, State
from joblib import load

model = load("models/cancer_model.joblib")

def cancer_model():
    return html.Div([
        html.Form([
            html.Div([
                html.Label("Age"),
                dcc.Input(type="number", id="age", className="mb-4"),
            ], className="mb-4"),
            
            html.Div([
                html.Label("Gender"),
                dcc.Dropdown(
                    id="gender",
                    options=[
                        {"label": "Male", "value": 0},
                        {"label": "Female", "value": 1}
                    ],
                    className="mb-4"
                ),
            ], className="mb-4"),
            
            html.Div([
                html.Label("BMI"),
                dcc.Input(type="number", id="bmi", className="mb-4"),
            ], className="mb-4"),
            
            html.Div([
                html.Label("Smoking"),
                dcc.Dropdown(
                    id="smoking",
                    options=[
                        {"label": "No", "value": 0},
                        {"label": "Yes", "value": 1}
                    ],
                    className="mb-4"
                ),
            ], className="mb-4"),
            
            html.Div([
                html.Label("Genetic Risk"),
                dcc.Dropdown(
                    id="genetic_risk",
                    options=[
                        {"label": "Low", "value": 0},
                        {"label": "Medium", "value": 1},
                        {"label": "High", "value": 2}
                    ],
                    className="mb-4"
                ),
            ], className="mb-4"),
            
            html.Div([
                html.Label("Physical Activity (hours/week)"),
                dcc.Input(type="number", id="physical_activity", className="mb-4"),
            ], className="mb-4"),
            
            html.Div([
                html.Label("Alcohol Intake Scale"),
                dcc.Input(type="number", id="alcohol_intake", className="mb-4"),
            ], className="mb-4"),
            
            html.Div([
                html.Label("Cancer History"),
                dcc.Dropdown(
                    id="cancer_history",
                    options=[
                        {"label": "No", "value": 0},
                        {"label": "Yes", "value": 1}
                    ],
                    className="mb-4"
                ),
            ], className="mb-4"),
            
            html.Button("Submit", id="submit-button", n_clicks=0),
        ]),
        
        html.Div(id="prediction-output", className="mt-4"),
    ])

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
        if None in [age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history]:
            return "Please fill out all fields before submitting."

        input_data = [[age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history]]
        
        prediction = model.predict(input_data)
        
        result = "You are likely to have cancer, exercise healthy precautions to decrease your chances" if prediction[0] == 1 else "You are not likely to have cancer, stay healthy!"
        
        return result
