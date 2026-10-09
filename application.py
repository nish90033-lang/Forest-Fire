
from flask import Flask, request, render_template
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load the trained model and scaler
with open('Models/ridge.pkl', 'rb') as file:
    ridge_model = pickle.load(file)

with open('Models/scaler.pkl', 'rb') as file:
    standard_scaler = pickle.load(file)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Get input values from the HTML form
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Arrange features in the model's expected order
            features = np.array([[
                Temperature, RH, Ws, Rain,
                FFMC, DMC, ISI, Classes, Region
            ]])

            # Scale the input and predict
            scaled_features = standard_scaler.transform(features)
            prediction = ridge_model.predict(scaled_features)[0]

            return render_template(
                'home.html',
                result=round(float(prediction), 2)
            )

        except (ValueError, TypeError) as error:
            return render_template(
                'home.html',
                error=f"Invalid input: {error}"
            )

    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
