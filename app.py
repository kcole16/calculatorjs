#!/usr/bin/env python
# -*- coding: utf-8 -*-

#flask
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def handle():
	return render_template('calculator.html')

if __name__ == "__main__":
	app.run(debug=True, port=5000)
