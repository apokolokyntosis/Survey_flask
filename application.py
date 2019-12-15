from flask import Flask, render_template, Response
import requests
import io
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


application = app = Flask(__name__)

# Survey1:
    # id  75e58d2a-5f02-4914-8181-a52047a3f76f
    # accesskey 3bc43120cf784d489aefbc4cec9b1268
    # ResultId 084644b9-b734-4d00-9afe-1fa82b803cb2
# Survey 2:
    # id e8e348cb-6a20-4b7a-8669-9bdb1b207e44


id = "990c9984-470b-4581-bcbf-0395366a5afd"
result_id = "c53520d2-4bfc-4af7-ac15-42cb129eae86"
accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id, accesskey)
url_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(id)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/results')
def results():
    questions = get_questions()
    print("questions", questions)
    for question in questions:
        if question.endswith("pie"):
            create_pie(question)
        else:
            create_bar(question)
    return render_template("results.html", questions=questions)


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


@app.route('/resultsraw')
def resultsraw():
    data = load_data()
    return data


# @app.route('/bar')
# def plot():
#     return create_bar("question2")
#
# @app.route('/pie')
# def pie():
#     return create_pie("question2")

def get_questions():
    data = load_data()
    questions = []
    first_dict = data["Data"][0]
    print(first_dict)
    for key in first_dict:
        if key.startswith("question"):
            questions.append(str(key))
    print(questions)
    return questions


def create_pie(q):
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    title = parse_survey()[q]
    q_data = parse_data(q)
    keys, counts = np.unique(q_data, return_counts=True)
    plt.pie(counts, labels=keys, autopct='%1.1f%%',
            shadow=True, startangle=0)
    plt.axis('equal')
    fig = plt.gcf()
    fig.suptitle(title, fontsize=16)
    plt.savefig("{}/{}.png".format(output_path, q))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


def create_bar(q):
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    title = parse_survey()[q]
    print("title:", title)
    q_data = parse_data(q)
    keys, counts = np.unique(q_data, return_counts=True)
    fig = create_figure(keys, counts)
    fig.suptitle(title, fontsize=16)
    fig.savefig("{}/{}.png".format(output_path, q))
    plt.show()
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
    print("survey:", survey)
    title_dict = {}
    for page in survey["pages"]:
        title_dict[page["elements"][0]["name"]] = page["elements"][0]["title"]
    print("titledict:", title_dict)
    return title_dict


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
