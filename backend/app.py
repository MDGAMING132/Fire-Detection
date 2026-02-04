import os
from flask import Flask, jsonify, send_from_directory, request
import requests
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")


def get_env(name, default=""):
    value = os.environ.get(name, default)
    return value if value is not None else ""


@app.get("/")
def index():
    # Serve the new "Professional UI" by default
    return send_from_directory(os.path.join(BASE_DIR, "frontend"), "alert_system.html")

@app.get("/map")
def global_map():
    # Fallback to the old global map if needed
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/assets/<path:subpath>")
def frontend_assets(subpath):
    # Serve assets from frontend/assets explicitly
    return send_from_directory(os.path.join(BASE_DIR, "frontend/assets"), subpath)

@app.get("/scripts/<path:subpath>")
def frontend_scripts(subpath):
     # Serve scripts from root/scripts or frontend/scripts depending on where they are
     # Based on file listing, there is a 'scripts' dir in root.
     return send_from_directory(os.path.join(BASE_DIR, "scripts"), subpath)

@app.get("/<path:filename>")
def static_files(filename):
    # Fallback for other root files
    return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
