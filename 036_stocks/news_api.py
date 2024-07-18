import requests

class NewsAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"

    def get_news(self, keyword: str):
        url = f"{self.base_url}/everything?q={keyword}&apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            return articles[:1][0]
        else:
            print("Error fetching news data. Status Code:", response.status_code)
            return None
