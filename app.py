from flask import Flask, render_template, request
from core.command import process_command
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        command = request.form["command"]
        response = process_command(command)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)