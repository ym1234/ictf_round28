#!/usr/bin/env python

from os import urandom
from flask import Flask, Response

app = Flask(__name__)

@app.route("/pin")
def pin():
    rand = int.from_bytes(urandom(4), "big")
    return Response(f"Your unique pin is: <b>{rand}")


@app.route("/")
def source():
    with open(__file__, "r") as f:
        source = f.read()
    return Response(source, mimetype="text/plain")


@app.route("/docker")
def docker_source():
    with open("Dockerfile", "r") as f:
        source = f.read()
    return Response(source, mimetype="text/plain")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
