import os
from flask import Flask, render_template
import json

app = Flask(__name__)


language_to_flag = {
    "Dutch" : '<span class="flag-icon flag-icon-nl"></span>'
}

acronyms = {
    "PST":	"Part of Speech Tagging",
    "DP":	"Dependency Parsing",
    "NER":	"Named Entity Recognition",
    "NLI":	"Natural Language Inference",
    "PP":	"Paraphrase",
    "WSD":	"Word Sense Disambiguation"	,
    "TC":	"Text Classification"	,
    "CP":	"Constituency Parsing"	,
    "SA":	"Sentiment Analysis",
    "SRL":	"Semantic Role Labeling",
    "STR":	"Spatio-Temporal Relation",
    "LPR":	"Linguistic Properties Recognition",
    "OLI":	"Offensive Language Identification",
    "BPE" :"Byte Pair Encoding",
    "DP-UAS":	"Unlabeled Attachment Score"	,
    "DP-LAS":	"Labeled Attachment Score",
}


@app.route("/")
def index():

    with open('data/data_example.json') as json_file:
        json_data = json.load(json_file)

    return render_template("./index.html", json_data=json_data, lang_to_flag = language_to_flag, acronyms=acronyms)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)