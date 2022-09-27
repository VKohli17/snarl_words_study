import tweepy
import csv 
import time 

def fetch_keys():
    api_file = open("api_keys.txt", "r")
    consumer_key = api_file.readline().strip("\n")
    consumer_secret = api_file.readline().strip("\n")
    access_token = api_file.readline().strip("\n")
    access_token_secret = api_file.readline().strip("\n")
    label = api_file.readline().strip("\n")

    # access token (and secret ) not required for now
    return consumer_key, consumer_secret, label

def authenticate(consumer_key, consumer_secret):
    
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    return api, auth

def fetch_data(api, csvWriter, query, label, fromDate, toDate):

    tweets = api.search_full_archive(
        label = label,
        query=query,
        fromDate=fromDate,
        toDate=toDate,
        maxResults=100
    )

    return tweets

def iterative_query(api, num_tweets, year, label):

    outfile = open("data/data_{}.csv".format(year), "a")
    csvWriter = csv.writer(outfile)

    formDate = "{}01010000".format(year)
    toDate = "{}01010000".format(year+1)

    for i in range(int(num_tweets/100)):
        try:
            tweets = fetch_data(api, csvWriter,
                        query="bhakt", 
                        label=label, 
                        fromDate=formDate,
                        toDate=toDate)
            for tweet in tweets:
                csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        except tweepy.errors.TooManyRequests:
            time.sleep(15*60)

consumer_key, consumer_secret, label = fetch_keys()

print(consumer_key)

api, auth = authenticate(consumer_key=consumer_key, consumer_secret=consumer_secret)


the_years = input("Enter the years for which you want the data for: ").split(" ")

for year_str in the_years:
    iterative_query(api, 400, int(year_str), label)
