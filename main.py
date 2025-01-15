from flask import Flask, render_template

app_skills = Flask(__name__)

@app_skills.route("/")
def homepage():
    return render_template("homepage.html")

@app_skills.route("/about")
def aboutpage():
    return render_template("about.html")

if __name__ == "__main__":
    app_skills.run(debug=True, port=2500)

