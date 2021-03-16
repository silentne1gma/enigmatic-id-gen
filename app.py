from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

url = "https://randomuser.me/api/"
r = requests.get(url)
random_json = r.text
random = json.loads(random_json)


@app.route("/")
def index():
    return render_template("index.html", random=random)

@app.route("/about")
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


if __name__ == "__main__":
    app.run()