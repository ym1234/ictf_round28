from flask import Flask, request, jsonify, send_file, render_template, flash, redirect, url_for, Response
import tempfile
from secret import banned_words, key
from subprocess import run

app = Flask(__name__)
app.secret_key = key

HEADERS = ["assert.h", "limits.h", "signal.h", "stdlib.h", "ctype.h", "locale.h", "stdarg.h", "string.h", "errno.h", "math.h", "stddef.h", "time.h", "float.h", "setjmp.h", "stdio.h"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compile", methods=["POST"])
def compile():
    content = request.form
    if not "code" in content:
        return jsonify({"success": False}), 400

    if any(word in content["code"] for word in banned_words):
        flash("Banned word")
        return redirect(url_for("index"))

    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(f"{tmpdirname}/main.c", "w") as srcfilename:
            # Add common includes
            srcfilename.write("\n".join(f"#include <{header}>" for header in HEADERS) + "\n")

            # Add user code
            srcfilename.write(content["code"])

        try:
            result = run(["gcc", "main.c"], timeout=3, cwd=tmpdirname, capture_output=True)
        except TimeoutError:
            flash("Compilation timed out")
            return redirect(url_for("index"))

        if result.returncode == 0:
            return send_file(f"{tmpdirname}/a.out")
        else:
            flash(result.stderr.decode())
            return redirect(url_for("index"))


@app.route("/docker")
def docker():
    return Response(open("Dockerfile").read(), mimetype="text/plain")


@app.route("/source")
def source():
    return Response(open(__file__).read(), mimetype="text/plain")
