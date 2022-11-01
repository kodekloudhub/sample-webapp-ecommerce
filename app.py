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
    "video": "#30336b",
    "404": "#3e169d",
    "food": "#30336b",
    "pay": "#2980b9"
}

images = {
    "apparels": "https://res.cloudinary.com/cloudusthad/image/upload/v1547052428/apparels.jpg",
    "video": "https://res.cloudinary.com/cloudusthad/image/upload/v1547052431/video.jpg",
    "404": "https://res.cloudinary.com/cloudusthad/image/upload/v1547053817/error_404.png",
    "food": "https://res.cloudinary.com/cloudusthad/image/upload/v1547258061/macaroon-PVQTF45-low.jpg",
    "pay": "https://res.cloudinary.com/cloudusthad/image/upload/v1547306802/a-customer-making-wireless-or-contactless-payment-PSWG6FE-low.jpg"
}


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('hello.html', COLOR=color_codes[APP], IMAGE=images["404"]), 404


@app.route('/')
def main():
    return render_template('hello.html', COLOR=color_codes[APP], IMAGE=images[APP])


if __name__ == "__main__":

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
