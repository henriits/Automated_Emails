from pprint import pprint

# API key abdc73e693b94dae98b16b7845f97039

import requests

topic = "python programming"

api_key = "abdc73e693b94dae98b16b7845f97039"
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'sortBy=publishedAt&'
       'apiKey=abdc73e693b94dae98b16b7845f97039&'
       'language=en')

request = requests.get(url)

# Get a Dictionary with data
content = request.json()

articles = content["articles"]

# Access the article titles and description
body = ""
for article in articles:
    body = body + article["title"] + "\n" + article["url"] + (2 * "\n")

# body = body.encode("utf-8")
print(body)


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass
