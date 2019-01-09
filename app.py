from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

APP = os.environ.get('APP') or "localhost"

color_codes = {
    "apparels": "#2980b9",
    "video": "#30336b"
}

@app.route("/")
def main():
    return render_template('hello.html', APP=APP, COLOR=color_codes[APP])


if __name__ == "__main__":

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
