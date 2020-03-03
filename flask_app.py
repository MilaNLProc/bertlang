import os
from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


language_to_flag = {
    "Dutch" : '<span class="flag-icon flag-icon-nl"></span>',
    "French" : '<span class="flag-icon flag-icon-fr"></span>',
    "German" : '<span class="flag-icon flag-icon-de"></span>',
    "Chinese" : '<span class="flag-icon flag-icon-cn"></span>',
    "Japanese" : '<span class="flag-icon flag-icon-jp"></span>',
    "Italian" : '<span class="flag-icon flag-icon-it"></span>',
    "Russian" : '<span class="flag-icon flag-icon-ru"></span>',
    "Finnish" : '<span class="flag-icon flag-icon-fi"></span>',
    "Turkish" : '<span class="flag-icon flag-icon-tr"></span>',
    "Arabic" : '<span class="flag-icon flag-icon-sa"></span>',
    "Spanish" : '<span class="flag-icon flag-icon-es"></span>',
    "English" : '<span class="flag-icon flag-icon-us"></span>',
    "English" : '<span class="flag-icon flag-icon-us"></span>',
    "Portuguese" : '<span class="flag-icon flag-icon-pt"></span>',
    "Mongolian" : '<span class="flag-icon flag-icon-mn"></span>',
    "Korean" : '<span class="flag-icon flag-icon-kr"></span>',
    "Thai" : '<span class="flag-icon flag-icon-th"></span>'
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
    "VSD"	: "Verb Sense Disambiguation",
     "NSD"	: "Noun Sense Disambiguation",
     "SC"	: "Subjectivity Classification",
     "ID"	: "Irony Detection",
     "DDD"	: "Die/Dat Disambiguation",
     "MRC"	: "Machine Reading Comprehension",
     "SPM"	: "Sentence Pair Matching",
     "POS (coarse)" :	"Part of Speech Tagging",
     "POS (fine-grained)"	: "Part of Speech Tagging",
     "LA"	: "Linguistic Acceptability",
     "TER"	:"Textual Entailment Recognition",
     "QA"	: "Question Answering",
     "CI"	: "Commonsense Inference",
     "RC"	: "Reading Comprehension"
}


@app.route("/")
def index():

    with open('static/data/data_example.json') as json_file:
        json_data = json.load(json_file)

    number_of_models = list(map(lambda x: x["name"], json_data))
    number_of_models = len(set(number_of_models))

    number_of_languages = list(map(lambda x: x["language"], json_data))
    number_of_languages = len(set(number_of_languages))

    tasks = []
    entries = 0
    for model in json_data:
        for task in model["tasks"]:
            entries = entries+1
            tasks.append(task["name"])

    number_of_tasks = len(set(tasks))

    stats = {"number_of_models" : number_of_models,
             "number_of_languages" : number_of_languages,
             "number_of_tasks" : number_of_tasks,
             "number_of_entries" : entries}

    number_of_models = list(map(lambda x: x["name"], json_data))
    number_of_models = len(set(number_of_models))

    return render_template("./index.html", json_data=json_data, lang_to_flag = language_to_flag, acronyms=acronyms, stats=stats)

@app.route("/about")
def about():
    return render_template("./about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)