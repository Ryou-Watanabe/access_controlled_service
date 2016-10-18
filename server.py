#! /usr/bin/env python
# -*- coding: utf-8 -*-
#*******************************************
# Name:        	server.py
# Author:      	Ryou.W
# Created:     	18/10/2016
# Last Date:   	18/10/2016
# Note:
# Issue:
# Reference:http://flask-docs-ja.readthedocs.io/en/latest/quickstart/
#*******************************************

import os
import socket
import sys
import requests
import json
from flask import Flask, request, redirect, url_for, abort, jsonify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)

class Tweet(Resource):
	def post(self):
		if request.headers['Content-Type'] == 'application/json':
			message = request.json['message']
			self.tweet(message)
		return message

	def tweet(self, message):
		print(message+"!!!!!")
		# ここにツイートのコードを書く

api.add_resource(Tweet, '/api/tweet')

if __name__ == '__main__':
	ip = socket.gethostbyname(socket.gethostname())
	app.debug=True
	app.run(host=ip)
