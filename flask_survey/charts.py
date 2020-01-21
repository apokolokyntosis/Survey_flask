import os
import io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from wordcloud import WordCloud
from flask import Response
from flask_survey import parser


def create_pie(q):
    plt.clf()
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    title = parser.parse_survey()[q]
    q_data = parser.parse_data(q)
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
    title = parser.parse_survey()[q]
    q_data = parser.parse_data(q)
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
    title = parser.parse_survey()[q]
    q_data = parser.parse_data(q)
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