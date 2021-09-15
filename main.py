from config import getApi
import os
import time

# if you are not french translate comment to french

os.system('cls')

api = getApi()

tweets = 15
searchs = 15
limitTweets = 100
limitSearchs = 200

def postStatus(update, inReplyTo):
    global tweets
    tweets += 1
    status = api.PostUpdate(update, in_reply_to_status_id=inReplyTo)

def search(research, howMany):
    global searchs
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany)
    for search in searchResults:
        postStatus("@" + search.user.screen_name + " Streameur is not a job !", search.id)

def start():
    global searchs
    global tweets
    global limitSearchs
    global limitTweets
    stop = False
    while stop == False: # mettre un fichier de log
        try:
            search("twitch", str(tweets))
        except:
            stop = True
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            stop = True
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            stop = True
        print(f"On a tweeté {str(tweets)} tweets wow :)")
        time.sleep(5)
    print("Fini !")

start()

# BOT fait un peu a l'arrache et avec quelque bug
# j'ai franchement eu la flemme de a faire un fichier de log et de corriger les quelques bugs
# si tu veux faire un bot du genre inspire toi et travaille toi même

# Dev By Fryzz Inspired Of V2F
