import schedule
import time
from fetch_news import fetch_news_data, save_news_to_excel

def fetch_and_save_news():
    news_data = fetch_news_data()
    save_news_to_excel(news_data)

fetch_and_save_news()

schedule.every(10).seconds.do(fetch_and_save_news)

print("News automation scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(1)
