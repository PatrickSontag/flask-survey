from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

user_responses = []

@app.route("/")
def home():
    """Generate and show form to ask words."""

    return render_template("home.html")

@app.route("/question")
def question():
    """Generate and show form to ask questions."""
    ask = satisfaction_survey.questions[0].question
    return render_template("question.html", ask=ask)


# satisfaction_survey.questions[0].question
# 'Have you shopped here before?'
