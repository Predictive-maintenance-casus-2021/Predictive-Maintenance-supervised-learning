from flask import Flask, render_template, request
import os
import webbrowser
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def testing_server():
    return render_template("index.html")


if __name__ == "__main__":
    # Automatically open the browser, if the reload has not yet run
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", use_reloader=True)
