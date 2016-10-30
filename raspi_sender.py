#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json


def twitterPost(message):
	s = requests.session()
	url = "http://192.168.11.10:5000/api/tweet"
	data = {
	"message" : message
	}
	headers={'Content-Type': 'application/json'}
	# r = s.get(url=url, params=data)
	r = s.post(url=url, data=json.dumps(data), headers=headers)
	# text = r.text
	# text = json.loads(text)
	# print("「"+text.encode("utf-8")+"」をtweetしました")
	# return r.text.encode("utf-8")

def linePost(message):
	s = requests.session()
	url = "http://192.168.11.10:5000/api/line"
	data = {
	"message" : message
	}
	headers={'Content-Type': 'application/json'}
	r = s.post(url=url, data=json.dumps(data), headers=headers)
	text = r.text
	text = json.loads(text)
	print("「"+text.encode("utf-8")+"」をlineNotifyしました")
	# return r.text.encode("utf-8")

def slackPost(message):
	s = requests.session()
	url = "http://192.168.11.10:5000/api/slack"
	data = {
	"message" : message
	}
	headers={'Content-Type': 'application/json'}
	r = s.post(url=url, data=json.dumps(data), headers=headers)
	# text = r.text
	# text = json.loads(text)
	# print("「"+text.encode("utf-8")+"」をslackPostしました")
	# # return r.text.encode("utf-8")

def calcPost(message):
	s = requests.session()
	url = "http://192.168.11.10:5000/api/calc"
	data = {
		"message" : message
	}
	headers={'Content-Type': 'application/json'}
	r = s.post(url=url, data=json.dumps(data), headers=headers)
	text = r.text
	text = json.loads(text)
	print("人数を計算しました。現在%s人います。"%text)
	return text

if __name__ == '__main__':
	message = sys.argv[1]
	number = calcPost(message)
	message= "現在%s人います。"%number
	# twitterPost(message)
	linePost(message)
	# slackPost(message)
