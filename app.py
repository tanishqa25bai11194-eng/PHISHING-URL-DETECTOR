from flask import Flask, render_template, request
import pickle
from feature_extractor import extract_features

app = Flask(__name__)

model = pickle.load(open("phishing_model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=["POST"])
def predict():

    url = request.form["url"]

    features = extract_features(url)

    result = model.predict([features])

    probability = model.predict_proba([features])[0][1]

    if result[0] == 1:
        prediction = "⚠️ Phishing Website Detected"
        color = "red"
    else:
        prediction = "✅ Safe Website"
        color = "green"

    confidence = round(probability * 100,2)

    return render_template(
        "index.html",
        prediction=prediction,
        color=color,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)
    