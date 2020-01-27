import os
import io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from wordcloud import WordCloud
from flask import Response
from flask_survey import parser


def create_charts(question, s_results, title_dict):
    plt.clf()
    dirname = os.path.dirname(__file__)
    output_path = os.path.join(dirname, "static/assets/charts")
    # s_data = parser.load_survey(uid)
    # s_results = parser.load_results(uid)
    # title_dict = parser.get_titles(uid)

    q_title = title_dict[question]
    q_results = parser.get_results_for_question(s_results, question)
    if question.endswith("pie"):
        print(q_results)
        keys, counts = np.unique(q_results, return_counts=True)
        colors = ['lightskyblue', 'lightcoral']
        labels = []
        print(keys)
        for i in range(len(keys)):
            if keys[i] == "True":
                keys[i] = "Ja"
            if keys[i] == "False":
                keys[i] = "Nein"
        # for items in keys:
        #     if items not in labels:
        #         if items == "False":
        #             labels.insert(0, "Nein")
        #         if items == "True":
        #             labels.append("Ja")
        #         else:
        #             labels.append(items)
            # if items == "False":
            #     labels.insert(0, "Nein")
            # else:
            #     labels.append("Ja")
        # labels_dup = []
        # for i in labels:
        #     if i not in labels_dup:
        #         labels_dup.append(i)
        print(labels)
        # print(labels_dup)
        plt.pie(counts, labels=keys, autopct='%1.1f%%', colors=colors,
                shadow=False, startangle=0)
        plt.axis('equal')

    elif question.endswith("cloud"):
        cloud_list = " ".join(q_results)
        wordcloud = WordCloud(width=480, height=480, margin=0, background_color="lightskyblue").generate(
            cloud_list)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)

    else:
        keys, counts = np.unique(q_results, return_counts=True)
        y_pos = np.arange(len(keys))
        plt.bar(y_pos, counts, color="lightskyblue", alpha=0.7)
        yint = range((min(counts)), (max(counts)) + 2)
        plt.yticks(yint)
        plt.xticks(y_pos, keys)
        plt.ylabel('Anzahl')
        plt.xlabel('Bewertung')
        plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.2)

    fig = plt.gcf()
    # fig.suptitle(q_title, fontsize=16)
    fig.savefig("{}/{}.png".format(output_path, question))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")
