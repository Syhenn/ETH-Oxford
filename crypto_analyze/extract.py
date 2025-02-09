import json
def extraction():
    path = "data.json"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    tweets_info = [{"Texte": tweet["Texte"], "Retweets": tweet["Retweets"]} for tweet in data]
    print(tweets_info)

    return tweets_info
