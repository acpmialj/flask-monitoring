import logging

from flask import Flask
from flask import jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

api = Flask(__name__)
metrics = PrometheusMetrics(api)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")


@api.route("/")
def oproot():
    return jsonify("Accessing root")


@api.route("/data", methods=['GET'])
def opget():
    return jsonify("Reading data")

@api.route('/data/<int:id>', methods=['DELETE'])
def opdel(id):
    return jsonify(f"Deleting record {id}")

@api.route('/data', methods=['POST'])
def opput():
    data = request.json['data']
    return jsonify(f'Added record: {data}')


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000)