import requests

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co"

    def get_stock_price_change(self, symbol):
        url = f"{self.base_url}/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            time_series = data.get('Time Series (Daily)', {})
            latest_date = list(time_series.keys())[0]
            latest_close = float(time_series[latest_date]['4. close'])
            previous_date = list(time_series.keys())[1]
            previous_close = float(time_series[previous_date]['4. close'])
            price_change = ((latest_close - previous_close) / previous_close) * 100
            return price_change
        else:
            print("Error fetching stock data. Status Code:", response.status_code)
            return None
