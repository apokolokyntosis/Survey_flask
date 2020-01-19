from flask import Flask, render_template, Response, flash, url_for, redirect
import requests
import io
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from wordcloud import WordCloud

from forms import CreateSurveyForm

import surveyjs_handler
import json_serializer

application = app = Flask(__name__)

app.config["SECRET_KEY"] = "760bb722fb969ca1ee600a8ac52b6a7d"

# Survey1:
# id  75e58d2a-5f02-4914-8181-a52047a3f76f
# accesskey 3bc43120cf784d489aefbc4cec9b1268
# ResultId 084644b9-b734-4d00-9afe-1fa82b803cb2
# Survey 2:
# id e8e348cb-6a20-4b7a-8669-9bdb1b207e44


id = "7b8ea9b3-284d-42fb-b08a-09ceb317cf2e"
accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id, accesskey)
url_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(id)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index1.html')


@app.route("/create", methods=["GET", "POST"])
def create():
    form = CreateSurveyForm()
    if form.validate_on_submit():
        # json_serializer.init()
        if form.question_type.data == "rating":
            json_serializer.add_question("rating", form.question_title.data, 0, 5)
        json_serializer.create_json()
        surveyjs_handler.new_survey(form.survey_name.data)
        flash("Survey {} created".format(form.survey_name.data), "success")

        return redirect(url_for("create"))
    return render_template("creation.html", title="Create a survey", form=form)


@app.route("/survey")
def survey():
    return render_template("survey.html", title="survey")

@app.route("/results")
def results():
    questions = get_questions()
    for question in questions:
        if question.endswith("pie"):
            create_pie(question)
        elif question.endswith("cloud"):
            create_cloud(question)
        else:
            create_bar(question)
    return render_template("results1.html", questions=questions)


@app.route('/results1')
def results1():
    return render_template("survey.html")


@app.route('/resultsraw')
def resultsraw():
    data = load_data()
    return data


def get_questions():
    data = load_data()
    questions = []
    first_dict = data["Data"][0]
    for key in first_dict:
        if key.startswith("question"):
            questions.append(str(key))
    return questions


def create_pie(q):
    plt.clf()
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    title = parse_survey()[q]
    q_data = parse_data(q)
    keys, counts = np.unique(q_data, return_counts=True)
    colors = ['lightskyblue', 'lightcoral']
    # debug
    labels = ["Nein", "Ja"]
    plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=colors,
            shadow=False, startangle=0)
    plt.axis('equal')
    fig = plt.gcf()
    fig.suptitle(title, fontsize=16)
    plt.savefig("{}/{}.png".format(output_path, q))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


# TODO: auslagern
def create_bar(q):
    plt.clf()
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    title = parse_survey()[q]
    q_data = parse_data(q)
    keys, counts = np.unique(q_data, return_counts=True)
    y_pos = np.arange(len(keys))
    plt.bar(y_pos, counts, color="lightskyblue", alpha=0.7)
    yint = range((min(counts)), (max(counts)) + 2)
    plt.yticks(yint)
    plt.xticks(y_pos, keys)
    plt.ylabel('Anzahl')
    plt.xlabel('Bewertung')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.2)
    fig = plt.gcf()
    # fig = create_figure(keys, counts)
    fig.suptitle(title, fontsize=16)
    fig.savefig("{}/{}.png".format(output_path, q))
    # plt.show()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


def create_cloud(q):
    plt.clf()
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    title = parse_survey()[q]
    q_data = parse_data(q)
    cloud_list = " ".join(q_data)
    wordcloud = WordCloud(width=480, height=480, margin=0, background_color="lightskyblue").generate(cloud_list)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    fig = plt.gcf()
    fig.suptitle(title, fontsize=16)
    fig.savefig("{}/{}.png".format(output_path, q))
    # plt.show()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


# loads mail addresses in a list
def get_mail():
    mail_list = parse_data("mail_form")
    return mail_list


# parses values for a specific question into a list
def parse_data(q):
    data = load_data()
    q_results = []
    for entry in data["Data"]:
        if "{}".format(q) in entry.keys():
            q_results.append(str(entry[q]))
    return q_results


# parse survey_json for question titles -> returns dict with question
# as key, and title as value
def parse_survey():
    survey = load_survey()
    title_dict = {"question1": "Wie hat Ihnen die heutige Veranstaltung gefallen?",
                  "question2pie": "Fühlen Sie sich ausreichend repräsentiert?",
                  "question3pie": "Fühlen Sie sich ausreichend informiert?",
                  "question4cloud": "Welchem Thema wurde ihrer Meinung\n nach noch nicht genug Beachtung geschenkt?"
                  }
    # for page in survey["pages"]:
    #     title_dict[page[0]["elements"][0]["name"]] = page[0]["elements"][0]["title"]["de"]
    #     print(title_dict)
    return title_dict


# delete
def create_figure(x, y):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.bar(x, y)
    return fig


def load_data():
    results = requests.get(url=url_results)
    results_json = results.json()
    return results_json


def load_survey():
    survey = requests.get(url=url_survey)
    survey_json = survey.json()
    return survey_json


def result_count():
    data = load_data()
    return data["ResultCount"]


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/emotionsavg')
# def emotionscores():
#     data = load_data()
#     scores = []
#     for entry in data["Data"]:
#         if "emotionsratings-widget" in entry.keys():
#             scores.append(int(entry["emotionsratings-widget"]))
#     return "Emotions average: " + str(sum(scores) / len(scores))


# @app.route('/emotionsplot')
# def plot_png():
#     data = load_data()
#     scores = []
#     for entry in data["Data"]:
#         if "emotionsratings-widget" in entry.keys():
#             scores.append(int(entry["emotionsratings-widget"]))
#     x, y = np.unique(np.asarray(scores), return_counts=True)
#     fig = create_figure(x, y)
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype="image/png")