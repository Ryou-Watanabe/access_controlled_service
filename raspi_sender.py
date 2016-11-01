#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

def post(message):
	s = requests.session()
	url = "http://"+ip+":5000/api/post"
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
	ip = sys.argv[2]
	
	number = post(message)
	message= "現在%s人います。"%number
