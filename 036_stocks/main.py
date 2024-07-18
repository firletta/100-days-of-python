from alpha_vintage_api import AlphaVantageAPI
from news_api import NewsAPI
from twilio_api import TwilioAPI

from config import ALPHA_VANTAGE_API_KEY, NEWS_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, MY_PHONE_NUMBER

SYMBOL = "BTC"
NAME = "Bitcoin"


def main():
    alpha_vantage = AlphaVantageAPI(ALPHA_VANTAGE_API_KEY)
    news_api = NewsAPI(NEWS_API_KEY)
    twilio = TwilioAPI(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN,
                       TWILIO_PHONE_NUMBER)

    price_change = alpha_vantage.get_stock_price_change(SYMBOL)

    if price_change and abs(price_change) >= 5:
        news_articles = news_api.get_news(keyword=NAME)

    if news_articles:
        message = f"{SYMBOL}: {"🔺" if price_change > 0 else "🔻"}{abs(price_change):.2f}%\n\n"
        for article in news_articles:
            message += f"**{article["title"]}**\n{article["description"]}\n{article['url']}\n\n"
        twilio.send_sms(message=message, to_phone_number=MY_PHONE_NUMBER)


if __name__ == "__main__":
    main()
