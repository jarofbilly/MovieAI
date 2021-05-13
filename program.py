import os
from flask import Flask, jsonify, render_template, send_from_directory
from recommend import *

# Set template folder
template_dir = os.path.abspath('frontend')
app = Flask(__name__, template_folder=template_dir)

# Default page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search/<string:title>")
def find(title):
    output = recommendations(title)
    if (output):
        return jsonify({"topRated": output[0], "similar": output[1]})
    else:
        return jsonify({})

# Static routing
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('frontend/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('frontend/css', path)

# Start webserver
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
