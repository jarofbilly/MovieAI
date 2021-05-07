import os
from flask import Flask, jsonify, render_template, after_this_request
from time import sleep
import threading

template_dir = os.path.abspath('../frontend')
print(template_dir)
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.js")
def js():
    return render_template("index.js")

@app.route("/api/<string:title>")
def getStuff(title):
    return jsonify({"stuff": "executing"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
