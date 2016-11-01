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

number = 0

class Response(Resource):
	def __init__(self):
		global number

	def get(self):
		global number
		return "now OKLAB member : %s"%number

	def post(self):
		global number
		if request.headers['Content-Type'] == 'application/json':
			self.message = request.json['message']
			if(self.message == "in"):
				number += 1
			elif(self.message == "out"):
				number -= 1
		return number


class SNS(Resource):
	def post(self):
		if request.headers['Content-Type'] == 'application/json':
			self.message = request.json['message']
			self.postAll()
		return self.message

	def slack(self):
		print(self.message)
		now = dt.now().strftime('%m/%d %H:%M:%S')
		data = {
			"text": self.message + "\n\n" + now,
			"username":'bot_desuyo',
			"icon_emoji":"grin",
			"channel":'#bot_room',
			}
		url = ""
		req = requests.post(url, data=json.dumps(data))

	def lineNotify(self):
		print(self.message)
		s = requests.session()
		url = "https://notify-api.line.me/api/notify"

		data = {
			"message": self.message,
		}
		headers = {'Authorization': 'Bearer '+''}
		r = s.post(url, data=data, headers=headers)
		text = r.text
		text = json.loads(text)
		print(text)

	def tweet(self):
		print(self.message)
		consumer_key = ""
		consumer_secret = ""
		access_token = ""
		access_secret = ""

		twitter = OAuth1Session(consumer_key,consumer_secret,access_token,access_secret)

		now = dt.now().strftime('%m/%d %H:%M:%S')
		params = {"status": self.message + "\n\n" + now}
		req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)

	def postAll(self):
		pass
		# self.tweet()
		# self.slack()
		# self.lineNotify()

class Post(Resource):
	def post(self):
		if request.headers['Content-Type'] == 'application/json':
			self.message = request.json['message']

			number = self.calc()
			s=SNS()
			s.message = self.message
			s.postAll()
			print(self.message)
		return number

	def calc(self):
		global number
		if self.message == "in":
			number += 1
		elif self.message == "out":
			number -= 1
		elif self.message == "init":
			number = 0
		self.message = "now OKLAB member : %s"%number
		return number


api.add_resource(Response, '/')
api.add_resource(SNS, '/api/sns')
api.add_resource(Post, '/api/post')

if __name__ == '__main__':
	# ip = socket.gethostbyname(socket.gethostname())
	ip = "127.0.0.1"
	app.debug=True
	app.run(host=ip)
