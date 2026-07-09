from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get input values from the form
    area = float(request.form["area"])
    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])
    age = float(request.form["age"])

    # Create DataFrame with correct feature names
    input_data = pd.DataFrame(
        [[area, bedrooms, bathrooms, age]],
        columns=["Area", "Bedrooms", "Bathrooms", "Age"]
    )

    # Predict house price
    prediction = model.predict(input_data)

    return render_template(
        "index.html",
        prediction_text=f"Estimated House Price: ₹ {prediction[0]:,.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)