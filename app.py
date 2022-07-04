#!/usr/bin/env python
# encoding: utf-8
import json
import os
from flask import Flask, request, jsonify
from nlpSentiment import *

app = Flask(__name__)


@app.route("/", methods=["POST"])
def isNegative():
    record = json.loads(request.data)
    isNegativeNLP(record['text'])
    return jsonify({"isNegative": False})


app.run( port=os.environ.get('PORT', 3000))