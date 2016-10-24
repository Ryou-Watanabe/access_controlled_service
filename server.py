#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket
import sys
import requests
import json
from flask import Flask, request, redirect, url_for, abort, jsonify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from requests_oauthlib import OAuth1Session
from datetime import datetime as dt

app = Flask(__name__)
api = Api(app)

class Response(Resource):
	def get(self):
		return "Server Connected"

class Tweet(Resource):
	def post(self):
		if request.headers['Content-Type'] == 'application/json':
			message = request.json['message']
			self.tweet(message)
		return message

	def tweet(self, message):

		consumer_key = ""
		consumer_secret = ""
		access_token = ""
		access_secret = ""

		twitter = OAuth1Session(consumer_key,consumer_secret,access_token,access_secret)

		now = dt.now().strftime('%m/%d %H:%M:%S')
		params = {"status": message + "\n\n" + now}
		req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
		#print(message+"!!!!!")
		# ここにツイートのコードを書く

class Line(Resource):
	def post(self):
		if request.headers['Content-Type'] == 'application/json':
			message = request.json['message']
			self.lineNotify(message)
		return message

	def lineNotify(self, message):
		s = requests.session()
		url = "https://notify-api.line.me/api/notify"

		data = {
			"message": message,
		}
		headers = {'Authorization': 'Bearer '+'[PUT LINE TOKEN]'}
		r = s.post(url, data=data, headers=headers)
		text = r.text
		text = json.loads(text)
		print(text)

api.add_resource(Response, '/')
api.add_resource(Tweet, '/api/tweet')
api.add_resource(Line, '/api/line')

if __name__ == '__main__':
	ip = socket.gethostbyname(socket.gethostname())
	app.debug=True
	app.run(host=ip)
