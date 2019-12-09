from flask import Flask, render_template, request
import requests
import numpy as np
import matplotlib.pyplot as plt

import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

application = app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# GET api/MySurveys/getSurveyResults/{id}?accessKey={accessKey}&from={from}&till={till}
# GET api/MySurveys/getSurveyResults/{75e58d2a-5f02-4914-8181-a52047a3f76f}?accessKey={3bc43120cf784d489aefbc4cec9b1268}&from={from}&till={till}
# GET api/Survey/getSurvey?surveyId={75e58d2a-5f02-4914-8181-a52047a3f76f}
# id  75e58d2a-5f02-4914-8181-a52047a3f76f
# accesskey 3bc43120cf784d489aefbc4cec9b1268
# ResultId 084644b9-b734-4d00-9afe-1fa82b803cb2

URL_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/75e58d2a-5f02-4914-8181-a52047a3f76f?accessKey=3bc43120cf784d489aefbc4cec9b1268"
r = requests.get(url=URL_results)
data = r.json()


@app.route('/resultcount')
def process_data():
    data = load_data()
    return "ResultCount: {}".format(data["ResultCount"])


@app.route('/emotionsavg')
def emotionscores():
    data = load_data()
    scores = []
    for entry in data["Data"]:
        if "emotionsratings-widget" in entry.keys():
            scores.append(int(entry["emotionsratings-widget"]))
    return "Emotions average: " + str(sum(scores) / len(scores))


@app.route('/results')
def results():
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


def create_figure(x, y):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.bar(x, y)
    return fig


def load_data():
    URL_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/75e58d2a-5f02-4914-8181-a52047a3f76f?accessKey=3bc43120cf784d489aefbc4cec9b1268"
    r = requests.get(url=URL_results)
    data = r.json()
    return data


if __name__ == '__main__':
    app.run(debug=True)
