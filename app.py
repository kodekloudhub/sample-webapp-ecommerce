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

images = {
    "apparels": "https://res.cloudinary.com/cloudusthad/image/upload/v1547052428/apparels.jpg",
    "video": "https://res.cloudinary.com/cloudusthad/image/upload/v1547052431/video.jpg"
}

@app.route("/")
def main():
    return render_template('hello.html', APP=APP, COLOR=color_codes[APP], IMAGE=images[APP])


if __name__ == "__main__":

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
