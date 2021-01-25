import os
from quart import Quart, jsonify, render_template, after_this_request
from time import sleep
from MovieLens import *
import threading

template_dir = os.path.abspath('../frontend')
print(template_dir)
app = Quart(__name__, template_folder=template_dir)


@app.route("/")
async def home():
    return await render_template("index.html")

@app.route("/index.js")
async def js():
    return await render_template("index.js")

@app.route("/api/<string:title>")
async def getStuff(title):
    search(title)
    return jsonify({"stuff": "executing"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
