import os
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():

    with open('data/data_example.json') as json_file:
        json_data = json.load(json_file)

    return render_template("./index.html", json_data=json_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)