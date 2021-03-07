import twitter

def getApi(): # 4 key you can have with twitter developpeur account - twitter API
    return twitter.Api(consumer_key='',
                    consumer_secret='',
                    access_token_key='',
                    access_token_secret='')