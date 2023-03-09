

import requests



class NewsFeed:
    base_url = "https://newsapi.org/v2/everything"
    api_key = "abdc73e693b94dae98b16b7845f97039"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = (f'{self.base_url}?'
               f'q={self.interest}&'
               f'from={self.from_date}&'
               f'to={self.to_date}&'
               f'apiKey={self.api_key}&'
               f'language={self.language}')

        request = requests.get(url)
        content = request.json()
        articles = content["articles"]

        # Access the article titles and description
        body = ""
        for article in articles:
            body = body + article["title"] + "\n" + article["url"] + (2 * "\n")

        return body


news_feed = NewsFeed(interest="python", from_date="2023-03-08", to_date="2023-03-09", language="en")
print(news_feed.get())