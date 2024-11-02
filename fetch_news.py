import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"
COUNTRY = "us" 

def fetch_news_data():

    try:
        params = {
            'apiKey': API_KEY,
            'country': COUNTRY
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        if news_data["status"] == "ok":
            articles = news_data["articles"]
            news_list = []
            for article in articles:
                news_item = {
                    "Title": article["title"],
                    "Source": article["source"]["name"],
                    "Published At": article["publishedAt"]
                }
                news_list.append(news_item)
            return news_list
        else:
            print("Failed to fetch news data.")
            return []
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

def save_news_to_excel(news_list):

    if news_list:
        news_df = pd.DataFrame(news_list)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"news_batch_{timestamp}.xlsx"
        
        news_df.to_excel(filename, index=False)
        print(f"Saved news to {filename}")
    else:
        print("No news data to save.")
