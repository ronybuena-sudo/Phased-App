from flask import Flask, render_template
from calculations import calculate_bmr, calculate_tdee, get_current_phase, adjust_calories

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)