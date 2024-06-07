from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("best_svm_model.joblib")

# Get feature names from the model (if stored)
feature_names = model.feature_names_in_

feature_names.tolist()


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Ensure the data has the correct feature names
    features = pd.DataFrame([data["features"]], columns=feature_names)
    prediction = model.predict(features)
    return jsonify({"prediction": prediction[0]})


if __name__ == "__main__":
    app.run(debug=True)
