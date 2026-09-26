from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/explore")
def explore():
    return render_template("explore.html")


@app.route("/paths")
def paths():
    return render_template("paths.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")


if __name__ == "__main__":
    app.run(debug=True)