import json
from newsapi import NewsApiClient

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key='3be190842de64ec492113f90af6ae055')


def fetch_news(query, language="en", sort_by="relevancy"):
    # Fetch top headlines
    everything = newsapi.get_everything(q=query, language=language, sort_by=sort_by)
    #print(json.dumps(everything, indent=4))


    # Extract title and content from articles
    articles_data = [
        {"title": article["title"], "content": article["content"]}
        for article in everything.get("articles", [])
    ]

    # Save data as JSON file
    with open("news_data.json", "w", encoding="utf-8") as json_file:
        json.dump(articles_data, json_file, indent=4, ensure_ascii=False)

    #print("JSON file saved as 'news_data.json'")
    
    return articles_data

fetch_news("usa")