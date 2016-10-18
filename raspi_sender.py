#! /usr/bin/env python
# -*- coding: utf-8 -*-
#*******************************************
# Name:        	raspi_sender.py
# Author:      	Ryou.W
# Created:     	18/10/2016
# Last Date:   	18/10/2016
# Note:			python raspi_sender.py message
# Issue:
# Reference:
#*******************************************

import sys
import requests
import json


def post(message):
	s = requests.session()
	url = "http://192.168.2.1:5000/api/tweet"
	data = {
	"message" : message
	}
	headers={'Content-Type': 'application/json'}
	# r = s.get(url=url, params=data)
	r = s.post(url=url, data=json.dumps(data), headers=headers)
	text = r.text
	text = json.loads(text)
	print("「"+text.encode("utf-8")+"」をツイートしました")
	# return r.text.encode("utf-8")

if __name__ == '__main__':
	post(sys.argv[1])
