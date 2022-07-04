#!/usr/bin/env python
# encoding: utf-8
import json
import os
from flask import Flask, request, jsonify
from nlpSentiment import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def isNegative():
    # print('x\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\nx\n')
    record = json.loads(request.data)
    tmp = dict(record)
    # print(record)
    for k,v in tmp.items():
        record[k]['isNegative'] = isNegativeNLP(v['text'])
    return jsonify(record)


# app.run( po)
