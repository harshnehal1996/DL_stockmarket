import tweepy
import sys

class MyStreamListener(tweepy.StreamListener):

        def on_status(self, status):
                    print(status.text)



def main():
    auth = tweepy.OAuthHandler(sys.argv[1],sys.argv[2])
    auth.set_access_token(sys.argv[3],sys.argv[4])
    api = tweepy.API(auth)

    stream_listener = MyStreamListener()
    stream = tweepy.Stream(auth = api.auth, listener=stream_listener)
    stream.filter(track=['airtel'])

if __name__ == '__main__':
    main()
