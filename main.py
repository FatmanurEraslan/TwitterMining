import tweepy  # This library provide to fetch data from Twitter
import yweather
import json

consumer_key = ""
consumer_secret = ""
endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json"
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class City:
    def __init__(self, name, woeid, topics):
        self.name = name
        self.topics = topics
        self.woeid = woeid


# For getting the TT  from the Twitter

def get_topic():
    with open('./woeid.json', 'rb') as f:
        data = json.load(f)
    for i in data['cities']:
        topics = []
        trends = api.get_place_trends(id=i['woeid'])
        for value in trends:
            for trend in value['trends'][:20]:
                topics.append(trend['name'])
        cities.append((i['name'], i['woeid'], topics))


def fetch():  # it's help to fetch woeid
    client = yweather.Client()
    woeid = client.fetch_woeid('Australia')
    print(woeid)


def search():
    param_args = {'environment_name': 'prod', 'query': 'Coronavirus place:Las Vegas', 'fromDate': '202010290000',
                  'toDate': '202011250000', }
    # tweet_results = api.search_30_day(label='research', query="RBI", fromDate="202111100000", toDate="202111300000")
    # get = tweepy.Cursor(api.search_full_archive,label='prod',environment_name='prod',query="trend", fromDate="202111100000", toDate="202111300000").items(100)
    # get = api.search_30_day(label="dev", query="Trump -is:retweet lang:es", maxResults=10, fromDate=202111100000,toDate=202111300000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cities = []
    get_topic()
    for city in cities:
        print(city)
