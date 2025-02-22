import json
from newsapi import NewsApiClient

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key='3be190842de64ec492113f90af6ae055')

def fetch_news(query, language="en", sort_by="relevancy"):
    everything = newsapi.get_everything(q=query, language=language, sort_by=sort_by)

    #Print response
    #print(json.dumps(everything, indent=4)) 

    # Handle API errors
    if everything.get("status") != "ok":
        print("Error:", everything.get("message", "Unknown error"))
        return []

    # Extract title and content
    articles_data = [
        {
            "title": article["title"],
            "content": article.get("content") or article.get("description") or "No content available"
        }
        for article in everything.get("articles", [])
    ]

    # Save data as JSON file
    with open("news_data.json", "w", encoding="utf-8") as json_file:
        json.dump(articles_data, json_file, indent=4, ensure_ascii=False)
        json_file.flush()  # Ensures writing is complete

    #print("✅ JSON file saved as 'news_data.json'")
    return articles_data

fetch_news("usa")
