from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


@app.route("/", methods=("GET", "POST"))
def home():
    """
    Reroute
    """

    return redirect(url_for("create"))


@app.route("/chatgpt", methods=("GET", "POST"))
def create():
    """
    Example function where ChatGPT response will come
    """

    if request.method == "POST":
        if request.authorization.token == BEARER_TOKEN:
            return (
                request.get_json()["prompt"]
                + " - Good question, sadly I'm not fully functional juuuuust yet"
            )
        else:
            return "Failed to authorise"
    if request.method == "GET":
        return "Try asking me a question :)"
