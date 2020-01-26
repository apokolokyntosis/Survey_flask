from flask import render_template, flash, url_for, redirect, session

from flask_survey import app, json_serializer, surveyjs_handler, charts, parser, lists
from flask_survey.forms import CreateSurveyForm, AddQuestionsForm


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
                json_serializer.add_question("rating", form.question_title.data)
            if form.question_type.data == "boolean":
                json_serializer.add_question("boolean", form.question_title.data)
            if form.question_type.data == "comment":
                json_serializer.add_question("comment", form.question_title.data)
            if form.question_type.data == "text":
                json_serializer.add_question("text", form.question_title.data)
            if form.question_type.data == "radiogroup":
                choices_input = form.radiogroup_choices.data
                choices = choices_input.split(";")
                for strings in choices:
                    strings.lstrip()
                json_serializer.add_question("radiogroup", form.question_title.data, choices)
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


@app.route("/survey/<uid>")
def survey(uid):
    survey_list = lists.get_lists()
    dict_id = {}

    for survey in reversed(survey_list):
        dict_id[survey.get("Id")] = [survey.get("PostId"), survey.get("Name")]

    postid = dict_id[uid][0]
    name = dict_id[uid][1]

    return render_template("survey.html", title="survey", postid=postid, uid=uid, name=name)


@app.route("/surveylist", methods=["GET", "POST"])
def surveylist():
    survey_list = lists.get_lists()
    return render_template("surveylist.html", survey_list=survey_list)


@app.route("/about")
def about():
    return render_template("about.html", title="about")


@app.route("/results/<uid>", methods=["GET", "POST"])
def results(uid):
    questions = parser.get_questions(uid)
    s_results = parser.load_results(uid)
    title_dict = parser.get_titles(uid)
    for question in questions:
        charts.create_charts(question, s_results, title_dict)

    return render_template("results.html", questions=questions, uid=uid)


@app.route('/resultsraw')
def resultsraw():
    data = parser.load_results()
    return data
