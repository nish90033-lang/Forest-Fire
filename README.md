# Forest Fire Prediction

A machine learning web application that predicts the Fire Weather Index (FWI) from weather and fire-weather observations. The project uses a trained Ridge Regression model and a fitted feature scaler, with a Flask application serving the prediction interface.

## Project Overview

The application collects the following input features from the user:

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Initial Spread Index (ISI)
- Classes
- Region

The submitted values are preprocessed using the saved scaler and passed to the trained Ridge Regression model to generate an FWI prediction.

> **Note:** The input feature names, order, and preprocessing must match the model's training pipeline. Check the training notebook before using predictions for any real-world decisions.

## Repository Structure

```text
Forest-Fire/
├── Models/
│   ├── ridge.pkl
│   └── scaler.pkl
├── Notebooks/
├── templates/
│   ├── index.html
│   └── home.html
├── Algerian_forest_fires_cleaned_dataset.csv
├── Algerian_forest_fires_dataset_UPDATE.csv
├── application.py
└── README.md
```

The exact files inside `Models/`, `Notebooks/`, and `templates/` may vary with your current repository version.

## Technologies Used

- Python
- Flask
- NumPy
- Pandas
- scikit-learn
- Pickle for loading the trained model and scaler
- HTML and Jinja templates
- Ridge Regression

## Dataset

This repository includes CSV files related to the Algerian Forest Fires dataset:

- `Algerian_forest_fires_dataset_UPDATE.csv`
- `Algerian_forest_fires_cleaned_dataset.csv`

Review the notebooks to understand the cleaning, feature selection, preprocessing, and model-training steps used for the saved model.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nish90033-lang/Forest-Fire.git
cd Forest-Fire
```

### 2. Create and activate a virtual environment

**Windows Command Prompt:**

```cmd
python -m venv myenv
myenv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the core dependencies:

```bash
pip install flask numpy pandas scikit-learn
```

### 4. Verify the model files

Confirm that these files exist relative to `application.py`:

```text
Models/ridge.pkl
Models/scaler.pkl
```

The saved model and scaler must be compatible with the installed scikit-learn version and with each other.

### 5. Run the application

```bash
python application.py
```

Open the following address in your browser:

http://127.0.0.1:5000/

To access the development server from another device on the same network, use the host address printed by Flask, provided your firewall and network settings allow it.

## How to Use

1. Open the application in your browser.
2. Enter the required weather and fire-weather feature values.
3. Click **Predict**.
4. View the predicted Fire Weather Index (FWI) on the page.

Use values in the ranges and formats expected by the training data. The prediction quality depends on the training data, model evaluation, and matching preprocessing.

## Model and Preprocessing

The Flask application loads two serialized artifacts:

- `Models/ridge.pkl` — trained Ridge Regression estimator.
- `Models/scaler.pkl` — fitted feature scaler.

The scaler transforms the input features before they are passed to the model. Keep the feature order and preprocessing consistent with training. If categorical features such as `Classes` or `Region` were encoded during training, apply the same encoding at prediction time rather than treating them as arbitrary numeric inputs.

**Security note:** Only load pickle files from sources you trust. Pickle files can execute code when deserialized.

## Troubleshooting

- **Template not found:** Make sure the HTML files are in the `templates/` directory.
- **404 on the prediction route:** Check that the form action uses Flask's `url_for('predict_datapoint')` and that the route is named correctly.
- **Template syntax error:** Flask uses Jinja syntax, such as `{{ url_for('predict_datapoint') }}`, not Django's `{% url ... %}` tag.
- **Missing model file:** Run the application from the project root and verify the paths under `Models/`.
- **Feature-count or prediction errors:** Confirm the model's expected feature count, feature order, data types, and preprocessing against the training notebook.

## Future Improvements

- Add input validation and clearer user-facing error messages.
- Display model evaluation metrics and explain the meaning of the prediction.
- Add automated tests for the prediction route and preprocessing pipeline.
- Improve the interface with responsive styling and accessible form labels.
- Document the dataset source, model performance, and supported input ranges.

## Disclaimer

This project is intended for educational and demonstration purposes. Its predictions should not be used as the sole basis for fire-risk assessment or emergency decisions.

## Author

**Nishant Suryavanshi**

GitHub: [nish90033-lang](https://github.com/nish90033-lang)
