#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask
from flask import request
from flask import Response

from lxml import html


app = Flask(__name__)


@app.route("/")
def root():
    return "Hello World"


@app.route("/pttbeauty", methods=["POST"])
def pttbeauty():
    body = request.data
    root = html.fromstring(body)
    title = root.xpath('//meta[@property="og:title"]/@content')[0]
    imgs = root.xpath('//div[@id="main-content"]/a/@href')
    rtn = []
    for img in imgs:
        rtn.append({
            "title": title,
            "img":img
        })
    return Response(
        json.dumps(rtn), mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)
