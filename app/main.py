import shutil
import logging
import os
from werkzeug.utils import secure_filename
from pathlib import Path

from flask import Flask, request, jsonify, json, make_response, Response
from flask_cors import CORS, cross_origin
import requests

from utils import text_extraction

application = app = Flask(__name__)

try:
    path = os.path.dirname(os.path.abspath(__file__))
    upload_folder = os.path.join(
        path.replace("/file_folder", ""), "tmp")
    os.makedirs(upload_folder, exist_ok=True)
    app.config['upload_folder'] = upload_folder
except Exception as e:
    app.logger.info('An error occurred while creating temp folder')
    app.logger.error("Exception occurred: {}".format(e))

app.config['UPLOAD_EXTENSIONS'] = ['.docx', '.doc', '.txt', '.pdf', '.html']
cors = CORS(app)


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/')
def upload_file():
    return jsonify('Matan-Ben Nagar python\'s parser!')


@app.route('/plaintext', methods=['POST', 'OPTIONS'])
def extractext():
    print("check 1")
    if request.method == 'OPTIONS':
        print("check 2")
        return _build_cors_preflight_response()

    elif request.method == 'POST':
        print("check 3")

        try:
            print("check 4")
            f = request.files['file']
            file_name = f.filename
            print("check 5")
            save_path = os.path.join(
                app.config.get('upload_folder'), file_name)
            f.save(save_path)
            print("check 6")
            result = text_extraction(save_path)
            return jsonify(result)
        except Exception as e:
            app.logger.info("error occurred")
    else:
        return jsonify("server only allows POST")


if __name__ == "__main__":
    app.run()
