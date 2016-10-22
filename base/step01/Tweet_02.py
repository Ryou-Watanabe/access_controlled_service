#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from requests_oauthlib import OAuth1Session
from datetime import datetime as dt

json_num = {
    'message':'2人'
}

num = json.dumps(json_num)

num=json.loads(num)
#print num["message"] # 2人

consumer_key = " "
consumer_secret = " "
access_token = " "
access_secret = " "

twitter = OAuth1Session(consumer_key,consumer_secret,access_token,access_secret)

def tweet_num(number):
    now = dt.now().strftime('%m/%d %H:%M:%S')
    params = {"status": number + "\n\n" + now}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)

if __name__ == '__main__':
    tweet_num(num["message"])
