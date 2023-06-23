from flask import Flask, request, redirect, url_for


app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    """
    Reroute
    """
   

    return redirect(url_for('create'))

@app.route('/chatgpt', methods=('GET', 'POST'))
def create():
    """
    Example function where ChatGPT response will come
    """
    if request.method == 'POST':
        return request.data+" - Good question, sadly I'm not fully functional juuuuust yet"
    if request.method == 'GET':
        return "Try asking me a question :)"