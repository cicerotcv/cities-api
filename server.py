# -*- coding: utf-8 -*-
import datetime
import json
import time

from flask import Flask, abort, jsonify, make_response, request

from search import search

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return make_response({"error": "Not found."}, 404)


@app.route('/cities', methods=["GET"])
def get_city():
    city = request.args.get("city", None)
    if city == None:
        return make_response({"error": "No query provided."}, 400)

    resp = search(city)

    if len(resp) > 20:
        return make_response({"error": "To many results. Consider being more " +
                              "specific.", "matches": len(resp)}, 400)

    resp = json.dumps(resp, ensure_ascii=False, indent=4)
    return resp


if __name__ == "__main__":
    app.run(debug=False)
