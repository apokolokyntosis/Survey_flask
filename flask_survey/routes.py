from flask import render_template, flash, url_for, redirect, session
from flask_survey.forms import CreateSurveyForm, AddQuestionsForm
from flask_survey import app, json_serializer, surveyjs_handler, charts, parser, lists


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/addquestions", methods=["GET", "POST"])
def addquestions():
    form = AddQuestionsForm()
    questions = json_serializer.get_questions()
    if form.validate_on_submit():
        if form.submit_question.data:
            if form.question_type.data == "rating":
                json_serializer.add_question("rating", form.question_title.data, 0, 5)
            if form.question_type.data == "boolean":
                json_serializer.add_question("boolean", form.question_title.data, 0, 5)
            if form.question_type.data == "comment":
                json_serializer.add_question("comment", form.question_title.data, 0, 5)
            flash("Question added", "success")
            return redirect(url_for("addquestions"))
        if form.submit_survey.data:
            survey_name = session.get("active_survey_creation", None)
            print(f"Umfrage {survey_name} wird erstellt...")
            json_serializer.create_json()
            surveyjs_handler.new_survey(survey_name)
            flash('Umfrage "{}" created'.format(survey_name), "success")
            return redirect(url_for("about"))
    return render_template("creation_2.html", title="Frage hinzufügen", form=form, questions=questions)


@app.route("/create", methods=["GET", "POST"])
def create():
    form = CreateSurveyForm()
    if form.validate_on_submit():
        if form.create_survey.data:
            json_serializer.clear_memory()
            session["active_survey_creation"] = form.survey_name.data
            flash('Umfrage "{}" angelegt'.format(form.survey_name.data), "success")
            return redirect(url_for("addquestions"))
    return render_template("creation_1.html", title="Neue Umfrage anlegen", form=form)


@app.route("/survey")
def survey():
    return render_template("survey.html", title="survey")


@app.route("/surveylist")
def surveylist():
    survey_list = lists.get_lists()
    return render_template("surveylist.html", survey_list=survey_list)


@app.route("/about")
def about():
    return render_template("about.html", title="about")


@app.route("/results")
def results():
    questions = parser.get_questions()
    for question in questions:
        if question.endswith("pie"):
            charts.create_pie(question)
        elif question.endswith("cloud"):
            charts.create_cloud(question)
        else:
            charts.create_bar(question)
    return render_template("results.html", questions=questions)


@app.route('/resultsraw')
def resultsraw():
    data = parser.load_data()
    return data
