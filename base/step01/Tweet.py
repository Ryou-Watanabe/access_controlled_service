import tweepy

class tweet_num:
    def __init__(self):
        self.cs_key=" "
        self.cs_secret=" "
        self.api_key=" "
        self.api_secret=" "

        self.auth = tweepy.OAuthHandler(self.cs_key, self.cs_secret)
        self.auth.set_access_token(self.api_key, self.api_secret)
        self.api = tweepy.API(self.auth)

    def tweet(self,text):
        self.api.update_status(text)


if __name__ == '__main__':
    tweet_num().tweet('test123')
