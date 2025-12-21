from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained artifacts
model = pickle.load(open("artifacts/model.pkl", "rb"))
preprocessor = pickle.load(open("artifacts/preprocessor.pkl", "rb"))

def risk_level(score):
    if score >= 80:
        return "Low Risk 🟢"
    elif score >= 50:
        return "Medium Risk 🟡"
    else:
        return "High Risk 🔴"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_df = pd.DataFrame(
            [{
                "gender": request.form["gender"],
                "race_ethnicity": request.form["race_ethnicity"],
                "parental_level_of_education": request.form["parent_education"],
                "lunch": request.form["lunch"],
                "test_preparation_course": request.form["test_prep"],
                "reading_score": float(request.form["reading_score"]),
                "writing_score": float(request.form["writing_score"])
            }]
        )

        transformed = preprocessor.transform(input_df)
        prediction = model.predict(transformed)[0]

        return render_template(
            "result.html",
            score=round(prediction, 2),
            risk=risk_level(prediction)
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
