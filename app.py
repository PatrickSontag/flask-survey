from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    """Generate and show form to ask words."""

    return render_template("home.html")
