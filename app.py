from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

current_survey = satisfaction_survey

responses = []

@app.route("/")
def home():
    """Generate and show form to ask words."""

    return render_template("home.html", current_survey=current_survey)

@app.route("/begin", methods=["POST"])
def begin():
    """Redirect to first question"""

    responses = []

    return redirect ("question/0")

@app.route("/question/<int:qid>")
def show_question(qid):
    """Display current question"""
    question = current_survey.questions[qid]

    return render_template("question.html", question_num=qid, question=question)

@app.route("/answer", methods=["POST"])
def answer():
    """Collect answer and direct to next question"""
    ans = request.form['answer']
    responses.append(ans)

    if (len(responses) == len(current_survey.questions)):
        return render_template("complete.html", responses=responses)
    else:
        return redirect (f"question/{len(responses)}")