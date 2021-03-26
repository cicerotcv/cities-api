# -*- coding: utf-8 -*-
import datetime
import json
import time

from flask import Flask, abort, jsonify, make_response, request

from search import model_selector, search

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return make_response({"error": "Not found."}, 404)


@app.route('/<collection>/', methods=["GET"])
def get_collection(collection: str):
    model = model_selector(collection)

    query = request.args.get("query", None, type=str)
    populate = request.args.get("populate", False, type=json.loads)

    if query == None:
        return make_response({"error": "No query provided."}, 400)


    resp: list = search(collection, query, populate)

    if len(resp) > 20:
        return make_response({"error": "To many results. Consider being more " +
                              "specific.", "matches": len(resp)}, 400)

    resp = json.dumps(resp, ensure_ascii=False, indent=4)
    return resp


if __name__ == "__main__":
    app.run(debug=False)
