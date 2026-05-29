from flask import Flask, render_template, request
from planner import generate_plan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        subjects = request.form["subjects"].split(",")
        subjects = [s.strip() for s in subjects]

        days = int(request.form["days"])
        hours = int(request.form["hours"])

        plan = generate_plan(subjects, days, hours)

        return render_template("index.html", plan=plan)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)