import os
from datetime import datetime

from flask import Flask, jsonify, render_template

# Elastic Beanstalk's Python platform expects the WSGI callable
# to be named 'application' by default.
application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html", env=os.environ.get("APP_ENV", "local"))


@application.route("/health")
def health():
    # EB's load balancer / health checker hits this path.
    # Keep it fast and dependency-free.
    return jsonify(status="ok", time=datetime.utcnow().isoformat() + "Z")


@application.route("/api/version")
def version():
    return jsonify(version=os.environ.get("APP_VERSION", "0.1.0"))


if __name__ == "__main__":
    # Only used for local `python application.py` runs.
    # EB runs this via gunicorn/WSGI, not this block.
    application.run(host="0.0.0.0", port=5000, debug=True)
