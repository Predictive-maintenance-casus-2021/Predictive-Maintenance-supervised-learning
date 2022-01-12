from flask import Flask, render_template, request
import os
import webbrowser
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def testing_server():
    return render_template("index.html")


@app.route('/home')
def go_to_home():
    print('[!] Go home')
    return 'Done'


@app.route('/info')
def go_to_info():
    print('[!] Go info')
    return 'Done'


# Allows communication between the front and backend server
# ToDo: get rid of when build fully
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response


if __name__ == "__main__":
    # Automatically open the browser, if the reload has not yet run
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", use_reloader=True)
