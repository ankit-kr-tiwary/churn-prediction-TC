from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
try:
    model = joblib.load("model/churn_model.pkl")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route("/", methods=["GET"])
def home():
    return "✅ Churn Prediction API is running! Use the `/predict` endpoint with a POST request."

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model is not loaded."}), 500

    try:
        # Parse input data
        input_data = request.get_json()
        df = pd.DataFrame([input_data])

        # Predict
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        # Return response
        return jsonify({
            "churn_prediction": int(prediction),
            "churn_probability": round(probability, 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
