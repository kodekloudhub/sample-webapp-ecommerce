from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

APP = os.environ.get('APP') or "localhost"


@app.route("/")
def main():
    return render_template('hello.html', APP=APP)


if __name__ == "__main__":

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
