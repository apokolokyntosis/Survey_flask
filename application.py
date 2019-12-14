from flask import Flask, render_template
import requests
import numpy as np
import io
import matplotlib as plt
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


application = app = Flask(__name__)

# Survey1:
    # id  75e58d2a-5f02-4914-8181-a52047a3f76f
    # accesskey 3bc43120cf784d489aefbc4cec9b1268
    # ResultId 084644b9-b734-4d00-9afe-1fa82b803cb2
# Survey 2:
    # id e8e348cb-6a20-4b7a-8669-9bdb1b207e44


id = "e8e348cb-6a20-4b7a-8669-9bdb1b207e44"
result_id = "c53520d2-4bfc-4af7-ac15-42cb129eae86"
accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id,accesskey)


@app.route('/')
def hello_world():

    return render_template('index.html')


@app.route('/results')
def generate_results():
    data = load_data()

    return render_template("results")



def result_count():
    data = load_data()
    return "ResultCount: {}".format(data["ResultCount"])


@app.route('/resultsoverview')
def generate_overview():
    data = load_data()


@app.route('/emotionsavg')
def emotionscores():
    data = load_data()
    scores = []
    for entry in data["Data"]:
        if "emotionsratings-widget" in entry.keys():
            scores.append(int(entry["emotionsratings-widget"]))
    return "Emotions average: " + str(sum(scores) / len(scores))



@app.route('/resultsraw')
def results_raw():
    data = load_data()
    return data


@app.route('/emotionsplot')
def plot_png():
    data = load_data()
    scores = []
    for entry in data["Data"]:
        if "emotionsratings-widget" in entry.keys():
            scores.append(int(entry["emotionsratings-widget"]))
    x, y = np.unique(np.asarray(scores), return_counts=True)

    fig = create_figure(x, y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


results_plot = {}

# loads mail addresses in a list
def get_mail():
    data = load_data()
    mail_list = []
    for entry in data["Data"]:
        if "mail_form" in entry.keys():
            mail_list.append((entry["mail_form"]))
    return mail_list


# def create_plot_bin(name,category,answer):
#     data=load_data()
#     for answer in data["Data"]:
#


def create_plot(question, answer):
    data = load_data()
    scores = []
    for entry in data["Data"]:
        if "{}".format(question) in entry.keys():
            scores.append((entry["".format(question)]))

    labels =






def create_plot_(name,category,answer):
    data = load_data()
    scores = []
    for entry in data["Data"]:
        if "{}".format(name) in entry.keys():
            scores.append((entry["emotionsratings-widget"])
    x, y = np.unique(np.asarray(scores), return_counts=True)

    fig = create_figure(x, y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


def create_figure(x, y):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.bar(x, y)
    return fig


def load_data():
    results = requests.get(url=url_results)
    results_json = results.json()
    return results_json


if __name__ == '__main__':
    app.run(debug=True)
